import json

with open("bonus15.json", 'r') as file:
    content = file.read()

# print(content) saia uma str

data = json.loads(content)

# "data" é uma lista composta por dicionários igual ao que está no ficheiro .json

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = input("Enter your answer: ")
    question["user_choice"] = int(user_choice)

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{index + 1} {result} " \
              f"- Your answer: {question['user_choice']}." \
              f" Correct Answer: {question['correct_answer']}"
    print(message)
