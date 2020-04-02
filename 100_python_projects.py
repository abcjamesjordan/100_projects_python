#!/usr/bin/env python3

# imports
# reminder to add required imputs to requirements.txt file_name
import numpy as np
import matplotlib as plt # need to add to requirements.txt

# Global Variables
mydata = [1, 2, 3, 4, 5, 6, 7, 8]
mydata2 = [1, 8, 2, 3, 4, 5, 6]
#A = np.array([1,2,3],[4,5,6])
#print(A)

"""Other Functions"""
# https://www.youtube.com/watch?v=cdCeU8DJvPM
def find_missing(input_1, input_2):
    sum1 = sum(input_1)
    sum2 = sum(input_2)
    return sum1 - sum2

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
def find_numbers(low, high):
    x = [];
    for i in range(low, high):
        if i % 7 == 0 and i % 5 != 0:
            x.append(i)
    return x

"""MIT Python"""
# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2019/course/
def longest_alphabetical_string(input_string):
    winner = ''
    s = input_string
    for i in range(len(s)):
        if i == len(s)-1:
            break
        letter1 = s[i]
        letter2 = s[i+1]
        string_tracker = letter1
        n = 1
        while letter1 <= letter2:
            n += 1
            string_tracker += letter2
            if i+n == len(s):
                break
            letter1 = letter2
            letter2 = s[i+n]
        if len(winner) < len(string_tracker):
            winner = string_tracker
    return winner

def guess_number_game(low, high):
    print("Please think of a number between " + str(low) + " and " + str(high) + ": ")
    while True:
        guess = (high + low)//2
        print("Is your number " + str(guess) + "?")
        a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        if a == 'c':
            print("Game over. Your secret number is: " + str(guess))
            break
        elif a == 'h':
            high = guess
        elif a == 'l':
            low = guess
        else:
            print("Sorry, I did not understand your input.")

"""Check.io Functions"""
def all_the_same(input_data):
    return input_data[1:] == input_data[:-1]


"""100 Programming Problems Functions"""
"""Text Examples"""
def reverse_some_data(input_data):
    return input_data[::-1] # reverses order of a string, one of many ways

def pig_latin(input_word):
    word = input_word.lower() # lower case input word
    if word[0] in 'aeiou':    # checks for vowel scenario
        pig_word = word[2:] + '-' + word[0] + 'ay'  # returns original word with first two characters put at end + 'ay'
        return pig_word
    else:                     # else assume constant rule
        pig_word = word[1:] + '-' + word[0] + 'ay'  # returns original word with first character put at end + 'ay'
        return pig_word

def count_vowels(input_word):
    word = input_word.lower()
    countera = 0
    countere = 0
    counteri = 0
    countero = 0
    counteru = 0
    for i, c in enumerate(word): # see stackoverflow for explanation @ https://stackoverflow.com/questions/538346/iterating-each-character-in-a-string-using-python
        if c in 'a':
            countera+=1
        if c in 'e':
            countere+=1
        if c in 'i':
            counteri+=1
        if c in 'o':
            countero+=1
        if c in 'u':
            counteru+=1
        else:
            pass
    return countera, countere, counteri, countero, counteru

def check_if_palindrome(input_word):
    return input_word == reverse_some_data(input_word)

def count_words_in_string(input_string):
    # 'This is my input string'
    # Goal is to count number of spaces and add 1???
    counter = 0
    for i, c in enumerate(input_string):
        if c == ' ':
            counter+=1
        else:
            pass
    counter+=1
    return counter

def count_words_in_txt_file(file_name):
    counter = 0
    myfile = open(file_name, "r")
    mytext = myfile.read()
    for i, c in enumerate(mytext):
        if c == ' ':
            counter+=1
    return counter

def fibonacci_sequence(input):
    if input == 0:
        return 0
    if input == 1 or input == 2:
        return 1
    i1 = 0
    i2 = 1
    while input > 1:
        fib_tracker = i1 + i2
        i2temp = i2
        i2 += i1
        i1 = i2temp
        input -= 1
    return fib_tracker


def main():
#    print("The Missing Number is: " + str(find_missing(mydata, mydata2)))
#    print("The Longest String is: " + str(longest_alphabetical_string("azcbobobegghakl")))
#    print("All the same returns: " + str(all_the_same(mydata)))
#    print("Your data reversed it: " + str(reverse_some_data(mydata)))
#    print("Pig Latin is: " + str(pig_latin("alphabet")))
#    print("The number of vowels is " + str(count_vowels("alphabet")))
#    print("Palidrome check returns: " + str(check_if_palindrome('abba')))
#    print("The number of words is: " + str(count_words_in_string("this is my string")))
#    print("The number of words in the file is: " + str(count_words_in_txt_file("string_of_words.txt")))
#    print("The Fibbonacci Sequence of 10 is: " + str(fibonacci_sequence(10)))
#    guess_number_game(0, 100)
    print(find_numbers(2000, 3200))

if __name__ == '__main__':
    main()
