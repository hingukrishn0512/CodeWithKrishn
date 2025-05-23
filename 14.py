words = {
    "kursi": "chair",
    "gadha": "donkey",
    "sarmila": "introvert"
}

word = input("Please enter a Hindi word: ").strip().lower()

# Check if word exists in dictionary
if word in words:
    print(f"The English meaning of '{word}' is '{words[word]}'.")
else:
    print("Sorry, that word is not in the dictionary.")
