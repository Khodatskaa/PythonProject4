line = input("Enter line: ")

input_string = line.replace(" ", "").lower()

reversed_string = input_string[::-1]

if input_string == reversed_string:
    print("Entered line is palindrome")
else:
    print("Entered line is not palindrome")