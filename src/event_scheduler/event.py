from datetime import datetime, timedelta

from event_scheduler.errors import EventValidationError


class Event:
    """
    Represents a scheduled event with a name, start time, and duration.
    """

    def __init__(self, name, start_time, duration):
        errors = self._validate_event(name, start_time, duration)

        if errors:
            raise EventValidationError(errors)

        self.name = name
        self.start_time = start_time
        self.duration = duration
        self.end_time = start_time + timedelta(minutes=duration)

    def _validate_event(self, name, start_time, duration):
        errors = []

        if not isinstance(name, str) or not name.strip():
            errors.append("name cannot be empty")

        if not isinstance(start_time, datetime):
            errors.append("start_time is not a valid datetime")

        if not isinstance(duration, int) or not (0 <= duration <= 1440):
            errors.append("duration must be a positive integer")

        return errors

    def __repr__(self):
        return (
            f"Event(name='{self.name}', "
            f"start_time='{self.start_time.strftime('%Y-%m-%d %H:%M')}', "
            f"duration={self.duration} mins)"
        )
