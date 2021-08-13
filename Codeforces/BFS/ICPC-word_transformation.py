'''
Question: A common word puzzle found in many newspapers and magazines is the word transformation. 
By taking a starting word and successively altering a single letter to make a new word, one can 
build a sequence of words which changes the original word to a given end word. For instance, 
the word “spice” can be transformed in four steps to the word “stock” according to the following 
sequence: spice, slice, slick, stick, stock. Each successive word diﬀers from the previous word 
in only a single character position while the word length remains the same.

Given a dictionary of words from which to make transformations, plus a list of starting and ending 
words, your team is to write a program to determine the number of steps in the shortest possible 
transformation.

Input Format:
The first line of the input is an integer N, indicating the number of test set that your correct 
program should test followed by a blank line.

Each test set will have two sections. The frst section will be the dictionary of available words 
with one word per line, terminated by a line containing an asterisk (*) rather than a word. There 
can be up to 200 words in the dictionary; all words will be alphabetic and in lower case, and no 
word will be longer than ten characters. Words can appear in the dictionary in any order.

Following the dictionary are pairs of words, one pair per line, with the words in the pair separated 
by a single space. These pairs represent the starting and ending words in a transformation. All pairs 
are guaranteed to have a transformation using the dictionary given. The starting and ending words will 
appear in the dictionary.

Two consecutive input set will separated by a blank line.

Output Format:
The output should contain one line per word pair for each test set, and must include the starting word, 
the ending word, and the number of steps in the shortest possible transformation, separated by single 
spaces.

Two consecutive output set will be separated by a blank line.
'''
import string
from queue import Queue

def BFS(s, f):
    q = Queue()
    q.put(s)
    n = len(s)

    cost = [-1] * (len(dictionary) + 5)
    cost[dictionary.index(s)] = 0

    while not q.empty():
        st = q.get()
        cur_cost = cost[dictionary.index(st)]
        if st == f:
            return cur_cost
        for i in range(n):
            for c in string.ascii_lowercase:
                if c != st[i]:
                    temp = st[0:i] + c + st[i+1:n]
                    if temp in dictionary and cost[dictionary.index(temp)] == -1:
                        idx = dictionary.index(temp)
                        cost[idx] = cur_cost + 1
                        q.put(temp)

t = int(input())
input()
for _ in range(t):
    dictionary = []

    while True:
        st = input()
        if st == "*":
            break
        dictionary.append(st)

    while True:
        try:
            query = list(input(). split())
        except EOFError:
            break
        if not query:
            break
        print(query[0], query[1], BFS(query[0], query[1]))

    print()

'''
Example input:
------------------------
1

dip
lip
mad
map
maple
may
pad
pip
pod
pop
sap
sip
slice
slick
spice
stick
stock
*
spice stock
may pod
------------------------
Output:
------------------------
spice stock 4
may pod 3
------------------------