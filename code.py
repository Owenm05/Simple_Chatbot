import random
count=0
member = ["uncle","sister","brother","aunt","cousin","friend"]
greetings = ["Hello!", "Welcome!", "welcome to the chat room","hey!!"]
goodbyes = ["Bye!", "Goodbye!", "Nice meeting you","Thanks for coming"]
keywords = [["cat","cats","dog","dogs","pet","pets"],["brother","sister","mother","father","family"],["gaming","coding","ai","sports","reading","hobbies"]]
responses =[["what is your pet's name?\n","what sort of pet do you have?\n","how old is your pet?\n"],["who are you closest to in your family?\n","how many people are in your direct family?\n","what do you enjoy doing with your family?\n"],["tell me about your hobbies\n","what hobbies do you have?\n","what specificaly do you enjoy doing?\n"]]
pets = {
    "name": None,
    "age": None,
    "animal":None
    }
family = {
    "amount":None
    }
hobbies = {
    "hobbies": [None]
    }
 
print(random.choice(greetings))
user = ""
def main():
    for i in range(len(keywords)):
        for j in range(len(keywords[i])):
            if keywords[i][j] in user:
                if i==0:
                    pcon()
                elif i==1:
                    fcon()
                elif i==2:
                    hcon()
                

def pcon():
    pets["name"]=input(responses[0][0])
    pets["animal"]=input(responses[0][1])
    pets["age"]=input(responses[0][2])
    run()
def fcon():
    family["amount"]=input(responses[1][1])
    run()
def hcon():
    global count
    temp=input(responses[2][random.randint(0,(len(responses[2])-1))])
    if hobbies["hobbies"][0] == None:
        hobbies["hobbies"].remove(None)
    if temp[-3:] == "ing":
        hobbies["hobbies"].append(temp[:-3])
    else:
        hobbies["hobbies"].append(temp)
    print("funny i had a " + random.choice(member) + " who liked to " +hobbies["hobbies"][count])
    count+=1
    run()
def info():
    if pets["name"]!=None:
        print("\t PET\n" + "Name: " + pets["name"]  + "\n" + "Age: " + pets["age"] + "\n" + "Species: " +pets["animal"] + "\n")
    if family["amount"]!=None:
        print("\t FAMILY\n" + "Amount: " + family["amount"]  + "\n")
    if hobbies["hobbies"] != None:
        print("\tHOBBIES\n" +"Hobbies: ")
        print(*hobbies["hobbies"], sep=",")
    run()
    
    
        
def run():
    global user
    user = ""
    user = input("What would you like to talk about?(type bye to leave or info to see info)\n")
    user = user.lower()
    if user!="bye" and user!="info":
        main()
    if user == "info":
        info()
    if user=="bye":
        print(random.choice(greetings))
        quit()
while True:        
    run()
