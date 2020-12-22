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



rules = {'do you think (.*)': ['if {0}? Absolutely.', 'No chance'], 
        'do you remember (.*)': ['Did you think I would forget {0}', "Why haven't you been able to forget {0}", 'What about {0}', 'Yes .. and?'], 
        'I want (.*)': ['What would it mean if you got {0}', 'Why do you want {0}', "What's stopping you from getting {0}"],
        'if (.*)': ["Do you really think it's likely that {0}", 'Do you wish that {0}', 'What do you think about {0}', 'Really--if {0}']}

phrases_replacement ={"you":'I',"your":"my, mine","I am":"you are","you are":"I am"}


bot_template ="Bot:{0}\t"

user_template="{0}:\t"

fallback_questions_answer ={"Do you think":["Why would I think ", "Why should I think " ,"Yes !"]

}
time_frame=[0.5,1.6,2.3,0.8,2,3.1,1]