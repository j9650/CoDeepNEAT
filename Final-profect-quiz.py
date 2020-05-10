#find a random 10 numbers from 1 to 15
import random
number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
random.shuffle(number_list)
number_list=number_list[0:10]
#open file and get data in it
file=open("Capital.txt","r")
all_line=file.readlines()
file.close
#ask and answer questions
for i in range (10):
   #pick a random question and answer
    the_question=(all_line[number_list[i]])
   #Seprate questions and answers 
    the_question=the_question.strip().split(",")
   #ask question and recieve input from user
    answer=input(the_question[0])
   #reponse to the user
    
    if answer.lower()==the_question[1].lower():
        print("Correct!")
    else:
        print(answer.lower())
        print(the_question[1].lower())
        print("Incorrect! The answer is",the_question[1])
       

