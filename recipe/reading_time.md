```python
# 1 
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

# 2 
def reading_time(text):
    # parameters:
       # a string represneting text
    # return:
        # a flloat for reading time

# 3
given a 200 word text 
it will return 1.0

reading_time(...200...)
# => 1.0

given a 400 word text 
it will return 2.0

reading_time(...400...)
# => 2.0

given a 500 word text 
it will return 2.5

reading_time(...500...)
# => 2.5

given a empty text w 
it will raise an error

reading_time(...0...)
# => Error



