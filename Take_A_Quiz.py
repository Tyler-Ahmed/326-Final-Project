import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def ask_to_go_back_to_menu():
    while True:
        choice = input("Do you want to go back to the main menu? (yes/no): ").lower()
        if choice == 'yes':
            main()
            break
        elif choice == 'no':
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


class Quiz:
    def __init__(self, subject, difficulty):
        self.subject = subject
        self.difficulty = difficulty
        self.questions = []
        self.new_question = None
        self.new_answer = None

    def add_question(self, question, answer):
        self.questions.append((question, answer))

    def save_score(self, name, score):
        with open(f"{self.subject}_{self.difficulty}_scores.txt", "a") as file:
            file.write(f"Name: {name}, Score: {score}%\n")
        print("Score saved successfully!")
        print("If you take the test again you can reenter your score!")

    def add_new_question(self, quiz):
        print(f"Enter the new question for {self.subject} ({self.difficulty}):")
        print("Format: Question? Answer")
        print("Example: What is the capital of France? Paris")
        user_input = input("Enter the new question and answer: ")

        try:
            new_question, new_answer = user_input.split("?")
            new_question = new_question.strip()
            new_answer = new_answer.strip()
        except ValueError:
            print("Invalid input format. Please follow the format: Question? Answer")
            return

        self.new_question = new_question
        self.new_answer = new_answer
        self.add_question(new_question, new_answer)
        print("New question added successfully to the quiz!")
        quiz.add_question(new_question, new_answer)  # Adding the new question to the quiz

        # Prompt the user to go back to the main menu
        ask_to_go_back_to_menu()

    def run_quiz(self, quiz):
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
        
        # Include the newly added question from the quiz object
        if quiz.new_question:
            print(quiz.new_question)
            user_answer = input("Input your answer here: ")
            if user_answer.lower() == quiz.new_answer.lower():
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Wrong! The correct answer is {quiz.new_answer}")
        
        percentage_score = (correct_answers / (num_questions + bool(quiz.new_question))) * 100
        print(f"\nYou got {correct_answers} out of {num_questions + bool(quiz.new_question)} questions correct.")
        print(f"Your percentage score is: {percentage_score:.2f}%")
        
        name = input("Enter your name: ")
        self.save_score(name, percentage_score)
        
        if correct_answers < num_questions:
            self.retake_quiz()

        # Display scores after completing the quiz
        self.display_scores()
        
        ask_to_go_back_to_menu()


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

    def display_scores(self):
        with open(f"{self.subject}_{self.difficulty}_scores.txt", "r") as file:
            scores = [line.strip() for line in file.readlines()]

        print("\n--- Scores ---")
        print("1. Display scores in order they were saved")
        print("2. Display scores from highest to lowest")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            print("\n--- Scores in order they were saved ---")
            for score in scores:
                print(score)
        elif choice == "2":
            valid_scores = [score for score in scores if "Name: " in score and ", Score: " in score]
            if valid_scores:
                sorted_scores = []
                for score in valid_scores:
                    try:
                        score_value = float(score.split(": ")[1][:-1])
                        sorted_scores.append((score, score_value))
                    except ValueError:
                        pass
                sorted_scores.sort(key=lambda x: x[1], reverse=True)
                print("\n--- Scores from highest to lowest ---")
                for score, _ in sorted_scores:
                    print(score)
            else:
                print("No valid scores found.")
        else:
            print("Invalid choice. Please enter either '1' or '2'.")


    def reset_scores(self):
        with open(f"{self.subject}_{self.difficulty}_scores.txt", "w") as file:
            file.write("")
        print("Scores reset successfully!")



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
    print("Choose an option:")
    print("1. Take a Quiz")
    print("2. Display Scores")
    print("3. Reset Scores")
    print("4. Add New Question")

    choice = input("Enter your choice (1-4): ")

    quizzes = sample_quizzes()

    if choice == "1":
        print("Choose a quiz:")
        print("1. Math (Easy)")
        print("2. Math (Hard)")
        print("3. History (Easy)")
        print("4. History (Hard)")
        print("5. Science (Easy)")
        print("6. Science (Hard)")

        quiz_choice = input("Enter the number of the quiz (1-6): ")
        if quiz_choice.isdigit():
            quiz_choice = int(quiz_choice)
            if 1 <= quiz_choice <= 6:
                # Pass the selected quiz to run_quiz()
                quizzes[quiz_choice - 1].run_quiz(quizzes[quiz_choice - 1])
            else:
                print("Invalid quiz number. Please enter a number between 1 and 6.")
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
    elif choice == "2":
        print("Choose the quiz whose scores you want to display:")
        print("1. Math (Easy)")
        print("2. Math (Hard)")
        print("3. History (Easy)")
        print("4. History (Hard)")
        print("5. Science (Easy)")
        print("6. Science (Hard)")

        quiz_choice = input("Enter the number of the quiz (1-6): ")
        if quiz_choice.isdigit():
            quiz_choice = int(quiz_choice)
            if 1 <= quiz_choice <= 6:
                quizzes[quiz_choice - 1].display_scores()
            else:
                print("Invalid quiz number. Please enter a number between 1 and 6.")
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
        ask_to_go_back_to_menu()
    elif choice == "3":
        print("Choose the quiz you want to reset scores for:")
        print("1. Math (Easy)")
        print("2. Math (Hard)")
        print("3. History (Easy)")
        print("4. History (Hard)")
        print("5. Science (Easy)")
        print("6. Science (Hard)")

        quiz_choice = input("Enter the number of the quiz (1-6): ")
        if quiz_choice.isdigit():
            quiz_choice = int(quiz_choice)
            if 1 <= quiz_choice <= 6:
                quizzes[quiz_choice - 1].reset_scores()
            else:
                print("Invalid quiz number. Please enter a number between 1 and 6.")
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
    elif choice == "4":
        quiz_choice = input("Enter the number of the quiz (1-6) to add a new question: ")
        if quiz_choice.isdigit():
            quiz_choice = int(quiz_choice)
            if 1 <= quiz_choice <= 6:
                quizzes[quiz_choice - 1].add_new_question(quizzes[quiz_choice - 1])
            else:
                print("Invalid quiz number. Please enter a number between 1 and 6.")
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

    main()  # Return to the main menu after any operation is completed

if __name__ == "__main__":
    main()
