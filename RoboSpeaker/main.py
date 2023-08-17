import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1, created by Manav Gambhir")
    while True:
        os.system("say 'Welcome to RoboSpeaker program, Please enter what u want me to say'")
        x = input("Enter what you want me to speak: ")
        if(x=="stop"):
            os.system("say 'Its a good bye from RoboSpeaker'")
            break
        speak= f"say {x}"
        os.system(speak)