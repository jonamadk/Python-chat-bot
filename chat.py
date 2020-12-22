from dictionary import responses, name, weather, bot_template, user_template
from dictionary import time_frame, fallback_questions_answer, rules, phrases_replacement
import time
import random
import re


class Chatbot():
    def __init__(self,conversation_length):
        self.input_msg=""
        self.user_name=""
        self.conversation_length = conversation_length
  
       
       
    def take_input(self):

        self.user_name=input("Enter your name \t")


    def respond(self):
        self.take_input()


        for self.conversation_length in responses:
            
            time.sleep(random.choice(time_frame))
            self.input_msg=input(user_template.format(self.user_name)).lower()

            if self.input_msg not in responses:
                response = None
                for pattern , response in rules.items():
                    match = re.search(pattern.lower(), self.input_msg) 
                    if match is not None:
                        response = random.choice(response)
                        if '{0}' in response:
                            phrase = match.group(1)
                            for sub_key, sub_value in phrases_replacement.items():
                                if sub_key in phrase:
                                    replaced_phrase = re.sub(sub_key, sub_value, phrase)
                                    time.sleep(random.choice(time_frame))
                                    result = response.format(replaced_phrase)
                                    print(result)
                                    
        
            elif self.input_msg in responses:    
                response_text = random.choice(responses[self.input_msg])
                time.sleep(random.choice(time_frame))
                result = bot_template.format(response_text)
                print(result)
                
            else:
                result = random.choice(responses["default_fallback"])
                print(result)
                
        

bot = Chatbot(len(responses))
bot.respond()
   





