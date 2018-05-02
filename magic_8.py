#Magic 8 ball for fortune-telling or seeking advice.
import random
import time
answers = ['It is certain', 'It is decidedly so',
           'Without a doubt', 'Yes – definitely',
           'You may rely on it', 'As I see it, yes',
           'Most likely', 'Outlook good',
           'Yes Signs point to yes', 'Reply hazy',
           'try again', 'Ask again later',
           'Better not tell you now', 'Cannot predict now',
           'Concentrate and ask again', 'Dont count on it',
           'My reply is no', 'My sources say no',
           'Outlook not so good', 'Very doubtful']

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')
print('')
print("Hello, Humanbeing! I am Magic 8. May I have your name?")
name=input("Please enter your name:")
print('Hello,{}!'.format(name))
def question_answer():
    print("You can ask me a question and I will tell you the answer.")
    input("Enter your question, please:")
    print(answers[random.randint(0,len(answers))])
    print("I hope the answer I tell will help!")
question_answer()

while True:
    print("Do you want to ask another question?(y for yes and n for no)")
    a=input("y/n:")
    if a.lower()=='y':
        question_answer()
    elif a.lower()=='n':
        print("Good luck! Bye!")
        break #this break is used for while
    elif a.lower()!='y' and a.lower()!='n':
        print("Your answer was invalid, please enter y for yes or n for no!")
      
