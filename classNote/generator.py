# Multiplication generator
status = True

while status:
    start = input("\nInput table start. P.S. Input must be an integer >>> ").strip()
    end = input("Input table end. P.S. Input must be an integer >>> ").strip()
    continue_choice = ""
    if start.isdigit() and end.isdigit():
        start = int(start)
        end = int(end)
        if end >= start:
            for i in range(start, end+1):
                print(f"\n Multiplication Table {i}")
                for j in range(1, 10+1):
                    print(f"{i} * {j} = {i*j}")
        else:
            print(f"End must be greater than the Start. Please try again \n")
    else:
        print(f"Start and End must be positive whole numbers. Please try again \n")
    while status:
        continue_choice = input("Do you want to continue? (yes/no) >>> ").lower().strip()
        if continue_choice == "yes":
            break
        elif continue_choice == "no":
            print("Goodbye! 👋🏽🙋🏽‍♂️")
            status = False
            break
        else:
            print("Invalid choice! Please enter 'yes' or 'no'.")
            continue





#Palindrome checker with list and string/slicing 