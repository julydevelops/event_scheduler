from datetime import datetime
from scheduler import Scheduler
from event import Event

def main():
  scheduler = Scheduler()

  e1 = Event("Meeting", datetime(2025, 4, 18, 9, 0), 60)
  e2 = Event("Standup", datetime(2025, 4, 18, 9, 30), 30)
  # e3 = Event("1:1", datetime(2025, 4, 18, 11, 0), 30)

  scheduler.add_event(e1)
  scheduler.add_event(e2)
  # scheduler.add_event(e3)

  # print(scheduler.get_events_by_date(datetime(2025, 4, 18).date()))
  # print(scheduler.get_next_event(datetime(2025, 4, 18, 9, 30)))
  # scheduler.remove_event("1:1")

  # print(scheduler.events)

# Only runs if this script is executed directly (not imported)
if __name__ == "__main__":
  main()