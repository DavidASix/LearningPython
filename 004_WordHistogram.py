#
#
# Take the text of a book and return a dictionary containing a word histogram
# Sort the histogram and display the top 5 results
#
#

import re

eggsHandle = open('./assets/004_GreenEggsAndHam.txt', 'r')
words = {}

for word in re.split('[^0-9a-zA-Z]+|[\n]+', eggsHandle.read().title()):
    words[word] = words.get(word, 0) + 1

result = list(map(lambda o: { 'word': o, 'count': words[o] }, words.keys()))
result.sort(key=lambda x: x.get('count'))
result.reverse()

print(result)
