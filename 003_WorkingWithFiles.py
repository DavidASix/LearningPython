
# myFile = open(filename, mode)
# Mode is r, w
# open returns a file handle. The handle is an object that allows you to interact with your file.

greatestSongsHandle = open('./assets/003_Top500GreatestSongs.txt', 'r')
# print(greatestSongsHandle.read())
lc = 0
artists = []
artistsOccurences = dict()
for line in greatestSongsHandle:
    # Ignore comments
    if line.startswith('#'): continue
    lc = lc + 1
    # Check for lines with multiple dashes
    #dashes = 0
    #for c in line: dashes = c == '-' and dashes + 1 or dashes
    #if dashes > 1: print(line.rstrip())
    # Parse out artist names and append to array
    artistName = line[line.rfind(' - ') + 3 : len(line.rstrip())]
    artists.append(artistName)
    # Add artist to occurences dictionary, or increment their value by one
    artistsOccurences[artistName] = artistsOccurences.get(artistName, 0) + 1

print('Number of songs', lc)

# Remap the artistsOccurences object to a sortable array
artistRemap = []
for artist in artistsOccurences.keys():
    artistRemap.append({
        'name': artist,
        'occurences': artistsOccurences[artist]
    })

print('Number of artists on top 500 songs: ', len(artistRemap))

artistRemap.sort(key=lambda x: x.get('occurences'))
artistRemap.reverse()
# print(artistRemap)
print()
print('Top 5 Bands:')

for artist in artistRemap[0:5]:
    print(artist['name'], artist['occurences'], 'occurences')