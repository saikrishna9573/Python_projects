import random
import time
from datetime import datetime

# Constants for the game
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


# Function to generate a math problem
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer


# Main game function
def math_quiz() -> object:
    wrong = 0
    input("Press Enter to start!")
    print("----------------------")

    start_time = time.time()

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            guess = input(f"Problem #{i + 1}: {expr} = ")
            if guess == str(answer):
                break
            wrong += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Format the elapsed time in HH:MM:SS
    elapsed_struct = time.gmtime(elapsed_time)
    formatted_time = time.strftime("%H:%M:%S", elapsed_struct)

    # Get the current date and time
    current_datetime = datetime.now().strftime("%A, %d %B %Y, %H:%M:%S")

    print("----------------------")
    print(f"Nice work! You finished in {formatted_time}!")
    print(f"Completed on: {current_datetime}")
    if wrong > 0:
        print(f"You had {wrong} wrong {'answer' if wrong == 1 else 'answers'}.")
    else:
        print("You had no wrong answers. Great job!")


# Run the game
if __name__ == "__main__":
    math_quiz()
