# Write your code below:

def google_welcome(name): 
  print("Welcome to crome v18.12 " + name)

def destination_setup(location, cortana, estimated_time, time="user"):
  print("Would you like to enable location? " + location)
  print("Would you like to enable cortana? " + cortana)
  print("What time zone do you live in? " + time)
  print("Your device ill be ready in about " + str(estimated_time) + " hours")


def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time


google_welcome(" <YOUR NAME HERE> ")
estimate = estimated_time_rounded(2.43)
destination_setup(" <YES OR NO> ", "<YES OR NO> ", estimate, "user")



