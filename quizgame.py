import random

print("welcome to quiz game,This game is for basic question for c programming language :")
score = 0
answer = 0
s1=print("1) why is it called 'C' & not 'D'?")
print("1: C stands for code\t [2]The inventor's name started with c\n[3]it developed after a language called 'B'\t[4]why should I care?")
answer=int(input())
if answer == 1:
    print("Thats the correct answer")
    score= score+1
    print("Your Score is now :" ,score)
else:
    print("Wrong answer")
    score=score-1
    print("Your Score is now :" ,score)
s2=print("2) It was developed at?")
print("[1] IBM [2] SAIFULLAH HACKING ZONE [3] Bell Labs[4]Microsoft(?)")
answer=int(input())
if answer == 3:
    print("Thats the correct answer")
    score= score+1
    print("Your Score is now :" ,score)
else:
    print("Wrong answer")
    score=score-1
    print("Your Score is now :" ,score)
s3=print("3) Which name is correct ?")
print("[1] Saifullah [2] Tanim [3] Farabi [4] saifullah al mahmud ")
answer=int(input())
if answer == 4:
    print("Thats the correct answer")
    score= score+1
    print("Your Score is now :" ,score)
else:
    print("Wrong answer")
    score=score-1
    print("Your Score is now :" ,score)

s4=print("4) Which library functions help users to dynamically allocate memory ?")
print("[1]A - memalloc()and alloc() [2] malloc() and memalloc() [3]malloc() and calloc() [4]all ")
answer=int(input())
if answer == 3:
    print("Thats the correct answer")
    score= score+1
    print("Your Score is now :" ,score)
else:
    print("Wrong answer")
    score=score-1
    print("Your Score is now :" ,score)
s5=print("5) Which of the following cannot be a variable name in C?")
print("[1]volatile [2]true [3]Friend [4]export")
answer=int(input())
if answer == 1:
    print("Thats the correct answer")
    score= score+1
    print("Your Score is now :" ,score)
else:
    print("Wrong answer")
    score=score-1
    print("Your Score is now :" ,score)
s6=print("6)  The C library function rewind() reposition the file pointer at the beginning of the file")
print("[1] True [2] False ")
answer=int(input())
if answer == 1:
    print("Thats the correct answer")
    score= score+1
    print("Your Score is now :" ,score)
else:
    print("Wrong answer")
    score=score-1
    print("Your Score is now :" ,score)



s7=print("7) C99 standard guarantees uniqueness of ____ characters for internal names!")
print("[1] 31 [2] 63 [3] 12 [4] 14 ")
answer=int(input())
if answer == 2:
    print("Thats the correct answer")
    score= score+1
    print("Your Score is now :" ,score)
else:
    print("Wrong answer")
    score=score-1
    print("Your Score is now :" ,score)
s8=print("8) C99 standard guarantees uniqueness of _____ characters for external names.!")
print("[1] 31 [2] 6 [3] 60 [4]82")
answer=int(input())
if answer == 1:
    print("Thats the correct answer")
    score= score+1
    print("Your Score is now :" ,score)
else:
    print("Wrong answer")
    score=score-1
    print("Your Score is now :" ,score)

s9=print("9) All keywords in C are in ____________")
print("[1] LowerCase letters [2] UpperCase letters [3] CamelCase letters [4] None of the mentioned")
answer=int(input())
if answer == 1:
    print("Thats the correct answer")
    score= score+1
    print("Your Score is now :" ,score)
else:
    print("Wrong answer")
    score=score-1
    print("Your Score is now :" ,score)
s10=print("10) Which is valid C expression?\n")
print("[1] int my_num = 100,000; [2] int my_num = 100000; [3] int my num = 1000; [4] int $my_num = 10000;")
answer=int(input())
if answer == 2:
    print("Thats the correct answer")
    score= score+1
    print("Your Score is now :" ,score)
else:
    print("Wrong answer")
    score=score-1
    print("Your Score is now :" ,score)

s11=print("Special One: Whats your Favourite programming language?")
print("1.C ; 2.Java ; 3.Python; 4.C# ")
answer=int(input())
if answer == 1 == 2 == 3 == 4:
    print(answer)
    score = score+5

print("Your Total points    :"  ,score)

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
s.extend(list(s5))
s.extend(list(s6))
s.extend(list(s7))
s.extend(list(s8))
s.extend(list(s9))
s.extend(list(s10))
s.extend(list(s11))

random.shuffle(s)

print("Thanks for taking the quiz Competition")