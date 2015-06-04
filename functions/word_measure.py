word_list = [] # make sure there's a list to append to
# assign this word to a variable
word_from_user = raw_input("Enter a word for me to measure. ")
# assign the length of the word to another variable
word_length = len(word_from_user)
# append the word to the end of a list
word_list.append(word_from_user)
# and tell me the word's length in plain language
print word_from_user + " is " + str(word_length) + " letters long."
print word_list
