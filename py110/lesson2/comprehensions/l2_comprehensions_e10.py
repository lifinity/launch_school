# write a function that takes no arguments & returns a string containing
# a universal unique identifier (uuid) which is defined as 32 hexadecimal
# characters (0-9 & a-f) broken into 5 sections in an 8-4-4-4-12 pattern
# e.g. f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91

import random

def generate_uuid():
    HEXADECIMALS = '0123456789abcdef'
    SECTIONS = [8, 4, 4, 4, 12]
    # uuid = [''.join([random.choice(HEXADECIMALS) for _ in range(section_len)]) \
    #                                              for section_len in SECTIONS]
    uuid = [''.join(random.choices(HEXADECIMALS, k=section_len)) for section_len in SECTIONS]
    return '-'.join(uuid)

print(generate_uuid())