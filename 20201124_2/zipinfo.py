import sys
from typing import Generator
import struct


class BytesReader:
    _buffer = b''
    _offset = 0

    def __init__(self, b: bytes):
        self._buffer = b

    def read(self, n: int):
        end = self._offset + n
        if len(self._buffer) <= self._offset:
            return b''
        if len(self._buffer) <= end:
            self._offset = len(self._buffer)
            return self._buffer[self._offset:]
        result = self._buffer[self._offset:end]
        self._offset = end
        return result

    def advance(self, n: int):
        self._offset += n


def read_struct(source, fmt):
    size = struct.calcsize(fmt)
    buffer = source.read(size)
    if len(buffer) < size:
        return None
    return struct.unpack(fmt, buffer)


def read_file_sizes(data: bytes) -> Generator[int, None, None]:
    reader = BytesReader(data)
    header_signature = 0x04034b50
    while True:
        res = read_struct(reader, fmt='<I')
        if res is None:
            return
        signature, = res
        if header_signature != signature:
            return
        res = read_struct(reader, fmt='<HHHHHIIIHH')
        if res is None:
            raise ValueError('Found incomplete file header')
        compressed_size, size, n, m = res[6:]
        title = reader.read(n=n).decode('utf-8')
        reader.advance(m + compressed_size)
        if not title.endswith('/'):
            yield size


def main():
    total_files = 0
    total_size = 0
    data = bytes.fromhex(sys.stdin.read())
    for size in read_file_sizes(data):
        total_files += 1
        total_size += size
    print(total_files, total_size)


if __name__ == '__main__':
    main()
