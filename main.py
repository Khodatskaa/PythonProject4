text = input("Enter your text: ")

reserved_words = input("Enter the list of reserved words (by comma): ").split(',')

words = text.split()

for i in range(len(words)):
    word = words[i]
    if word.lower() in map(str.strip, reserved_words):
        words[i] = word.upper()
    if not word.isalpha():
        print(f"Error: '{word}' contains non-alphabetic characters and is not a reserved word.")
        break

modified_text = ' '.join(words)
print("Modified text:")
print(modified_text)
