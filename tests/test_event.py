from datetime import datetime, timedelta

import pytest

from event_scheduler.errors import EventValidationError
from event_scheduler.event import Event


# Creating an Event with valid name, start_time, and duration_minutes
def test_create_event():
    name = "Team Meeting"
    start_time = datetime(2023, 5, 10, 14, 30)
    duration = 60

    event = Event(name, start_time, duration)

    assert event.name == name
    assert event.start_time == start_time
    assert event.duration == duration
    assert event.end_time == start_time + timedelta(minutes=duration)


def test_multiple_validation_errors():
    with pytest.raises(EventValidationError) as exc_info:
        Event("", "not a datetime", -5)

    errors = exc_info.value.errors
    assert "name cannot be empty" in errors
    assert "start_time is not a valid datetime" in errors
    assert "duration must be a positive integer" in errors
    assert len(errors) == 3
