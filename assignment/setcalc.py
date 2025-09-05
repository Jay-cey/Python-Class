print("Welcome to the ultimate set calculator by Jeremy! 🎊😌🎆")
username = input(" Please type in your name >>> ")
list_of_sets =[]

while True:
    status = input("Are you ready to proceed or quit? 'p' or 'q' >>> ").lower().strip()
    if status in ["p", "proceed"]:
        number_of_sets = input("\n How many sets (in decimal) do you want to create for the operation? \n P.S. A minimum of 2 is required>>>").strip()
        while not number_of_sets.isdecimal() or int(number_of_sets) < 2:
            number_of_sets = input("Invalid input. Please enter a valid number (minimum 2) >>> ").strip()
        if number_of_sets.isdecimal():
            for i in range(1, int(number_of_sets)+1):
                print(f"Creating set {i}:")
                set_values = input(f"\n Input the elements of set{i} separated by commas >>> ").strip().removesuffix(",")
                print(f"set values: {set_values}")
                list_of_sets.append(set(set_values.strip().split(",")))
            print(list_of_sets)
            continue_state = True
            while continue_state:
                continue_status = input("\n Do you want to continue to the operation phase? 'y' or 'n' >>> ").lower().strip()
                if continue_status in ["y", "yes"]:
                    print("\n Available operations include: \n 1. Union \n 2. Intersection \n 3. Difference \n 4. Is Disjoint \n 5. Symmetric Difference")
                    while True:
                        operation = input("Choose an operation from the list above (1-5) >>> ").strip()
                        if operation in ["1", "2", "3", "4", "5", "union", "intersection", "difference", "is disjoint", "symmetric difference"]:
                            break
                        else:
                            print("Invalid input. Please choose a valid operation from the list.")
                    
                    print("\nAvailable sets include: ")
                    for i in range(len(list_of_sets)):
                        print(f"Set {i+1}: {list_of_sets[i]}")

                    set1_index = input(f"\nChoose the first set by its number (1-{len(list_of_sets)})>>> ").strip()
                    set2_index = input(f"Choose the second set by its number (1-{len(list_of_sets)})>>> ").strip()
                    if set1_index.isdecimal() and set2_index.isdecimal():
                        set1_index = int(set1_index)-1
                        set2_index = int(set2_index)-1
                        if operation in ["1", "union"]:
                            result = list_of_sets[set1_index].union(list_of_sets[set2_index])
                            print(f"The union of Set {set1_index+1} and Set {set2_index+1} is: {result}")
                        elif operation in ["2", "intersection"]:
                            result = list_of_sets[set1_index].intersection(list_of_sets[set2_index])
                            print(f"The intersection of Set {set1_index+1} and Set {set2_index+1} is: {result}")
                        elif operation in ["3", "difference"]:
                            result = list_of_sets[set1_index].difference(list_of_sets[set2_index])
                            print(f"The difference of Set {set1_index+1} and Set {set2_index+1} is: {result}")
                        elif operation in ["4", "is disjoint"]:
                            result = list_of_sets[set1_index].isdisjoint(list_of_sets[set2_index])
                            print(f"Is Set {set1_index+1} disjoint with Set {set2_index+1}? {result}")
                        elif operation in ["5", "symmetric difference"]:
                            result = list_of_sets[set1_index].symmetric_difference(list_of_sets[set2_index])
                            print(f"The symmetric difference of Set {set1_index+1} and Set {set2_index+1} is: {result}")
                        else:
                            print("Invalid operation choice. Please try again.")
                        continue_status = input("Do you want to continue with the operation phase? 'y' or 'n' >>> ").lower().strip()
                        if continue_status not in ["y", "yes", "n", "no"]:
                            print("Invalid input. Please enter 'y' or 'n'.")
                        elif continue_status in ["y", "yes"]:
                            continue
                        else:
                            continue_state = False
                    else:
                        print("Set indices must be numbers. Please try again.")
                elif continue_status in ["n", "no"]:
                    create_new = input("Do you want to create new sets? 'y' or 'n' >>> ").lower().strip()
                    if create_new in ["y", "yes"]:
                        add_or_replace = input("Do you want to add to the existing sets or replace them? 'a' to add, 'r' to replace >>> ").lower().strip()
                        if add_or_replace in ["a", "add"]:
                            number_of_new_sets = input("How many new sets do you want to add? >>> ").strip()
                            if number_of_new_sets.isdecimal():
                                for i in range(int(number_of_new_sets)):
                                    setnum = len(list_of_sets) + 1
                                    print(f"Creating set {setnum}:")
                                    set_values = input(f"Input the elements of set{setnum} separated by commas ',' >>> ").strip().removesuffix(",")
                                    print(f"set values: {set_values}")
                                    list_of_sets.append(set(set_values.strip().split(",")))
                                print(f"New list of sets: {list_of_sets}")
                                continue
                        elif add_or_replace in ["r", "replace"]:
                            list_of_sets.clear()
                            number_of_new_sets = input("How many new sets do you want to add? >>> ").strip()
                            if number_of_new_sets.isdecimal():
                                for i in range(int(number_of_new_sets)):
                                    setnum = len(list_of_sets) + 1
                                    print(f"Creating set {setnum}:")
                                    set_values = input(f"Input the elements of set{setnum} separated by commas >>> ").strip().removesuffix(",")
                                    print(f"set values: {set_values}")
                                    list_of_sets.append(set(set_values.strip().split(",")))
                                print(f"New list of sets: {list_of_sets}")
                        else:
                            print("Invalid input. Please enter 'a' to add or 'r' to replace.")
                    elif create_new in ["n", "no"]:
                        continue_state = False
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print("Please enter a valid number for the sets.")           
    elif status in ["q", "quit"]:
        print(f"Thank you {username} for using the set calculator. Goodbye! 👋")
        break    
    else:
        print("Invalid input. Please enter 'p' to proceed or 'q' to quit.")           