# 1

As a user 
to check grammar 
i want to confirm if the text starts with a capital letter and ends with a punctuation mark.

As a user 
so that i can check what percentage of total checks passed 
i want a number representing total checks passed as a percentage

# 2

check('Hello world.')
# parameter 
    a string representing a text 
# returns 
    Boolean representing if the check passed or not 

percentage_good()
# no parameter 
# returns 
    percentage of checks passed 

# 3 

check('Hello world.')
=> True

check('Hello world,')
=> False

check('hello world.')
=> False

check('hello world,')
=> False

check('Hello world!')
=> True

check('')
=> 'Error'

check("Hello world!")
percentage_good()
=> 100

check("Hello world,")
percentage_good()
=> 0

check("Hello world!")
check("Hello world,")
percentage_good()
=> 50

check("Hello world!")
check("Hello world,")
check("Hello world.")
percentage_good()