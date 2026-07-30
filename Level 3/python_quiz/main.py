import os
import json
import random
FOLDER = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_PATH = os.path.join(FOLDER, "questions.json")
HIGHSCORE_PATH = os.path.join(FOLDER, "highscore.json")
def load_questions():
    with open(QUESTIONS_PATH,"r",encoding="utf-8") as file:
        return json.load(file)
def load_highscore():
    if os.path.exists(HIGHSCORE_PATH):
        with open(HIGHSCORE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)["best"]
    return 0
def save_highscore(score):
    with open(HIGHSCORE_PATH, "w",encoding="utf-8") as file:
        json.dump({"best":score},file)
def display_title(total):
    print("\n========================")
    print("      PYTHON QUIZ")
    print("========================")
    print(f"{total} questions loaded. Good luck!")
def get_answer(options):
    for index,option in enumerate(options,start=1):
        print(f"  {index} > {option}")
    while True:
        try:
            choice = int(input("Your answer: "))
            if 1<=choice<=len(options):
                return options[choice-1]
            print(f"Please choose a number between 1 and {len(options)}.")
        except ValueError:
            print("Please enter a valid number.")
def quiz(questions):
    score = 0
    total = len(questions)
    for number,item in enumerate(questions,start=1):
        print(f"\nQuestion {number}/{total}")
        print(item["question"])
        options = item["options"][:]
        random.shuffle(options)
        chosen = get_answer(options)
        if chosen==item["answer"]:
            score+=1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was: {item['answer']}")
 
    return score
def results(score,total,previous_best):
    percentage = (score/total)*100
    print("\n========================")
    print("       RESULTS")
    print("========================")
    print(f"Score: {score}/{total} ({percentage:.0f}%)")
    if percentage==100:
        print("Perfect score!")
    elif percentage>=70:
        print("Great job!")
    elif percentage>=50:
        print("Not bad!")
    else:
        print("You are so stupid! ")
    if score>previous_best:
        print(f"New high score! (previous best: {previous_best})")
        save_highscore(score)
    else:
        print(f"High score to beat: {previous_best}")
    print("========================")
def main():
    questions = load_questions()
    random.shuffle(questions)
    previous_best = load_highscore()
    display_title(len(questions))
    score = quiz(questions)
    results(score,len(questions),previous_best)
if __name__ == "__main__":
    main()