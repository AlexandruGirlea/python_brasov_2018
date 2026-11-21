negative_words = ['bad', 'negative', 'down', 'black']
positive_words = ['good', 'positive', 'up', 'white']


def word_type(word):
    if word in negative_words:
        print('You entered a negative word')
    elif word in positive_words:
        print('You entered a positive word')
    else:
        print('The word could not be classified')
