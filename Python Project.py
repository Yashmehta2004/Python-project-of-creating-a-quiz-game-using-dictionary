Q1 = """Q1: What of the following is not a keyword?
a. eval
b. assert
c. nonlocal
d. pass"""
Q2 = """Q2: Python is a which level language?
a. High
b. Low
c. Medium
d. Moderate"""
Q3 = """Q3: What is the output of 2*8**2?
a. 18
b. 64
c. 128
d. 256"""
Q4 = """"Q4: a"+"bc"=?
a. a
b. bc
c. bca
d. abc"""
Q5 = """Q5: What is the maximum length of Python identifier?
a. 32
b. 16
c. 64
d. No fixed length"""
Questions = {Q1:"a",Q2:"a",Q3:"c",Q4:"d",Q5:"d"}
name=input("Enter Your Name")
print("Hello",name,"Welcome to the Quiz Game")
score=0
for i in Questions:
    print(i)
    ans = input("Ans: enter the answer (a/b/c/d):")
    if ans==Questions[i]:
        print("=>""Congratulation,correct answer,you got 1 point")
        score=score+1
    else:
        print("Sorry,wrong answer,you lost 1 point")
        score=score-0
print("Your Final Score is:",score)
