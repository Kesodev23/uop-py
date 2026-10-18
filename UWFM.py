#Cleaning raw feedback
def Question1():
    raw = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "

    text = raw.strip()                      # remove leading/trailing spaces
    text = text.lower()                     # convert to lowercase
    text = text.replace("speaker", "presenter")  # standardize wording
    text = " ".join(text.split())           # remove extra internal spaces
    text = text.title()                     # title case

    print(f"Cleaned feedback: {text}")



#Writing, reading, and appending feedback
def Question2():
    feedback_list = [
        "The Presenter Was Great But The Room Was Cold",
        "The Workshop Examples Were Great",
        "More Time For Questions Would Help",
    ]

    with open("feedback.txt", "w") as file:      # write mode
        for message in feedback_list:
            file.write(message + "\n")

    print("--- Original feedback ---")
    with open("feedback.txt", "r") as file:      # read mode
        for line in file:
            print(line.strip())

    with open("feedback.txt", "a") as file:      # append mode
        file.write("Registration Was Quick And Easy\n")

    print("--- Updated feedback ---")
    with open("feedback.txt", "r") as file:
        for line in file:
            print(line.strip())


#Exception handling for file reading
from unittest.mock import patch

def read_feedback(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found. Please create feedback.txt first.")
    except PermissionError:
        print("Permission denied. Close the file and try again.")
    finally:
        print("Operation completed.")

def Question3():
    print("Test 1: file exists")
    read_feedback("feedback.txt")

    print("\nTest 2: file missing")
    read_feedback("missing_feedback.txt")

    print("\nTest 3: simulated locked file")
    with patch("builtins.open", side_effect=PermissionError):
        read_feedback("feedback.txt")


#Counting mentions of "great" and writing a summary
def Question4():
    with open("feedback.txt", "r") as file:
        lines = file.readlines()

    total = len(lines)
    great_count = 0
    for line in lines:
        if "great" in line.lower():          # case-insensitive check
            great_count += 1

    with open("summary.txt", "w") as summary:
        summary.write("=== Workshop Feedback Summary ===\n")
        summary.write(f"Total Feedback: {total}\n")
        summary.write(f"Mentions of 'Great': {great_count}\n")

    print("=== Workshop Feedback Summary ===")
    print(f"Total Feedback: {total}")
    print(f"Mentions of 'Great': {great_count}")

def Display_Menu(menu_list):
    print('Select Option Below:\n','='*20)
    for index,name in menu_list.items():
        print(f'{index}. {name}')
    print('='*40)

def Prompt_user():
    response = False
    while not response:
        Display_Menu(menu_list)
        user_choice = 0
        try:
            user_choice = int(input("Select option index to proceed "))
            response = user_choice>=1 and user_choice <=4
            if response:
                Method_Selected(user_choice)
        except ValueError:
           print('Input is not a valid index')
        

def Method_Selected(index):
    if index == 1:
        Question1()
    elif index == 2:
        Question2()
    elif index == 3:
        Question3()
    else:
        Question4()

def run():
    Prompt_user()

menu_list={'1':Question1.__name__,'2':Question2.__name__,'3':Question3.__name__,'4':Question4.__name__}

cont = True
while cont:
    try:
        run()
        user_input = str(input("\nDo you want to Continue? "))
        if user_input.isalpha():
            cont = user_input.strip().capitalize().startswith('Ye')
        
    except ValueError:
        print('Options are Yes/ No!')

print(f'{'<<.>>'*10}\nThanks for your time! Much appreciated. \n\nAu revoir!\n{'<<->>'*10}')
    