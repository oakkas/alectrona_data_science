import pandas as pd
pd.set_option('expand_frame_repr', False)

class Schedule():
  def __init__(self):
    days = {
          'Monday': {'07 AM - 08 AM': '', '08 AM - 09 AM': '', '09 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 01 PM': '', '01 PM - 02 PM': '', '02 PM - 03 PM': '', '03 PM - 04 PM': '', '04 PM - 05 PM': '', '05 PM - 06 PM': '', '06 PM - 07 PM': '', '07 PM - 08 PM': '', '08 PM - 09 PM': '', '09 PM - 10 PM': ''},
          'Tuesday': {'07 AM - 08 AM': '', '08 AM - 09 AM': '', '09 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 01 PM': '', '01 PM - 02 PM': '', '02 PM - 03 PM': '', '03 PM - 04 PM': '', '04 PM - 05 PM': '', '05 PM - 06 PM': '', '06 PM - 07 PM': '', '07 PM - 08 PM': '', '08 PM - 09 PM': '', '09 PM - 10 PM': ''},
          'Wednesday': {'07 AM - 08 AM': '', '08 AM - 09 AM': '', '09 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 01 PM': '', '01 PM - 02 PM': '', '02 PM - 03 PM': '', '03 PM - 04 PM': '', '04 PM - 05 PM': '', '05 PM - 06 PM': '', '06 PM - 07 PM': '', '07 PM - 08 PM': '', '08 PM - 09 PM': '', '09 PM - 10 PM': ''},
          'Thursday': {'07 AM - 08 AM': '', '08 AM - 09 AM': '', '09 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 01 PM': '', '01 PM - 02 PM': '', '02 PM - 03 PM': '', '03 PM - 04 PM': '', '04 PM - 05 PM': '', '05 PM - 06 PM': '', '06 PM - 07 PM': '', '07 PM - 08 PM': '', '08 PM - 09 PM': '', '09 PM - 10 PM': ''},
          'Friday': {'07 AM - 08 AM': '', '08 AM - 09 AM': '', '09 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 01 PM': '', '01 PM - 02 PM': '', '02 PM - 03 PM': '', '03 PM - 04 PM': '', '04 PM - 05 PM': '', '05 PM - 06 PM': '', '06 PM - 07 PM': '', '07 PM - 08 PM': '', '08 PM - 09 PM': '', '09 PM - 10 PM': ''}
          }
    
    self.initial_schedule = pd.DataFrame.from_dict(days)
  
  def add_course(self, course, course_schedule):
    for schedule in course_schedule:
      column = list(schedule.keys())[0]
      hours = schedule[column]
      for hour in hours:
        self.initial_schedule.at[hour, column] = course

  def display(self):
    print(self.initial_schedule)
