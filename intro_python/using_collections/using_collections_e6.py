print('abc-def'.isalpha())        # False '-'
print('abc_def'.isalpha())        # False '_'
print('abc def'.isalpha())        # False ' '
print('abc def'.isalpha() and     # False (short-circuit)
      'abc def'.isspace())
print('abc def'.isalpha() or      # False (neither true)
      'abc def'.isspace())
print('abcdef'.isalpha())         # True
print('31415'.isdigit())          # True
print('-31415'.isdigit())         # False '-'
print('31_415'.isdigit())         # False '_'
print('3.1415'.isdigit())         # False '.'
print(''.isspace())               # False