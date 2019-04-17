text_file = open('generator.txt', 'r')
print(text_file.read())

list = [word for word in text_file.read()]
text_file.close()

import random
def generate_animals(size):
    my_list = []
