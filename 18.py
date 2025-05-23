# Create an empty dictionary
friends_languages = {}

# Get input for 4 friends
for i in range(4):
    name = input("Enter friend's name: ")
    language = input(f"Enter {name}'s favorite language: ")
    friends_languages[name] = language

# Display the dictionary
print(friends_languages)
