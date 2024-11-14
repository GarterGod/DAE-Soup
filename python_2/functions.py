def read():
    filetoreadfrom=open("notouch.txt","r")
    line=filetoreadfrom.readline().rstrip("\n")
    while line !="":
        print(line)
        line=filetoreadfrom.readline().rstrip("\n")
def clear():
    filetowriteto=open("notouch.txt", "w")
    filetowriteto.write("")
    print("Cleared")
def write():
    filetowriteto=open("notouch.txt", "a")

    filetowriteto.write(input("input: "))
    filetowriteto.write("\n")
def BallFinder (Net): 
    import random
    global Ball
    Ballmin=0
    Ballmax=0
    while Ballmin==Ballmax:
      
        Roll()
        Ballmin=waw
        Roll()
        Ballmax=waw
    Ball=Net

    while Ball==Net:
        if Ballmin>Ballmax: 
            random_numbers = random.randint(Ballmax,Ballmin) 
            Ball=random_numbers

        elif Ballmax>Ballmin:
            random_numbers = random.randint(Ballmin,Ballmax) 
            Ball=random_numbers   
def Adding(waw,Ball):
  
    Roll()
    if waw<0:
        Ball=Ball+waw
        waw=waw*-1
        print(f"Subtracting {waw}")
        print()
        print(Ball)
        print()
       
    else:
        print(f"Adding {waw}")
        Ball=Ball+waw
        print()
        print(Ball)
        print()
def Roll(Minumum, Maximum):
    global waw
    import random
    random_number=random.randint(Minumum, Maximum) 
    waw = random_number   
def Subtracting(waw,Ball):

    if waw<0:
        Ball=Ball-waw
        waw=waw*-1
        print(f"Adding {waw}")
        print()
        print(Ball)
        print()
        
    else:
        print(f"Subtracting {waw}")
        Ball=Ball-waw
        print()
        print(Ball)
        print()      
def listmkr(amountoflines):
    thislist = [] #makes a blank list
    filetoreadfrom=open("notouch.txt","r") #open notouch.txt in reading mode and turns it into a variable
    line=filetoreadfrom.readline().rstrip("\n") #reads a line of notouch.txt and removes the breaks (dont know if there actualy called breaks)
    for a in range(1,amountoflines): #starts a for loop for a set amount of lines
      b=a-1 #this is so we only sellecet one place in the list at a time
      line=filetoreadfrom.readline().rstrip("\n")#reads a line of notouch.txt and removes the breaks (dont know if there actualy called breaks)
      thislist[b:a] = [line]#adds read line to thislist
    print(thislist)#when it finishes it prints the entirety of this list







