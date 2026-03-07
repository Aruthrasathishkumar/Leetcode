import os

for fd in range(3, 1024):
    try:
        os.close(fd)
    except OSError:
        pass