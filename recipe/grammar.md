```python
# 1

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

# 2
def grammar(text)
# parameters 
    # text in human readable form
# returns 
    # returns True if grammar is correct else false

# 3

if grammar starts with capital and end with full stop 
it should return True 

grammar('Hello, welcome home.')
# => True 

if grammar starts with capital and end with question mark 
it should return True 

grammar('Hello, welcome home?')
# => True 

if grammar starts with capital and end with ! 
it should return True 

grammar('Hello, welcome home!')
# => True 

if grammar starts with capital and end with coma
it should return False 

grammar('Hello, welcome home,')
# => False

if grammar does not start with capital and ends with full stop
it should return False 

grammar('hello, welcome home.')
# => False

if string is empty
it should return error

grammar('')
# => Error




