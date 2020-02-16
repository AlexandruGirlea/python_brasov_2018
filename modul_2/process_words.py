negative_words = ['rau', 'negativ', 'jos', 'negru']
positive_words = ['bun', 'pozitiv', 'sus', 'alb']


def word_type(word):
    if word in negative_words:
        print('Ati introdus un cuvant negativ')
    elif word in positive_words:
        print('Ati introdus un cuvant pozitiv')
    else:
        print('Cuvantul nu a putut fi clasificat')

