import random
import string

class RandomGenerator:
    def generate_string(self):
        return ''.join(random.choices(string.ascii_uppercase, k=15))
    
    def set_length(self, length):
        if 1 <= length <= 100:
            self.length = length
    
    def generate_multiple_strings(self, count):
        return [self.generate_string() for _ in range(count)] 