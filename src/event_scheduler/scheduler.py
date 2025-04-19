from datetime import datetime, timedelta

class Scheduler:
  def __init__(self):
    # TODO: Store this in a DB
    self.events = list()

  def add_event(self, event):
    if self._is_overlapping(event):
      print("ERROR: Cannot add event since it overlaps with existing event.")
    else:
      self.events.append(event)

  def get_events_by_date(self, date):
    # List comprehension
    return [event for event in self.events if event.start_time.date() == date]
  
    # Funtional
    # return list(filter(lambda event: event.start_time.date() == date, self.events))

  def remove_event(self, name):
    # TODO: Consider more efficient way of removing element
    self.events = [event for event in self.events if event.name != name]

  def get_next_event(self, current_time):
    return [event for event in self.events if event.start_time > current_time]
  
  def _is_overlapping(self, new_event):
    for event in self.events:
      if (new_event.start_time < event.end_time or event.end_time < new_event.end_time):
        return True
      
    return False
    