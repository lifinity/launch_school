print(int('3.1415'))    # error b/c str -> int requires string to be formatted precisely as an int; this is float formatting
print(int(float('3.1415')))   # for successful conversion