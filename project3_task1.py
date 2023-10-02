def most_frequent(string):
    # Remove spaces and convert to lowercase for case-insensitive counting
    cleaned_string = string.replace(" ", "").lower()
    
    # Create an empty dictionary to store letter frequencies
    letter_count = {}
    
    # Iterate through the string to count letter frequencies
    for letter in cleaned_string:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    
    # Sort the dictionary by values in descending order
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    
    
    for letter, frequency in sorted_letters:
        print(f"{letter} = {frequency:02d}", end=" ")

string = input("Please enter a string: ")
most_frequent(string)