###############################################
#                                             #
#        Michael Theisen                      #
#        06/02/2023                           #
#        TCSS 435, Artificial Intelligence    #
#        Assignment 3                         #
#                                             #
###############################################

# Source code that implements the hash table/linked structure.

import random
import string

class MarkovModel:
    def __init__(self): 
        self.model = {} # dictionary

    # method to read the files and train the model
    def train(self, filenames):
        for filename in filenames:
            with open(filename, 'r') as file:

                # skip the first 8 lines since thats where 
                # the title, author, and chapter is at. It
                # was the quickest solution to indentifying
                # them and trying to account for them and 
                # remove them.
                lines = file.readlines()[8:]  

            # join the lines into a single string doc
            doc = ' '.join(lines)  

            # split into separate sentences based on if we hit a period.
            sentences = doc.split('.')

            # get rid of the spaces
            for sentence in sentences:
                sentence = sentence.strip()

                # remove punctuation
                # https://www.geeksforgeeks.org/python-maketrans-translate-functions/
                # https://docs.python.org/3/library/string.html 
                # https://stackoverflow.com/questions/41535571/how-to-explain-the-str-maketrans-function-in-python-3-6 
                sentence = sentence.translate(str.maketrans('', '', string.punctuation))  
                
                # if sentence:
                #     # change capitals to lowercase in the sentences,
                #     # and split up the words
                #     words = self.splitWords(sentence.lower()) 
                #     # update the model based on the words
                #     self.updateModel(words)

                # is the if even nessesary now that I took 
                # care of the cases for empty strings with
                # the splitWords method??
                # Nope! Works fine. Keep it just in case....

                # change capitals to lowercase in the sentences,
                # and split up the words
                words = self.splitWords(sentence.lower()) 

                # update the model based on the words list
                self.updateModel(words)
    
    # needed to implement another method that deals with 
    # words concatenating when they were originally not 
    # separated with a space. i.e., at the end of a line
    # and then someone just hit "enter" to go to the next
    # line without adding a space.
    def splitWords(self, sentence):
            words = [] # list 
            word = '' 

            # go over literally every char in the sentence
            for char in sentence:

                # if its a letter, add it to the word
                if char.isalpha():
                    word += char
                elif word:

                    # if its not a letter, add it to the list
                    words.append(word)

                    # start over
                    word = '' 
            # return the list of words        
            return words


    # updates the Markov Model with the count of how often the word3 
    # appears given word2 and word1. If its in the nested dictionary
    # of the model already, increments the count. If not, add it such
    # that it can be incremented if we come across it again. 
    def updateModel(self, words):

        # trigram needs 3 words, keep going until we get 3
        if len(words) < 3:
            return

        ###########################################################
        #                                                         #
        #   From the Assignment3.docx:                            #
        #                                                         #
        #      "Example: Consider the following sentence          # 
        #       S = “This is a test sentence from a document”     #
        #       P(test|a, is) = Count(is a test) / Count(is a)    #
        #                     = 1/1 = 1 "                         #
        #                                                         #
        #      "P(W_0), P(W_1|W_0), and P(W_i|W_(i-1),W_(i-2))."  #
        #                                                         #
        #      "hash on word W_(i-2)"                             #
        #                                                         #
        ###########################################################


        # iterate over words up to i-2 then update.
        for i in range(len(words) - 2):
            word1 = words[i]
            word2 = words[i + 1]
            word3 = words[i + 2]

            # if the word1 is in not in the model, 
            # add it to the empty dictionary
            if word1 not in self.model:
                self.model[word1] = {}

            # if the word2 is not in the dictionary 
            # that corresponds to word1 in the model, 
            # add an empty dictionary as the value 
            # for word2 given word1
            if word2 not in self.model[word1]:
                self.model[word1][word2] = {}

            # if the word3 is not in the dictionary that 
            # corresponds to the two preceding words in 
            # the model, initialize word3 to 1.
            if word3 not in self.model[word1][word2]:
                self.model[word1][word2][word3] = 1
            # if however word 3 is indeed present in the 
            # dictionary, increment word3 by 1.
            else:
                self.model[word1][word2][word3] += 1

    # makes a probable story based off of the length
    def probableStory(self, length):

        # a very unprobable story...(empty list)
        story = [] 
        # random selection from outer dictionary
        word1 = random.choice(list(self.model.keys()))
        # random selection from inner dictionary from word1
        word2 = random.choice(list(self.model[word1].keys()))

        # iterate and append over the range of the input length, (2000)
        for _ in range(length):
            story.append(word1)
            word1, word2 = word2, self.getNextWord(word1, word2)

        # adds back in that space between words
        return ' '.join(story)


    # gets the next word base off of the probabilities.
    def getNextWord(self, word1, word2):

        # if word1 and word2 are both presennt in their 
        # respective models, it retrieve the nested dictionary
        if word1 in self.model and word2 in self.model[word1]:
            nextWords = self.model[word1][word2]

            # get the total count of the next words,
            totalCount = sum(nextWords.values())

            # gets the probability of the next words by 
            # dividing their counts by the total count
            probabilities = [count / totalCount for count in nextWords.values()]

            # returns the next word randomly using the probabilities 
            # as weights, and selects the first element from the result. 
            # The higher the count, the more likely its selected.
            return random.choices(list(nextWords.keys()), probabilities)[0]
        else:
            # if however word1 and word2 not present in the model, a
            # random word is chosen from all words in the model. 
            return random.choice(list(self.model.keys()))
