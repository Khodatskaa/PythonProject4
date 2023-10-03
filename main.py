text = input("Enter your text: ")

sentences = text.split('.')


sentences = list(filter(None, sentences))

sentence_count = len(sentences)

print(f"There are {sentence_count} sentences in text")