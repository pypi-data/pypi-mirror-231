import base64
import copy
import fcntl
import json
import os
import random
import socket
import sys
import time


MAX_WRITE = 2048


class PacketTooLarge(Exception):
    ...


class Agent(object):
    def __init__(self, logger=None):
        self.buffer = b''
        self.received_any_data = False
        self.last_data = time.time()

        self.output_fileno = None
        self.input_fileno = None

        self._command_map = {
            'ping': self.send_pong,
            'pong': self.noop,
            'json-decode-failure': self.log_error_packet,
            'command-error': self.log_error_packet,
            'unknown-command': self.log_error_packet,
        }

        self.log = logger
        self.poll_tasks = []

    def _read(self):
        d = None
        try:
            d = os.read(self.input_fileno, MAX_WRITE * 2)
            self.received_any_data = True
        except BlockingIOError:
            time.sleep(0.200)

        if d:
            self.last_data = time.time()
            if self.log:
                self.log.debug('Read: %s' % d)
        return d

    def _write(self, data):
        try:
            while data:
                os.write(self.output_fileno, data[:MAX_WRITE])
                data = data[MAX_WRITE:]
        except BlockingIOError:
            if self.log:
                self.log.info(
                    'Discarded write due to non-blocking IO error, no connection?')
            pass

    def set_fd_nonblocking(self, fd):
        oflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oflags | os.O_NONBLOCK)

    def add_command(self, name, meth):
        if self.log:
            self.log.debug('Registered command %s' % name)
        self._command_map[name] = meth

    def poll(self):
        if time.time() - self.last_data > 5:
            pts = self.poll_tasks
            if not pts:
                pts = [self.send_ping]

            for pt in pts:
                if self.log:
                    self.log.debug(
                        'Sending %s poll due to idle connection' % pt)
                pt()
            self.last_data = time.time()

    def close(self):
        if self.log:
            self.log.debug('Cleaning up connection for graceful close.')
        os.close(self.input_fileno)
        os.close(self.output_fileno)

    # Our packet format is:
    #
    #     *SFv001*XXXXXXX*YYYY
    #     ^........^........^
    #     0 byte   10th byte
    #
    # Where XXXXXXX is a eight character decimal length with zero padding (i.e. 00000100)
    # and YYYY is XXXXXXX bytes of UTF-8 encoded JSON
    PREAMBLE = '*SFv001*'

    def send_packet(self, p):
        j = json.dumps(p)
        j_len = len(j)

        if j_len > 99999999:
            raise PacketTooLarge(
                'The maximum packet size is 99,999,999 bytes of UTF-8 encoded JSON. '
                'This packet is %d bytes.' % j_len)

        packet = '%s[%08d]%s' % (self.PREAMBLE, j_len, j)
        self._write(packet.encode('utf-8'))
        if self.log:
            self.log.debug('Sent: %s' % packet)

    def find_packets(self):
        packet = self.find_packet()
        while packet:
            yield packet
            packet = self.find_packet()

    def find_packet(self):
        d = self._read()
        if d:
            self.buffer += d

        buffer_as_string = self.buffer.decode('utf-8')
        offset = buffer_as_string.find(self.PREAMBLE)
        if offset == -1:
            return None

        # Do we have any length characters?
        blen = len(self.buffer)
        len_end = offset + 17
        if blen < len_end:
            return None

        # Find the length of the body of the packet
        plen = int(buffer_as_string[offset + 9: len_end])
        if blen < len_end + 1 + plen:
            return None

        # Extract and parse the body of the packet
        packet = self.buffer[len_end + 1: len_end + 1 + plen]
        packet_as_string = packet.decode('utf-8')
        self.buffer = self.buffer[len_end + 1 + plen:]
        try:
            return json.loads(packet_as_string)
        except json.JSONDecodeError:
            if self.log:
                self.log.with_fields({'packet': packet_as_string}).error(
                    'Failed to JSON decode packet')
            self.send_packet(
                {
                    'command': 'json-decode-failure',
                    'message': ('failed to JSON decode packet: %s'
                                % packet.decode('utf-8'))
                })

    def dispatch_packet(self, packet):
        if self.log:
            lp = copy.copy(packet)
            if 'chunk' in lp:
                lp['chunk'] = '...'
            self.log.debug('Processing: %s' % lp)
        command = packet.get('command')

        if command in self._command_map:
            try:
                self._command_map[command](packet)
            except Exception as e:
                if self.log:
                    self.log.with_fields({'error': str(e)}).error(
                        'Command %s raised an error')
                self.send_packet(
                    {
                        'command': 'command-error',
                        'message': 'command %s raised an error: %s' % (command, e)
                    })
        else:
            if self.log:
                self.log.error('Could not find command "%s" in %s'
                               % (command, self._command_map.keys()))
            self.send_packet(
                {
                    'command': 'unknown-command',
                    'message': '%s is an unknown command' % command
                })

    def noop(self, packet):
        return

    def log_error_packet(self, packet):
        if self.log:
            self.log.with_fields(packet).error('Received a packet indicating an error')

    def send_ping(self, unique=None):
        if not unique:
            unique = random.randint(0, 65535)

        self.send_packet({
            'command': 'ping',
            'unique': unique
        })

    def send_pong(self, packet):
        self.send_packet({
            'command': 'pong',
            'unique': packet['unique']
        })

    def _path_is_a_file(self, command, path, unique):
        if not path:
            self.send_packet({
                'command': '%s-response' % command,
                'result': False,
                'message': 'path is not set',
                'unique': unique
            })
            return 'path is not set'

        if not os.path.exists(path):
            self.send_packet({
                'command': '%s-response' % command,
                'result': False,
                'path': path,
                'message': 'path does not exist',
                'unique': unique
            })
            return 'path does not exist'

        if not os.path.isfile(path):
            self.send_packet({
                'command': '%s-response' % command,
                'result': False,
                'path': path,
                'message': 'path is not a file',
                'unique': unique
            })
            return 'path is not a file'

        return None

    def _send_file(self, command, source_path, destination_path, unique):
        st = os.stat(source_path, follow_symlinks=True)
        self.send_packet({
            'command': command,
            'result': True,
            'path': destination_path,
            'stat_result': {
                'mode': st.st_mode,
                'size': st.st_size,
                'uid': st.st_uid,
                'gid': st.st_gid,
                'atime': st.st_atime,
                'mtime': st.st_mtime,
                'ctime': st.st_ctime
            },
            'unique': unique
        })

        offset = 0
        with open(source_path, 'rb') as f:
            d = f.read(1024)
            while d:
                self.send_packet({
                    'command': command,
                    'result': True,
                    'path': destination_path,
                    'offset': offset,
                    'encoding': 'base64',
                    'chunk': base64.b64encode(d).decode('utf-8'),
                    'unique': unique
                })
                offset += len(d)
                d = f.read(1024)

            self.send_packet({
                'command': command,
                'result': True,
                'path': destination_path,
                'offset': offset,
                'encoding': 'base64',
                'chunk': None,
                'unique': unique
            })


class SocketAgent(Agent):
    def __init__(self, path, logger=None):
        super(SocketAgent, self).__init__(logger=logger)
        self.s = socket.socket(socket.AF_UNIX)
        self.s.connect(path)
        self.input_fileno = self.s.fileno()
        self.output_fileno = self.s.fileno()
        self.set_fd_nonblocking(self.input_fileno)


class FileAgent(Agent):
    def __init__(self, path, logger=None):
        super(FileAgent, self).__init__(logger=logger)
        self.input_fileno = os.open(path, os.O_RDWR)
        self.output_fileno = self.input_fileno
        self.set_fd_nonblocking(self.input_fileno)


class StdInOutAgent(Agent):
    def __init__(self, logger=None):
        super(StdInOutAgent, self).__init__(logger=logger)
        self.input_fileno = sys.stdin.fileno()
        self.output_fileno = sys.stdout.fileno()
        self.set_fd_nonblocking(self.input_fileno)
