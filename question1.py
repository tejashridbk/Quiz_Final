import json
import pprint
with open('example.json','r') as file:
     data = file.read()
   
     example_dict = json.loads(data)
   
     
def quiz():
    score = 0
    subject = input("enter quiz subject you want:")
   
    for sub_key in example_dict['quiz']:
              if subject == sub_key:
                  for q_key in example_dict['quiz'][sub_key]:
                     pprint.pprint(example_dict['quiz'][sub_key][q_key]['question'])
                     pprint.pprint(example_dict['quiz'][sub_key][q_key]['options'])
                     answer = input("enter answer")
                     if answer == example_dict['quiz'][sub_key][q_key]['answer']:
                            print("correct")
                            score=score+1
                            print("your score is :" + str(score))
             
            
  
               

def run_test():
    print("\n\nwhich type of quiz you want to solve?\n")
    pprint.pprint("\nsport\nmaths\nsportmatch")
    quiz()
    
    
     
run_test()		             
	             
		
			
		
		
		            
	

# this selects question from sport topic one by one
		
