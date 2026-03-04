from datetime import datetime
import heapq


class DataCenterSimulator:
    def __init__(self):
        self.servers = {}          # server_id -> status
        self.failure_events = []   # min heap of (time, server_id)
        self.recovery_events = []  # min heap of (time, server_id)

    def add_failure(self, server_id, failure_time):
        """Schedule a server failure"""
        heapq.heappush(self.failure_events, (failure_time, server_id))

    def add_recovery(self, server_id, recovery_time):
        """Schedule a server recovery"""
        heapq.heappush(self.recovery_events, (recovery_time, server_id))

    def simulate_until(self, end_time):
        """Run simulation until specified time"""
        events = []

        # Combine all failure events
        for time, server in self.failure_events:
            if time <= end_time:
                events.append((time, server, 'failure'))

        # Combine all recovery events
        for time, server in self.recovery_events:
            if time <= end_time:
                events.append((time, server, 'recovery'))

        # Sort events by time
        events.sort()

        timeline = []

        # Process events
        for time, server, event_type in events:
            if event_type == 'failure':
                self.servers[server] = 'failed'
            else:
                self.servers[server] = 'active'

            timeline.append({
                'time': time,
                'server': server,
                'event': event_type,
                'total_failed': sum(
                    1 for s in self.servers.values() if s == 'failed'
                )
            })

        return timeline

    def get_availability(self, start_time, end_time):
        """Calculate availability percentage"""
        total_server_time = len(self.servers) * (end_time - start_time)
        failed_time = 0

        # Calculate downtime for each server
        # (Implementation depends on detailed event tracking)

        if total_server_time == 0:
            return 100

        return (total_server_time - failed_time) / total_server_time * 100