import random

class MathMentorPro:
    def __init__(self):
        self.difficulty = None
        self.score = 0

    def set_difficulty(self):
        while True:
            print("Select difficulty level:")
            print("1. Easy (Addition and Subtraction within 10)")
            print("2. Medium (Addition, Subtraction, and Multiplication within 100)")
            print("3. Hard (All operations within 1000)")
            choice = input("Enter your choice (1, 2, or 3): ")
            if choice in ['1', '2', '3']:
                self.difficulty = int(choice)
                break
            else:
                print("Invalid choice. Please try again.")

    def generate_problem(self):
        if self.difficulty == 1:
            return self.generate_easy_problem()
        elif self.difficulty == 2:
            return self.generate_medium_problem()
        elif self.difficulty == 3:
            return self.generate_hard_problem()

    def generate_easy_problem(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-'])
        if operation == '+':
            correct_answer = num1 + num2
        else:
            correct_answer = num1 - num2
        return f"{num1} {operation} {num2}", correct_answer

    def generate_medium_problem(self):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(['+', '-', '*'])
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
        return f"{num1} {operation} {num2}", correct_answer

    def generate_hard_problem(self):
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        operation = random.choice(['+', '-', '*', '/'])
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        elif operation == '*':
            correct_answer = num1 * num2
        else:
            correct_answer = num1 / num2
        return f"{num1} {operation} {num2}", correct_answer

    def start(self):
        self.set_difficulty()
        while True:
            problem, correct_answer = self.generate_problem()
            print(f"Solve the following problem: {problem}")
            user_answer = input("Your answer: ")
            try:
                user_answer = float(user_answer)
                if abs(user_answer - correct_answer) < 0.001:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Incorrect. The correct answer was {correct_answer}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            
            print(f"Your current score: {self.score}")
            continue_playing = input("Do you want to solve another problem? (yes/no): ").lower()
            if continue_playing != 'yes':
                print(f"Thank you for playing! Your final score: {self.score}")
                break

if __name__ == "__main__":
    mentor = MathMentorPro()
    mentor.start()
