import eel
import json
import random
import os

eel.init('web')

@eel.expose
def get_random_question_from_chapter(chapter, type):
    chapter = int(chapter)
    if chapter < 10:
        filename = f'chapter 0{chapter}.json'  # Add a space for chapters less than 10
    else:
        filename = f'chapter{chapter}.json'  # No space for chapter numbers 10 and above
    
    if type == "MultiSelect":
        filepath = os.path.join('Json', 'MultiSelect', filename)
    else:
        filepath = os.path.join('Json', 'TrueOrFalse', filename)
    
    with open(filepath, 'r', encoding='utf-8') as file:
        questions = json.load(file)
    
    return random.choice(questions)  # Return a random question from the chapter

if __name__ == "__main__":
    eel.start('main.html')
