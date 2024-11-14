import functions

choice=1
try:
    while choice<4 :
        print("Read = 1")
        print("Write = 2")
        print("Clear = 3")
        print("End Program = 4")
        choice=int(input("Selection: "))
        print()
        if choice==1:
            functions.read()
            print()
        elif choice==2:
            functions.write()
            print()
        elif choice==3:
            functions.clear()
            print()
        else: 
            print("Not Valid Selection")



    print("Editing Finished")
except Exception as ourException:
    print()
    print(ourException)
else:
    print("No exceptions occurred")
finally:
    print()
    print("Done")
