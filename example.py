#Given a word as input, output a list, containing only the letters of the word that are not vowels.
#The vowels are a, e, i, o, u.
#Sample Input = awesome, so Sample Output would be ['w', 's', 'm'].

word = input()
result = [letter for letter in word if letter.lower() not in 'aeiou']
print(result)