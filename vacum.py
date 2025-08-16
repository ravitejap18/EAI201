def first(choice):
    if choice == "start":
        print("lets Start !!!!!1")
        while True:
            print("1. Left")
            print("2. Right")
            print("3. Dock")
            h=input("enter you gudence")
            if h== "left":
                print("Turn Left!!!!!!!")
            elif h == "right":
                print("Turn Right!!!!!!!!!!!")
            elif h == "dock":
                print("Dock!!!!!!!!!")
            else:
                print("stoping the process!!!!")
                break 
        else :
            print("try again...")
def sec(entry) :
    if entry == 1:
        print ("Turn on the simple mode :")
    elif entry == 2:
        print ("turn on power mode !!!")
    elif entry == 3 :
        print ("Turn on the ultra power mode!!!!!!!!!")
    else:
        print("Invalid choice.")


print("Enter the type of dust:")
print("1 .Normal")
print("2. Small crystls or rocks")
print("3. Hardr things")
entry= int(input("enter the kind (1/2/3)"))
sec(entry)
print("Options:")
print("1. Start")
choice = input("Enter your choice : ").lower()

first(choice)
