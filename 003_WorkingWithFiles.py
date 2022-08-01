
# myFile = open(filename, mode)
# Mode is r, w
# open returns a file handle. The handle is an object that allows you to interact with your file.

inputFHandle = open('./assets/003input.txt', 'r')
print(inputFHandle.read())
