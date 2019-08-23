import json
import pprint
with open('quiz.json','r') as file:
     data = file.read()
   
     example_dict = json.loads(data)
   
     
def sport_quiz():
    score = 0
    for q_key in example_dict['quiz']['sport']:

            pprint.pprint(example_dict['quiz']['sport'][q_key]['question'])
            pprint.pprint(example_dict['quiz']['sport'][q_key]['options'])
            answer = input("enter answer")
            if answer == example_dict['quiz']['sport'][q_key]['answer']:
                     print("correct")
                     score=score+1
            
            print("your score is :" + str(score))	
           
               
def maths_quiz():
    score = 0
    for i in example_dict['quiz']['maths']:
            pprint.pprint(example_dict['quiz']['maths'][i]['question'])
            pprint.pprint(example_dict['quiz']['maths'][i]['options'])
            answer = input("enter answer")
            if answer == example_dict['quiz']['maths'][i]['answer']:
                score+=1
                print("correct")
            print("your score is :" + str(score))
def run_test():
    print("\n\nwhich type of quiz you want to solve?\n" + "sport\n" + "maths\n")
    choice = input("enter choice:")
    if choice == "sport":
        sport_quiz()
    else:
        maths_quiz()
     
run_test()	
