# Created by Nicholas Dominici at Very Good Softworks

# Imports delays
def wait_minute():
    import time
    time.sleep(60)

def wait_thirty():
    import time
    time.sleep(30)

def wait_five():
    import time
    time.sleep(5)

def wait_two():
    import time
    time.sleep(2)

# Imports press a key functionality on windows
import msvcrt as m
def wait():
    m.getch()
    
print(" Mini Game by Nicholas Dominici")

def menu():  # Game Menu
    start0 = input("Type 'start' to begin the game>>")

    # Checks if the player entered start or not.
    if start0 == "start":
        import scene0.py
    
    elif start0 == "Start":
        import scene0.py

    else:
        print("Type start please!")
        print
        menu()
menu()