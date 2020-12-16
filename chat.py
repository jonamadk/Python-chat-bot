name="chill bot"
weather="cloudy"


responses={
    "hi": ["hello, bud !", "Yo !", "Hey dude","Wassup !"],
    "k chha":["thik thak","fine bhanam","cool"],
    "k xa":["thik thak","fine bhanam","cool"],
    "la thik xa":["same to you", "huss tw ni"],
    "k gardai": ["nachdai","kei nai"],
    "k gardai xau":["nachdai","kei nai"],
    "shit":["you are shi**","buddy chill"],
    "maam khayeu":["xaina ! khuwaideu na","nay nay","ummmmmmm"],
    "haha":["kastari haseko marxu ki kya ho","hehe","hasdeko maya","aich aich"],
    "nice":["nice nice","yup"],
    "lol":["sahi ho sahi ho","k ka lol ho"],
    "damn":["i know i am cool","hell yeah","dayumn"],
    "fuck you":["bad guy spotted","fuck you too man", "someone is pissed !"],
    "fuck":["you","slang spotted", "nice word selection"],
    "hey":["hello, bud !","Yo !", "Hey dude","Wassup !"],
    "your name":["Imma Fucked Up bot",  "Same as your crush name !", "Imma chill bot"],
    "who made you":[  "Sandu Subedi , she gave me birth","Self Made", "God" ],
    "chill":["Imma always chillin' ", "chill pill"],
    "take care":["Fuck you !","see you later aligator !"],
    "bye":["see ya ","tata maya" ,"tata"],
     "tata":["Bi Bi ","bye" ],
     "byee":["see ya ","tata","bye" ],
     "byeee":["bye ","la gako ma pani" , "tata"] ,
     "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
   "name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default_fallback": ["Sorry ! I'm still learning !","Can you ask me soemthing else?","Opps 404 ! resource not found","something next"]
  
} 



fallback_questions_answer ={"Do you think":["Why would I think ", "Why should I think " ,"Yes !"]

}
time_frame=[0.5,1.6,2.3,0.8,2,3.1,1]

import time
import random
import re

bot_template ="Bot:{0}\t"


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
            
            self.input_msg=input("{0}:".format(self.user_name)).lower()

            try:
                pattern="Do you think (.*)"
                match=re.search(pattern.lower(), self.input_msg).group(1)
                if 'you are' or 'you are' in match:
                    swaped_text = re.sub('you are','I am',match)
                    print(random.choice(fallback_questions_answer["Do you think"])+ swaped_text)
            
                
            except AttributeError:
                if self.input_msg in responses: 
                    
                    response_text = random.choice(responses[self.input_msg])
                    time.sleep(random.choice(time_frame))
                    print(bot_template.format(response_text))
                else:
                    print(random.choice(responses["default_fallback"]))
                
        

bot = Chatbot(len(responses))
bot.respond()
   





