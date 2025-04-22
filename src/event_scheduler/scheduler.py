class Scheduler:
    def __init__(self):
        # TODO: Store this in a DB
        self.events = []

    def add_event(self, event):
        """Add an event if it does not overlap with existing events."""
        if self._is_overlapping(event):
            print("ERROR: Cannot add event since it overlaps with existing event.")
            return
        self.events.append(event)

    def get_events_by_date(self, date):
        """Return events occurring on the given date."""
        return [event for event in self.events if event.start_time.date() == date]

    def remove_event(self, name):
        """Remove all events with the given name."""
        self.events = [event for event in self.events if event.name != name]

    def get_next_event(self, current_time):
        """Return events starting after the current_time."""
        return [event for event in self.events if event.start_time > current_time]

    def _is_overlapping(self, new_event):
        """Check if new_event overlaps with any existing event."""
        for event in self.events:
            if new_event.start_time < event.end_time and new_event.end_time > event.start_time:
                return True
        return False
