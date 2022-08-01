# Learning Python

I'm looking to expand my skillset by learning Python. My end goal is to able to seamlessly integrate with an existing Machine Learning codebase. I'm working on this new skill by working through the Python for Everybody and Scientific Computing with Python courses on [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/)
Additionally, I would like to automate some of my repetitive daily and weekly tasks, and feel Python may be a good way to do this.

This is a **Sandbox Repository** mostly for scratch notes and testing through my learning journey. I will be storing genuine python projects & scripts in separate repo's once they are complete.

### Notes

* dir(object) to see the methods avaialble on the object.
* in can be used as a declaration for a for loop, or as a operator similiar to in SQL.
* String counting begins at 0 (for find, etc)
* Slicing a string or an array can be done by calling it's indexes. For instance
```python
myString = 'This is a String'
print(myString[0:4]) # Outputs 'This'
```
* In python 2, non latin characters were type unicode, in Python 3 they are type str
* range(x) returns an array containing values 0 through x. This is useful for for loops where you need to know your index. For instance:
``` python
artists = ['Bob Dylan', 'The Rolling Stones', 'John Lennon', 'Marvin Gaye', 'Aretha Franklin']
for i in range(len(artists)):
  print(artists[i])
```
* Plus operator and concatenate arrays