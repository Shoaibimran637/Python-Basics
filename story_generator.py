# Story Generator
print("Python Mini Projects\n".center(60), "Story Generator")
print("""
You and your friends found a brick of gold in the middle of the forest and you are wondering what to do with it. You have to choose one of the following options:
A. Take all the gold and kill the other 2 friends
B. Split the gold between 3 friends
""")
choice = input("Choose Options: A / B: " )
if choice == "A":
    print("Your other 2 friends will think the same and kill you, so you failed the test.")
elif choice == "B":
    print("You and your friends split the gold and you all get 1/3 each; hence you pass the test.")
else:
    print("Invalid choice. Please choose A or B.")
