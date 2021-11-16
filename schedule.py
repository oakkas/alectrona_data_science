import pandas as pd
pd.set_option('expand_frame_repr', False)

class Schedule():
  def __init__(self):
    days = {
          'Monday': {'7 AM - 8 AM': '', '8 AM - 9 AM': '', '9 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 1 PM': '', '1 PM - 2 PM': '', '2 PM - 3 PM': '', '3 PM - 4 PM': '', '4 PM - 5 PM': '', '5 PM - 6 PM': '', '6 PM - 7 PM': '', '7 PM - 8 PM': '', '8 PM - 9 PM': '', '9 PM - 10 PM': ''},
          'Tuesday': {'7 AM - 8 AM': '', '8 AM - 9 AM': '', '9 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 1 PM': '', '1 PM - 2 PM': '', '2 PM - 3 PM': '', '3 PM - 4 PM': '', '4 PM - 5 PM': '', '5 PM - 6 PM': '', '6 PM - 7 PM': '', '7 PM - 8 PM': '', '8 PM - 9 PM': '', '9 PM - 10 PM': ''},
          'Wednesday': {'7 AM - 8 AM': '', '8 AM - 9 AM': '', '9 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 1 PM': '', '1 PM - 2 PM': '', '2 PM - 3 PM': '', '3 PM - 4 PM': '', '4 PM - 5 PM': '', '5 PM - 6 PM': '', '6 PM - 7 PM': '', '7 PM - 8 PM': '', '8 PM - 9 PM': '', '9 PM - 10 PM': ''},
          'Thursday': {'7 AM - 8 AM': '', '8 AM - 9 AM': '', '9 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 1 PM': '', '1 PM - 2 PM': '', '2 PM - 3 PM': '', '3 PM - 4 PM': '', '4 PM - 5 PM': '', '5 PM - 6 PM': '', '6 PM - 7 PM': '', '7 PM - 8 PM': '', '8 PM - 9 PM': '', '9 PM - 10 PM': ''},
          'Friday': {'7 AM - 8 AM': '', '8 AM - 9 AM': '', '9 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 1 PM': '', '1 PM - 2 PM': '', '2 PM - 3 PM': '', '3 PM - 4 PM': '', '4 PM - 5 PM': '', '5 PM - 6 PM': '', '6 PM - 7 PM': '', '7 PM - 8 PM': '', '8 PM - 9 PM': '', '9 PM - 10 PM': ''}
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
