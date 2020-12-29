print("Welcome to the program")
u_res = input("Enter 1 to continue ?")

if u_res == "1":
  u_res2 = input(f"You have chosen {u_res} to continue. What is your name? ")
  if u_res2 == "Eli":
    print(f"I know you {u_res2}")
  else:
    print("I dont know you")
else:
  print(f"You have chosen {u_res}, so you cant continue!")