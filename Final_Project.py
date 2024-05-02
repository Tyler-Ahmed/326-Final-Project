import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, subject, difficulty):
        self.subject = subject
        self.difficulty = difficulty
        self.questions = []

    def add_question(self, question, answer):
        self.questions.append((question, answer))

    def save_score(self, name, score):
        with open(f"{self.subject}_{self.difficulty}_scores.txt", "a") as file:
            file.write(f"Name: {name}, Score: {score}%\n")
        print("Score saved successfully!")

    def run_quiz(self):
        random.shuffle(self.questions)
        num_questions = len(self.questions)
        correct_answers = 0
        
        print(f"--- {self.subject} {self.difficulty.capitalize()} Quiz ---")
        
        for question, answer in self.questions:
            print(question)
            user_answer = input("Input your answer here: ")
            if user_answer.lower() == answer.lower():
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Wrong! The correct answer is {answer}")

        percentage_score = (correct_answers / num_questions) * 100
        print(f"\nYou got {correct_answers} out of {num_questions} questions correct.")
        print(f"Your percentage score is: {percentage_score:.2f}%")

        name = input("Enter your name: ")
        self.save_score(name, percentage_score)

        if correct_answers < num_questions:
            self.retake_quiz()

    def retake_quiz(self):
        while True:
            print("\nWould you like to retake the quiz?")
            retake_choice = input("Enter 'yes' or 'no': ").lower()
            
            if retake_choice == 'yes':
                self.run_quiz()
                break
            elif retake_choice == 'no':
                print("Thank you for taking the quiz!")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

def sample_quizzes():
    easy_math_quiz = Quiz("Math", "easy")
    easy_math_quiz.add_question("How many degrees does a triangle have?", "180")
    easy_math_quiz.add_question("Square root of 25?", "5")

    hard_math_quiz = Quiz("Math", "hard")
    hard_math_quiz.add_question("What is 2^10?", "1024")
    hard_math_quiz.add_question("What is the area of a circle with radius 5?", "78.5")

    easy_history_quiz = Quiz("History", "easy")
    easy_history_quiz.add_question("What year was the University of Maryland founded?", "1856")

    hard_history_quiz = Quiz("History", "hard")
    hard_history_quiz.add_question("Who was the first president of the United States?", "George Washington")

    easy_science_quiz = Quiz("Science", "easy")
    easy_science_quiz.add_question("What is the name of gold on the periodic table?", "AU")

    hard_science_quiz = Quiz("Science", "hard")
    hard_science_quiz.add_question("What is the chemical symbol for lead?", "Pb")

    return easy_math_quiz, hard_math_quiz, easy_history_quiz, hard_history_quiz, easy_science_quiz, hard_science_quiz

def main():
    print("Welcome to the Quiz App!")
    print("Choose a quiz:")
    print("1. Math (Easy)")
    print("2. Math (Hard)")
    print("3. History (Easy)")
    print("4. History (Hard)")
    print("5. Science (Easy)")
    print("6. Science (Hard)")

    choice = input("Enter your choice (1-6): ")

    quizzes = sample_quizzes()

    if choice == "1":
        quizzes[0].run_quiz()
    elif choice == "2":
        quizzes[1].run_quiz()
    elif choice == "3":
        quizzes[2].run_quiz()
    elif choice == "4":
        quizzes[3].run_quiz()
    elif choice == "5":
        quizzes[4].run_quiz()
    elif choice == "6":
        quizzes[5].run_quiz()
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
