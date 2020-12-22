from dictionary import responses, name, weather, bot_template, user_template
from dictionary import time_frame, fallback_questions_answer, rules
import time
import random
import re


class Chatbot():
    def __init__(self,key):
        self.input_msg=""
        self.user_name=""
        self.key_len =key

       
       
    def take_input(self):

        self.user_name=input("Enter your name \t")


    def respond(self):
        self.take_input()
 

        for self.key_len in responses:
       
            time.sleep(random.choice(time_frame))
            
            self.input_msg=input(user_template.format(self.user_name)).lower()

            if self.input_msg not in responses:
                response = None
                for pattern , response in rules.items():
                    match = re.search(pattern.lower(), self.input_msg) 

                    if match is not None:
                        response = random.choice(response)

                        if '{0}' in response:
                            self.phrase = match.group(1)
                            ans=random.choice(rules[pattern])
                            time.sleep(random.choice(time_frame))
                            print(ans + self.phrase) 
      
            elif self.input_msg in responses:    
                response_text = random.choice(responses[self.input_msg])
                time.sleep(random.choice(time_frame))
                print(bot_template.format(response_text))
            else:
                print(random.choice(responses["default_fallback"]))
                

bot = Chatbot(len(responses))
bot.respond()
   





