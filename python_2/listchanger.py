thislist = [] #makes a blank list
filetoreadfrom=open("notouch.txt","r") #open notouch.txt in reading mode and turns it into a variable
line=filetoreadfrom.readline().rstrip("\n") #reads a line of notouch.txt and removes the breaks (dont know if there actualy called breaks)
for a in range(1,amountoflines): #starts a for loop for a set amount of lines
    b=a-1 #this is so we only sellecet one place in the list at a time
    line=filetoreadfrom.readline().rstrip("\n")#reads a line of notouch.txt and removes the breaks (dont know if there actualy called breaks)
    thislist[b:a] = [line]#adds read line to thislist
  print(thislist)#when it finishes it prints the entirety of this list
#use this with file chager for full effect

