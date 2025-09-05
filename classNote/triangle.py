#Right Angled Triangle
print("""
        WELCOME TO THE ULTIMATE RIGHT ANGLED TRIANGLE GENERATOR!!!!!! 🤯🤯🔥🎊🎊
    """)
state = True
while state:
    triangle_type = input('''Please choose from the following types the type of triangle to generate. \n\t 1. Upright Right angled triangle. \n\t 2. Upside down right angled triangle \n\t 3. Flipped upright right angled triangle. \n\t 4. Flipped upside down right angled triangle \n >>> ''').strip()
    if triangle_type.isdecimal() == True:
        choice = int(triangle_type)
        if choice == 1:
            height = int(input(" Enter desired triangle height >>> "))
            for i in range(height, height+1):
                print(f"\nRight Angled Triangle. Height = {i}")
                for j in range(1, i+1):
                    count = "*" * j
                    print(f"{count}")

        elif choice == 2:
            height = int(input(" Enter desired triangle height >>> "))
            for i in range(height, height+1):
                print(f"\nUpside down right angled triangle. Height = {i}")
                for j in range(i, 0, -1):
                    count = "*" * j
                    print(f"{count}")

        elif choice == 3:
            height = int(input(" Enter desired triangle height >>> "))
            for i in range(height, height+1):
                print(f"\nFlipped upright right angled triangle. Height = {i}")
                print(f"{' ' * height}/|")
                for j in range(1, i+1):
                    count = "*" * j
                    diff = i - j
                    space = " " * diff
                    print(f"{space}/{count}|")
                under = height+2
                print("¯" * under)

        elif choice == 4:
            height = int(input(" Enter desired triangle height >>> "))
            for i in range(height, height+1):
                print(f"\nFlipped upside down right angled triangle. Height = {i}")
                under = height+2
                print("_" * under)
                for j in range(i, 0, -1):
                    count = "*" * j
                    diff = i - j
                    space = " " * diff
                    print(f"{space}\\{count}|") 
                print(f"{space} \\|") 
                
        else: 
            print("invalid triangle type choice. Please choose from either '1', '2', '3' or '4' \n")
    else: 
        print("invalid triangle type choice. Please choose from either '1', '2', '3' or '4' \n")

    while state:
        continue_choice = input("Do you want to continue? (yes/no) >>> ").lower().strip()
        if continue_choice == "yes":
            break
        elif continue_choice == "no":
            print("Goodbye! See ya next time 👋🏽🙋🏽‍♂️")
            state = False
            break
        elif continue_choice not in ['yes', 'no']:
            print("Invalid choice! Please enter 'yes' or 'no'.")
            continue