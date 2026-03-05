from collections import defaultdict, deque


class LogProcessor:
    def __init__(self, window_size=3600):  # 1 hour window
        self.window_size = window_size
        self.error_counts = defaultdict(lambda: deque())
        self.alert_threshold = 100

    def process_log_line(self, timestamp, log_line):
        """Process a single log line"""
        if self._is_error(log_line):
            error_type = self._extract_error_type(log_line)
            self._update_counts(error_type, timestamp)
            self._check_alerts(error_type, timestamp)

    def _update_counts(self, error_type, timestamp):
        """Update error counts with sliding window"""

        queue = self.error_counts[error_type]

        # Remove old entries outside the sliding window
        while queue and timestamp - queue[0] > self.window_size:
            queue.popleft()

        # Add current error timestamp
        queue.append(timestamp)

    def _check_alerts(self, error_type, timestamp):
        """Check if error threshold exceeded"""
        if len(self.error_counts[error_type]) >= self.alert_threshold:
            print(
                f"ALERT: {error_type} exceeded threshold at {timestamp}. "
                f"Count = {len(self.error_counts[error_type])}"
            )

    def _is_error(self, log_line):
        """Detect if log line represents an error"""
        return "error" in log_line.lower()

    def _extract_error_type(self, log_line):
        """Extract error type from log line"""
        words = log_line.lower().split()
        for word in words:
            if "error" in word:
                return word
        return "unknown_error"