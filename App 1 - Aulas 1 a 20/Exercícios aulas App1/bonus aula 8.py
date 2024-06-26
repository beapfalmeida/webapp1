date = input("Enter today's date: ")
mood = input("How's your mood today from 0 to 10?")
thoughts = input("Let your thoughts flow:\n")

with open(f"venv/{date}.txt", 'w') as file:
    file.write(mood + 2 * '\n')
    file.write(thoughts)
