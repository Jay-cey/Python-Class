# status = True

print("\t Welcome to the Palindrome Checker!!! 🥂🥳")
# while status:
#     text = input(" Please type in the word you what to check if it a Palindrome \n\t>>>").strip().lower()
#     reversed_text = text[::-1]
#     if text == reversed_text :
#         print(f"The word '{text.capitalize()}' is a palindrome ✅😌🍾")
#     else:
#         print(f"The word '{text.capitalize()}' is not a palindrome ❌😔")
#     while status:
#         continue_choice = input("Do you want to continue with another word? (yes/no) >>> ").lower().strip()
#         if continue_choice == "yes":
#             break
#         elif continue_choice == "no":
#             print("Goodbye! 👋🏽🙋🏽‍♂️")
#             status = False
#             break
#         elif continue_choice not in ['yes', 'no']:
#             print("Invalid choice! Please enter 'yes' or 'no'.")
#             continue

status = True

while status:
    text = input(" Please type in the word you what to check if it is a Palindrome \n\t>>>").strip().lower()
    text_list = []
    for i in text:
        text_list.append(i)
    text_list.reverse()
    reversed_text = "".join(text_list)
    print(reversed_text)

    if text == reversed_text:
        print(f"The word '{text.capitalize()}' is a palindrome ✅😌🍾")
    else:
        print(f"The word '{text.capitalize()}' is not a palindrome ❌😔")
    while status:
        continue_choice = input("Do you want to continue with another word? (yes/no) >>> ").lower().strip()
        if continue_choice == "yes":
            break
        elif continue_choice == "no":
            print("Goodbye! 👋🏽🙋🏽‍♂️")
            status = False
            break
        elif continue_choice not in ['yes', 'no']:
            print("Invalid choice! Please enter 'yes' or 'no'.")
            continue