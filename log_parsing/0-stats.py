#!/usr/bin/python3
"""Read HTTP logs from stdin and print cumulative metrics."""

import re
import sys


VALID_CODES = (200, 301, 400, 401, 403, 404, 405, 500)
LOG_PATTERN = re.compile(
    r'^(\d{1,3}(?:\.\d{1,3}){3}) - \[([^\]\r\n]+)\] '
    r'"GET /projects/260 HTTP/1\.1" (\S+) ([0-9]+)$'
)


def print_stats(total_size, counts):
    """Print the total size and status counts in ascending order."""
    print("File size: {}".format(total_size))
    for code in VALID_CODES:
        if counts[code]:
            print("{}: {}".format(code, counts[code]))


def parse_line(line):
    """Return the status and size, or None for a malformed log."""
    match = LOG_PATTERN.match(line.rstrip('\r\n'))
    if match is None:
        return None

    if any(int(part) > 255 for part in match.group(1).split('.')):
        return None

    try:
        status = int(match.group(3))
    except ValueError:
        status = None

    return status, int(match.group(4))


def main():
    """Process stdin without running when the module is imported."""
    total_size = 0
    line_count = 0
    counts = {code: 0 for code in VALID_CODES}

    try:
        for line in sys.stdin:
            line_count += 1
            parsed = parse_line(line)

            if parsed is not None:
                status, size = parsed
                total_size += size
                if status in counts:
                    counts[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, counts)

    except KeyboardInterrupt:
        print_stats(total_size, counts)
        raise

    if line_count == 0 or line_count % 10 != 0:
        print_stats(total_size, counts)


if __name__ == "__main__":
    main()
