# Question: Write a program to compute the frequency of the words from the input. The output should output after sorting the key
# alphanumerically. Suppose the following input is supplied to the program: New to Python or choosing between Python 2 and Python 3?
# Read Python 2 or Python 3. Then, the output should be: 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1

frequency={

}

data = [x for x in input("enter the whole string").split(" ")]
data.sort()
for words  in data:
    frequency[words]=data.count(words)
print(frequency)

# Solution:
# freq = {} # frequency of words in text
# line = input()
# for word in line.split():
# freq[word] = freq.get(word,0)+1
#  words = freq.keys()
# words.sort()
#  for w in words:
# print("%s:%d" % (w,freq[w]))