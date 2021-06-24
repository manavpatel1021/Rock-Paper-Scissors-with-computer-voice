import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


l1 = ["stone", "paper", "scissor"]

print("please enter any one of this three ->",l1)

user_choice = input("enetr your choice = ")

comp_choice = random.choice(l1)

speak("your choise is ",user_choice)
speak("computrt choice is ",comp_choice)

print("computer choice = ", comp_choice)

if user_choice in l1:

    if user_choice==comp_choice:
        print("draw this round")
        speak("draw")

    elif user_choice == "stone" and comp_choice == "paper" or user_choice == "paper" and comp_choice == "scissor" or user_choice == "scissor" and comp_choice == "stone":
        print("user lose this round")
        speak('computer won')
    else: #user_choice == "stone" and comp_choice == "scissor" or user_choice == "scissor" and comp_choice == "paper" or user_choice == "paper" and comp_choice == "stone":
        print(" user won this round")
        speak('user won')

else:
    print("invalid input")
    speak('try again')