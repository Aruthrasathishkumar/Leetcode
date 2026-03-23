from collections import deque

def tail(filename, n):
    """Print last n lines of file"""
    last_lines = deque(maxlen=n)

    try:
        with open(filename, 'r') as f:
            for line in f:
                last_lines.append(line.rstrip())

        for line in last_lines:
            print(line)

    except FileNotFoundError:
        print(f"Error: {filename} not found")