#
#
# Take the text of a book and return a dictionary containing a word histogram
# Sort the histogram and display the top 5 results
#
#

import re

# Putting word number first as if this is not entered by the user no need to calculate the histogram
numberOfWords = ''
attempt = 0
while numberOfWords == '':
    if attempt == 3: quit()
    attempt = attempt + 1
    try:
        numberOfWords = input('How many words would you like to see? ')
        numberOfWords = int(numberOfWords)
    except:
        print('Please input a whole number')
        numberOfWords = ''


eggsHandle = open('./assets/004_GreenEggsAndHam.txt', 'r')
words = {}

for word in re.split('[^0-9a-zA-Z]+|[\n]+', eggsHandle.read().title()):
    words[word] = words.get(word, 0) + 1

result = list(map(
    lambda o: { 'word': o, 'count': words[o] },
    words.keys()
))
result.sort(key=lambda x: x.get('count'))
result.reverse()

for i in range(min([numberOfWords, len(result)])):
    print(str(i+1)+': "', result[i]['word'], '" occured', result[i]['count'], 'times')