text = input("Enter a sentence: ")

words = len(text.split())
characters = len(text.replace(" ", ""))
reversed_text = text[::-1]

print("Words: ", words)
print("Characters (no spaces): ",  characters)
print("Reversed:", reversed_text)