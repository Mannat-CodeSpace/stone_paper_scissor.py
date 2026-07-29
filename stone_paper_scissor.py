import random


num = [1, 2, 3]

print("/"*75)
window1 = "<-- Get Ready For Fun -->"
window2 = "The Stone-Paper-Scissor Game!!!"
print(window1.center(90))
print()
print(window2.center(90))
print("~"*75)
print()
print("[*]","Rules To Play-->")
print("{1} '1' refers to STONE")
print("{2} '2' refers to PAPER")
print("{3} '3' refers to SCISSOR")
print()
print("Now lets start the game!!!")
print()
while True:
    print("[*] STONE=1 | PAPER=2 | SCISSOR=3 | Exit = 0")
    print()
    choice = int(input("Enter your choice:"))
    choice2 = int(random.choice(num))
    print("*"*25)
    user = print(f"[$] Users choice:{choice}")
    print("[$] Computer's choice:",choice2)
    if choice == choice2:
        print()
        print("Result: Match TIE!!!")
        print("*"*25)
        print()
    elif (choice ==1 and choice2 ==2):
        print()
        print("Result: Computer win!!")
        print("*"*25)
        print()
    elif (choice ==2 and choice2 ==3): 
        print()
        print("Result: Computer win!!")
        print("*"*25)
        print()
    elif (choice ==3 and choice2 ==1): 
        print()
        print("Result: Computer win!!")
        print("*"*25)
        print()
    elif choice>3:
        print()
        print("INVALID CHOICE!!")
        print("*"*25)
        print()
    elif choice == 0:
        print()
        print("[*] Thanks for playing [*]")
        print()
        break
    else:
        print()
        print("Result: User win!!")
        print("*"*25)
        print()

    