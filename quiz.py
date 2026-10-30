import random

questions = [{"question":"Which language is commonly used for programming?","options":["A. Python","B. HTML","C. CSS","D. SQL"],"answer":"A"},
               {"question":"Which data type stores True or False values in Python?","options":["A. String","B. Boolean","C. List","D. Integer"],"answer":"B"},
               {"question":"Which symbol is used for comments in Python?","options":["A. //","B. &","C. #","D. **"],"answer":"C"},
               {"question":"Which keyword is used to define a function in Python?","options":["A. function","B. define","C. fun","D. def"],"answer":"D"},
               {"question":"Which collection stores items in key-value pairs?","options":["A. List","B. Tuple","C. Dictionary","D. Set"],"answer":"C"}]

def run_quiz():
    score = 0
    
    quiz_questions = questions.copy()
        
    random.shuffle(questions)

    print("\n=================================================================================================================================================================================")
    print("                PYTHON QUIZ")
    print( "==================================================================================================================================================================================")

    for number, question_data in enumerate(questions, start=1):
        print(f"\nQuestion {number}:{question_data['question']}")
        
        for option in question_data["options"]:
            print(option)
            
        user_answer = input("Enter your answer (A, B, C or D): ").strip().upper()
        
        while user_answer not in ["A", "B", "C", "D"]:
            print("Invalid choice. Please enter A, B, C, or D.")
            user_answer = input("Your answer: ").strip().upper() 
        if user_answer == question_data["answer"]:
            print("Correct! Well done Mzee!!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question_data['answer']}.")
            
    percentage = (score / len(questions)) * 100

    print("\n======================================================================================================================================================================================")
    print("                       QUIZ RESULTS")
    print("===================================================================================================================================================================================")

    print(f"Your score: {score}/ {len(questions)}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("Excellent! You got every question right!")
    elif percentage >= 60:
        print("Good job! Keep practising.")
    else:
        print("Keep learning. You will improve with practice!")
    print("=========================================================================================================================================================================")

if __name__ == "__main__":
    run_quiz()