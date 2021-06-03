import random
language = ["English", "Hindi", "Sanskrit", "French", "German", "Spanish", "Japenese"]
subject = ["Physics", "Chemistry", "Biology", "Mathematics", "History", "Civics", "Geography"]
print("I will choose the Language or Subject you will read")
first = input("Would you like to read a Language or a Subject?")
if first == "Language":
    choice = random.choice(language)
    print("Read the Language: " + choice)
elif first == "Subject":
    choice = random.choice(subject)
    print("Read the Subject: " + choice)
else:
    print("Sorry, please choose a valid option")