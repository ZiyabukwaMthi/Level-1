
# Ask the user for input
str_manip = input("Enter a sentence: ")

# Calculate and display the length of str_manip
print("Length of a sentence is: ", len(str_manip))

# Find the last letter and replace every occurrence with '@'

last_letter = str_manip[-1]
print(last_letter)

replaced_sent = str_manip.replace(last_letter, "@")
print("After replacing last letter with '@':", replaced_sent)

# Print the last 3 characters in reverse
print("Last 3 characters in reverse:", str_manip[-3:][::-1])

# Create a five-letter word (first 3 + last 2 characters)
five_letter_word = str_manip[:3] + str_manip[-2:]
print("Five-letter word:", five_letter_word)