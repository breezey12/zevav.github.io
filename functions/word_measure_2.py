def transform_and_measure_a_word(a_word):
    print a_word.lower().replace('a','x')
    print "The only thing we have to fear is " + a_word + " itself."
    word_length = len(a_word)
    print a_word + " is " + str(word_length) + " letters long."

user_word = raw_input("What word would you like to transform? ")
transform_and_measure_a_word(user_word)
another_word = "Lake Champlaign"
transform_and_measure_a_word(another_word)
     
