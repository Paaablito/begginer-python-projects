import random

user_selection = input("What do you choose? : rock(r), paper(p), scissors(s): ")

print(f"User selection: {user_selection}")
computer_selection = random.choice("rps")
print(f"Computer selection: {computer_selection}")

def rps(user_selection, computer_selection):
    if (user_selection == 'r' and computer_selection == 's') or (user_selection == 's' and computer_selection == 'p') or (user_selection == 'p' and computer_selection == 'r'):
        return True

if computer_selection == user_selection:
    print(f"It's a draw!")
elif rps(user_selection, computer_selection) == True:
    print("You win!")
else:
    print("You lost!")
