import eel
import json
import random
import os

eel.init('web')

@eel.expose
def get_random_question_from_chapter(chapter):
    filename = f'chapter {str(chapter).zfill(2)}.json'  # Format filename with leading zeros
    filepath = os.path.join('Json', filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        questions = json.load(file)
    return random.choice(questions)  # Return a random question from the chapter

if __name__ == "__main__":
    eel.start('main.html')
