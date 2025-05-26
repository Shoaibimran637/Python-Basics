import random
secert_number = random.randint(1, 100)
guess = 0
attempts = 0
while guess != secert_number:
  try:
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1
    if guess < secert_number: 
      print("Hehe too low!")
    elif guess > secert_number:
      print("Hehe too high!")
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 100.")
      
print(f"Congratulations! You guessed the number in {attempts} attempts.")
