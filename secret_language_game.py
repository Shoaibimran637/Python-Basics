import random
import string

def code():
    message = input("Enter the message to code: ")
    words = message.split()
    new_words = []
    for word in words:
        if len(word) >= 3:
            new_word = word[1:] + word[0]
            random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
            new_word = random_chars + new_word + random_chars
            new_words.append(new_word)
        else:
            new_word = word[::-1]
            new_words.append(new_word)
    new_message = ' '.join(new_words)
    print(f"Your coded message is: {new_message}")

def decode():
    message = input("Enter the message to decode: ")
    words = message.split()
    new_words = []
    for word in words:
        if len(word) >= 3:
            new_word = word[3:-3]
            new_word = new_word[-1] + new_word[:-1]
            new_words.append(new_word)
        else:
            new_word = word[::-1]
            new_words.append(new_word)
    new_message = ' '.join(new_words)
    print(f"Your decoded message is: {new_message}")

def main():
    print("Welcome to the Secret Language Generator!")
    while True:
        choice = input("Do you want to code or decode? (a/b): ").lower()
        if choice == "a":
            code()
        elif choice == "b":
            decode()
        else:
            print("Invalid choice. Please try again.")
            continue

        another = input("Do you want to continue? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
  main()
