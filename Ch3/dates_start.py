#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today's date is", today)
  print('')

  # print out the date's individual components
  print("Date Components:", today.day, today.month, today.year)
  print('')

  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today's weekday number is", today.weekday())
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  print("Which is a", days[today.weekday()])
  print('')

  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("The current date and time is:",today)
  print('')

  # Get the current time
  t = datetime.time(datetime.now())
  print("The current time is:", t)
  
if __name__ == "__main__":
  main();
  