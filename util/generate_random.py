import random
import string

class generate_random:

    # def __init__(self, randomlength=16):

    def generate_random_unique(randomlength=7):
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
        random_str = ''.join(str_list)
        return random_str




