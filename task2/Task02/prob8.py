# Generate a random password of 8 characters,
# including a mix of uppercase letters, lowercase letters,
# and numbers.

import random
import string
chars = string.ascii_letters + string.digits
password = ''.join(random.choice(chars) for x in range(8))
print("Random password:", password)
