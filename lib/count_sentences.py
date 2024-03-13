#!/usr/bin/env python3

class MyString:
    def __init__(self, value='') -> None:
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print('The value must be a string.')

    def is_sentence(self):
        return self.value.endswith('.')
   
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        """ Count number of sentences in self.value

        I'm working off the observation that sentences are delimited
        by a punctuation mark (. / ! / ?) followed by a space. After
        splitting the initial value on a single white-space character
        any list items that end with the punctuation above should 
        mark the ends of sentences.
        """
        count = 0
        init_value = self.value
        for item in init_value.split(' '):
            if item.endswith('.') or item.endswith('!') or item.endswith('?'):
                count += 1
        return count