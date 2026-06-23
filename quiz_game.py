score = 0

print("Python Quiz")

answer = input("1. What is the capital of India? ")

if answer.lower() == "new delhi":
    score += 1

answer = input("2. Which language are we using? ")

if answer.lower() == "python":
    score += 1

answer = input("3. What is 5 + 5? ")

if answer == "10":
    score += 1

print("Your Score =", score, "/ 3")