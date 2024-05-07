import requests as req
import json
import random
import html

# API URL to fetch trivia questions
url = "https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=multiple"

# Initialize variables
check_end_game = ""
score = 0
number_correct_answers = 0

# Game instructions
print("Welcome to the Quiz Game!")
print("Correct answer earns 2 points.")
print("Wrong answer deducts 1 point.")
print("************************************")

# Main game loop
while check_end_game != "yes":
    print()
    
    # Fetch a question from the trivia API
    response = req.get(url)
    
    # Check if API request was successful
    if response.status_code != 200:
        check_end_game = input("Sorry, there is a problem with the API. Press 'yes' to continue: ")
        print("************************************")
    else:
        # Parse the JSON response
        data = json.loads(response.text)
        question = html.unescape(data['results'][0]['question'])
        incorrect_answers = data['results'][0]['incorrect_answers']
        correct_answer = html.unescape(data['results'][0]['correct_answer'])
        
        # Combine correct and incorrect answers and shuffle them
        answers = incorrect_answers + [correct_answer]
        random.shuffle(answers)
        
        # Display the question and shuffled answers
        print(question)
        for idx, answer in enumerate(answers, start=1):
            print(f"{idx}- {answer}")
        
        # Prompt user for answer and check correctness
        user_choice = int(input("Enter the number of the correct answer: "))
        if correct_answer == answers[user_choice - 1]:
            print("Correct!")
            score += 2
            number_correct_answers += 1
        else:
            print(f"Sorry, the correct answer is: {correct_answer}")
            if score != 0:
                score -= 1
        
        # Ask user if they want to end the game
        check_end_game = input("Do you want to end the game? (yes/no): ").lower()
        print("************************************\n")

# Game summary
print(f"You have answered {number_correct_answers} questions correctly.")
print(f"Your final score is: {score}\n")
print("************************************")
print("Thank you for playing the Quiz Game!")