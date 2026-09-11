name = input("What's your name? ")
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) My Favorite Book")
    print("4) Exit")
    choice = input("Pick 1-4: ")
    if choice == "1":
        print("Hi! I am Harshitha Nandakumar. I have an immense passion for all things math and physics which has really inspired me to pursue engineering.")
    elif choice == "2":
        print("I aim to become and entrepreneur in the Electrical Engineering field.")
    elif choice == "3":
        print("My favorite book series is the Inheritance Games")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, or 3.")