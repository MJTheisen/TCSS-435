###############################################
#                                             #
#        Michael Theisen                      #
#        06/02/2023                           #
#        TCSS 435, Artificial Intelligence    #
#        Assignment 3                         #
#                                             #
###############################################

# A tester file that reads input files, connects to the Markov 
# source code, and generates the output story

from Markov import MarkovModel

# instantiate the model
model = MarkovModel() 

# model.train('stud.txt') # start with just the one.   
# model.train('houn.txt') # test   

# train the model
model.train(['stud.txt', 'houn.txt'])  

# write a probable story
story = model.probableStory(2000) 


# Well, 2000 words wraps automatically while 100 and 50 words just keeps extending...........
# story = model.probableStory(100) # test for 100
# story = model.probableStory(50) # test for 50

# print out the probableStory to a Readme.txt
with open('Readme.txt', 'w') as file:
    file.write(story)

# Note. I was getting wierd input with numbers like "97163" 
# from line 1029 of stud.txt, and just the letter "l" as in,
# lowercase "L". It looks like my code is actually working fine. 
# Some one literally just typed "l" instead of "i" or "I" on 
# line 5441 of houn.txt... Occasionally, I will see "grassgrown" 
# or something like it. This is because of the presence of \
# "grass-grown" being converted into one word, like that of line 
# 3082 in houn.txt. 
