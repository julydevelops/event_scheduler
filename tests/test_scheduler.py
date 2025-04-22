from datetime import datetime

import pytest

from event_scheduler.event import Event
from event_scheduler.scheduler import Scheduler


@pytest.fixture
def sample_event():
    return Event("Sample", datetime(2025, 4, 18, 9, 0), 60)


@pytest.fixture
def overlapping_event():
    return Event("Sample", datetime(2025, 4, 18, 9, 30), 60)


def test_create_scheduler():
    scheduler = Scheduler()

    assert isinstance(scheduler.events, list)
    assert len(scheduler.events) == 0


def test_add_event(sample_event):
    scheduler = Scheduler()

    scheduler.add_event(sample_event)

    print(scheduler.events)

    assert len(scheduler.events) == 1
    assert scheduler.events[0].name == "Sample"
    assert scheduler.events[0].start_time == datetime(2025, 4, 18, 9, 0)
    assert scheduler.events[0].duration == 60


def test_add_overlapping_event(capfd, sample_event, overlapping_event):
    scheduler = Scheduler()

    scheduler.add_event(sample_event)
    scheduler.add_event(overlapping_event)

    out, err = capfd.readouterr()
    assert "ERROR: Cannot add event since it overlaps with existing event." in out


def test_get_events(sample_event):
    scheduler = Scheduler()

    scheduler.add_event(sample_event)
    events = scheduler.get_events_by_date(datetime(2025, 4, 18, 9, 0).date())

    assert len(events) == 1
    assert events[0].name == "Sample"
    assert events[0].start_time == datetime(2025, 4, 18, 9, 0)
    assert events[0].duration == 60


def test_remove_event(sample_event):
    scheduler = Scheduler()

    scheduler.add_event(sample_event)

    assert len(scheduler.events) == 1

    scheduler.remove_event("Sample")

    assert len(scheduler.events) == 0


def test_next_event(sample_event):
    scheduler = Scheduler()

    scheduler.add_event(sample_event)

    next_event = scheduler.get_next_event(datetime(2025, 4, 18, 8, 0))

    assert len(next_event) == 1
    assert next_event[0].name == "Sample"
