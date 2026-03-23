def tail_large_file(filename, n, block_size=1024):
    """Efficiently read last n lines from large file"""

    with open(filename, 'rb') as f:
        # Move to end of file
        f.seek(0, 2)
        file_size = f.tell()

        lines_found = []
        block_num = -1
        blocks = []

        while len(lines_found) < n and file_size > 0:
            if file_size - block_size > 0:
                # Read one block from end
                f.seek(block_num * block_size, 2)
                blocks.append(f.read(block_size))
            else:
                # Read remaining bytes
                f.seek(0, 0)
                blocks.append(f.read(file_size))

            lines_found = b''.join(reversed(blocks)).decode('utf-8').splitlines()

            block_num -= 1
            file_size -= block_size

        # Print last n lines
        for line in lines_found[-n:]:
            print(line)