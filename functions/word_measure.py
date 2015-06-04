the_word = raw_input("What word would you like to play with? (make sure it has an 'a' in it) ")
print the_word.lower().replace('a','x')
print "The only thing we have to fear is " + the_word + " itself."
word_length = len(the_word)
print the_word + " is " + str(word_length) + " letters long."
