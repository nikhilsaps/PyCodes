# Level 2
# Question£o Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence
# capitalized. Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be:
# HELLO WORLD PRACTICE MAKES PERFECT
data =input("enter the string to be capitalized")

print(data.upper())


# Solution: ```python
# lines = []
# while True: s = input()
# if s: lines.append(s.upper())
# else: break;
# for sentence in lines:
#     print(sentence) ```