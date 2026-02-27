#!/usr/bin/env python3
import sys
import time
from collections import deque


def process_vmstat(metric, limit, count, window):
    limit = int(limit)
    count = int(count)
    window = int(window)

    violations = deque()
    headers = []
    first_line_skipped = False

    for line in sys.stdin:

        if line.startswith('procs'):
            headers = next(sys.stdin).split()
            metric_idx = headers.index(metric)
            continue

        if headers and not first_line_skipped:
            first_line_skipped = True
            continue

        if headers:
            data = line.split()
            if not data:
                continue

            value = int(data[metric_idx])
            current_time = time.time()

            # Remove old violations outside window
            while violations and violations[0][0] < current_time - window:
                violations.popleft()

            # Check for violation
            if value > limit:
                violations.append((current_time, value))

            if len(violations) > count:
                print(
                    f"Violation at {time.strftime('%Y-%m-%d %H:%M:%S')}: {value}"
                )


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: vmstat 1 | python script.py <metric> <limit> <count> <window>")
        sys.exit(1)

    _, metric, limit, count, window = sys.argv
    process_vmstat(metric, limit, count, window)