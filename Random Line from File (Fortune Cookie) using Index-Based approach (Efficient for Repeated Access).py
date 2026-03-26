import os
import random

class FortuneFile:
    def __init__(self, filename, delimiter='#'):
        self.filename = filename
        self.delimiter = delimiter
        self.indices = []
        self.last_modified = 0
        self._build_index()

    def _build_index(self):
        """Build index of fortune positions"""
        self.indices = []
        current_pos = 0

        with open(self.filename, 'r') as f:
            for line in f:
                if line.strip() == self.delimiter:
                    self.indices.append(current_pos)
                current_pos = f.tell()

        self.last_modified = os.path.getmtime(self.filename)

    def get_random(self):
        """Get random fortune using index"""

        # Rebuild index if file modified
        if os.path.getmtime(self.filename) != self.last_modified:
            self._build_index()

        if not self.indices:
            return None

        # Choose random starting position
        start_pos = random.choice(self.indices)

        with open(self.filename, 'r') as f:
            f.seek(start_pos)

            fortune_lines = []
            for line in f:
                if line.strip() == self.delimiter:
                    break
                fortune_lines.append(line.strip())

        return ' '.join(fortune_lines)