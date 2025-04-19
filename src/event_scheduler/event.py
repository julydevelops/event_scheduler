from datetime import timedelta

class Event:
  def __init__(self, name, start_time, duration_minutes):
    self.name = name
    self.start_time = start_time
    self.end_time = self.start_time + timedelta(minutes=duration_minutes)
    self.duration_minutes = duration_minutes
  
  def __repr__(self):
    return (f"Event(name='{self.name}', "
            f"start_time='{self.start_time.strftime('%Y-%m-%d %H:%M')}', "
            f"duration={self.duration_minutes} mins)")