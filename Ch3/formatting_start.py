#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()

  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  # Lowercase stands for abbreviated years, weekdays, and months
  print('')
  print("Here is an example of the strftime formatting in use - 1 variable at a time.")
  print(now.strftime("The current year is: %Y"))
  print(now.strftime("The current weekday is: %A"))
  print(now.strftime("The current month is: %B"))
  print(now.strftime("The current day of the month is: %d"))
  print('')

  print("Here is an example of the strftime formatting in use - multiple variables at a time.")
  print(now.strftime("%a, %d %B, %y"))
  print('')

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print("Here is an example of the gathering locale date and time.")
  print(now.strftime("Locale date and time: %c"))
  print(now.strftime("Locale date: %x"))
  print(now.strftime("Locale time: %X"))
  print('')

  #### Time Formatting ####


  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print("Here is an example of gathering time components.")
  print(now.strftime("Current time: %I:%M:%S, %p"))
  print(now.strftime("24-hour time: %H:%M:%S, %p"))

if __name__ == "__main__":
  main();
