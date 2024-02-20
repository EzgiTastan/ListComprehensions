#List Comprehensions

#Creating a list containing the squares of numbers:
squares = [x**2 for x in range(1, 6)]
# squares: [1, 4, 9, 16, 25]

#Creating a list containing only even numbers:
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
# even_numbers: [2, 4, 6, 8, 10]

#Converting the letters of a string to uppercase:
original_string = "hello world"
uppercase_string = [char.upper() for char in original_string]
# uppercase_string: ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

#Creating a list of the first ten positive integers:
positive_integers = [x for x in range(1, 11)]
# positive_integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Generating a list of the lengths of words in a sentence:
sentence = "List comprehensions are concise and powerful"
word_lengths = [len(word) for word in sentence.split()]
# word_lengths: [12, 13, 3, 6, 2, 8]