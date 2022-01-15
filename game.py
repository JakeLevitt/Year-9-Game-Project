#List of question for referece

#who are the characters
q1a = ["jabari, his dad, and his sister", "jabari, his cousins and his dad", "jabari, his friends, and his dad"]

#where is the setting
q2a = ["pool", "zoo", "garage"]

#why did Jabari let the other kids go ahead of him when he was in line to get on the diving board
q3a = ["he had good manners", "he was thinking about what jump he wanted to do", "he liked the kids"]

#why did Jabari climb up the ladder and then climb back down
q4a = ["the lifeguard closed the pool" "it began raining", "he told his dad he was a little tired and needed to rest"]

#how did Jabari’s dad help him feel better about jumping off the diving board
q5a = ["he pushed him off the board", "he told him to take a deep breath and tell himself he is ready", "he told him they were going home"]

#how did Jabari feel after he jumped off the diving board
q6a = ["he was excited and happy that he jumped", "he felt mad that his dad made him jump", "he was still scared"]

#what did Jabari tell his dad after he jumped off the diving board
q7a = ["i don’t want to do that again", "i want to go home", "surprise double backflip is next"]

score = 0

#Asking the questions

print ("Welcome to the Jabari Jumps quiz! Make sure to type in exactly one of the possible answers. Make sure that you have no capital letters or periods in your answer. Good luck!")

q1q = input("Q1. Who are the characters? Possible answers are; jabari, his dad, and his sister; jabari, his cousins and his dad; jabari, his friends, and his dad: ")
if q1q == "jabari, his dad, and his sister":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")

q2q = input("Q2. Where is the setting? Possible answers are; pool; zoo; garage: ")
if q2q == "pool":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")

q3q = input("Q3. Why did Jabari let the other kids go ahead of him when he was in line to get on the diving board? Possible answers are; he had good manners; he was thinking about what jump he wanted to do; he liked the kids: ")
if q3q == "he was thinking about what jump he wanted to do":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")

q4q = input("Q4. Why did Jabari climb up the ladder and then climb back down? Possible answers are; the lifeguard closed the pool; it began raining; he told his dad he was a little tired and needed to rest: ")
if q4q == "he told his dad he was a little tired and needed to rest":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")

q5q = input("Q5. How did Jabari’s dad help him feel better about jumping off the diving board? Possible answers are; he pushed him off the board; he told him to take a deep breath and tell himself he is ready; he told him they were going home: ")
if q5q == "he told him to take a deep breath and tell himself he is ready":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")

q6q = input("Q6. How did Jabari feel after he jumped off the diving board? Possible answers are; he was excited and happy that he jumped; he felt mad that his dad made him jump; he was still scared: ")
if q6q == "he was excited and happy that he jumped":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")

q7q = input("Q7. What did Jabari tell his dad after he jumped off the diving board? Possible answers are; i don’t want to do that again; i want to go home; surprise double backflip is next: ")
if q7q == "surprise double backflip is next":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")

#Telling what score you got

if score == 0:
    print("You got 0/7 correct. Try again to receive a higher score!")

if score == 1:
    print("You got 1/7 correct. Try again to receive a higher score!")

if score == 2:
    print("You got 2/7 correct. Try again to receive a higher score!")

if score == 3:
    print("You got 3/7 correct. Try again to receive a higher score!")

if score == 4:
    print("You got 4/7 correct. Good job!")

if score == 5:
    print("You got 5/7 correct. Good job!")

if score == 6:
    print("You got 6/7 correct. Great job!")

if score == 7:
    print("You got 7/7 correct. Perfect!")