import random
import time

def main():
    while True:
        operation = get_operation()
        max_number = get_max_number()
        play_game(operation, max_number)

def get_operation():
    while True:
        operation = input("Please enter an operation [+, -, x, /]: ")
        if operation in ['+', '-', 'x', '/']:
            return operation
        else:
            print("That is not a correct operation. Please try again [+, -, x, /]:")

def get_max_number():
    while True:
        try:
            max_number = int(input("Please enter a max number between 1 and 100: "))
            if 1 < max_number < 100:
                return max_number
            else:
                print("Invalid input. Please enter a valid max number.")
        except ValueError:
            print("Invalid input. Please enter a valid max number.")

def play_game(operation, max_number):
    timer = 30
    correct_answers = 0
    start_time = time.time()

    while timer > 0:
        current_time = time.time()
        elapsed_time = current_time - start_time
        timer = max(30 - int(elapsed_time), 0)

        num1 = random.randint(1, max_number)
        num2 = random.randint(1, max_number)
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        elif operation == 'x':
            correct_answer = num1 * num2
        else:
            correct_answer = num1 / num2

        print(f"{num1} {operation} {num2} = ?")
        print(f"You have {timer} seconds left.")
        answer = input("Enter an answer: ")

        if answer == str(correct_answer):
            print(f"{correct_answer} is correct!")
            correct_answers += 1
        else:
            print(f"{answer} is not correct. Try again!")

    if timer == 0:
        print("Time is up!")
        print(f"Sorry, you didn’t get that answer in on time.")
        print(f"You answered {correct_answers} problems!")
        input("Press Enter to play again.")

if __name__ == "__main__":
    main()
