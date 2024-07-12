
height = int(input("What is your height: "))
credits = int(input("How much credits do u have: "))
min_height = 137
min_credits = 10

if height > min_height and credits > min_credits:
  print("Enjoy the ride! ")
elif height < min_height and credits > min_credits:
  print("You are not tall enough to ride. ")
elif height > min_height and credits < min_credits:
  print("You don't have enough credits. ")
else:
  print("You have not met any of the requirement. ")