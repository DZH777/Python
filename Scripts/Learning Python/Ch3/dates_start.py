#
# Example file for working with date information
#

import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = datetime.date.today()
  print("Today's date is", today)

  # print out the date's individual components
  print("Date components:", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today's weekday number is", today.weekday())
  days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  print("Today's weekday name is", days[today.weekday()])
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.datetime.now()
  print("Current date and time", today)
  # Get the current time
  t = datetime.datetime.time(today)
  print(t)
  
if __name__ == "__main__":
  main();
  
