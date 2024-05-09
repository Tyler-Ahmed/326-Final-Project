# 326-Final-Project
Documentation


Project Overview: What It Does?

Our project is a program that helps users study and test their knowledge on various subjects. The user runs the program and chooses the subject that they are learning, as well as how difficult they want their quiz to be. Once the quiz starts, the user will answer the prompted questions (our program lets them know whether they were right or wrong). When they are done they are presented with their final score and asked if they would like to retake it or take a quiz on another subject. 


Running the Program: Command Line Instructions

Enter into the command line: python3 Take_A_Quiz.py

To run test script input: pytest -s Final_Testing.py



Program Usage and Output Guide

After entering the main screen you will have 4 options. The following options are to take a test, display scores, reset scores, and add a question. After choosing an option you will be taken to another prompt screen where you will continue with the option. After selecting a test you will be given the option to choose which test you would like to take. After answering a series of questions you will be given a score and the option to save your name. It will then display the scores in a way that you would like. You then have the option to retake the test if not given a 100% or going back to the main menu. If you choose no for both options then the program will end. 


Annotated Bibliography

https://www.w3schools.com/python/ref_string_isdigit.asp
	
Used to learn about the isdigit() method. This method returns True if all the    characters are digits, otherwise False. We used this method in our main function to verify if the number of the quiz is a digit. If not, it will return an error message. 

https://www.w3schools.com/python/ref_random_shuffle.asp

Used to learn about the shuffle() method from Random. This method actually takes a sequence, like a list, and reorganizes the order of the items. However, it changes the original list but it doesn’t create a new one. We used this method in our Quiz class to randomize the questions.

https://docs.pytest.org/en/latest/how-to/monkeypatch.html
	
‘monkeypatch.setattr()’ is being used to replace the built-in input() function with a mock implementation. This is an attribute provided by pytest. The purpose of using monkeypatch.setattr() here is to control the input provided to the run_quiz() function during testing. By replacing the input() function with a mock implementation, the test can simulate various user inputs ("correct", "wrong", "yes") without requiring actual user interaction.
