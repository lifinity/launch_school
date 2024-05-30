# a function that returns the sum of two numbers 
'''
START

GET first number from user; SET as variable first_number
GET second number from user; SET as variable second_number

(alternatively, given both numbers as arguments passed into the function)

RETURN first_number + second_number, i.e the sum

END
'''

# a function that takes a list of strings, and returns a string that is all those strings concatenated together
'''
START

given a list of strings called: strlist

(use the built-in str.join method to return concatenated str separated by '' b/c delimiter unspecified)

SET iterator = 0
SET result = '' to hold return value

WHILE iterator < length of strlist
    SET current_str = value in strlist at index of iterator
    result += current_str, to concatenate string to result
    iterator += 1, increment to progress loop

RETURN result, all of strlists elements concatenated into one str

END
'''

# a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. For instance: every_other([1,4,7,2,5]) => [1,7,5]
'''
START

given a list of integers, called: intlist

(use list comprehension to filter based on odd index)

SET iterator = 0
SET result = [], empty list to hold elements for the new list we want to return

WHILE iterator < length of intlist
    SET current_int = value in intlist at index of iterator
    IF iterator % 2 == 0
        (0-based indexing means alternating even to odd idx, start at first (0), so even idx == 'every other element')
        result += current_int, to add current integer to new list   
    iterator += 1, increment to progress loop

RETURN result, new list containing every other element from original list
    
END
'''

# a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None. 
'''
START

given a string: str, & given a character: chr

SET iterator = 0
SET occurrence_count = 0

WHILE iterator < length of str
    SET current_chr = character of str at index iterator
    IF current_chr = chr
        occurrence_count += 1, update how many times we've seen the given character
        IF occurence_count == 3
            RETURN iterator, i.e. index of 3rd occurrence of chr
    iterator += 1, increment to progress loop

RETURN None, if we didn't return inside while loop, implies occurrence_count never got to 3

END
'''

# a function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes. For instance: merge([1, 2, 3], [4, 5, 6]) => [1, 4, 2, 5, 3, 6]
'''
START

given two number lists: nums1, nums2

SET iterator = 0
SET result = [], empty list to hold elements for new merged list

WHILE iterator < length of the longer one btwn nums1 & nums2
    SET current_num1 = element of nums1 at index iterator OR None (if past end of nums1)
    SET current_num2 = selement of nums2 at index iterator OR None (if past end of nums2)

    (0-based indexing, even -> odd alternate, so if you start w/ appending num1 element followed by num2)
    (num1 elements will always be at even indexes & num2 always at odd UNLESS non-matching lists lengths)

    IF current_num1 != None
        result += current_num1
    
    IF current_num2 != None
        result += current_num2
    iterator += 1, increment to progress loop

(assumed behavior for non-matching length lists: add all elements of longer list at end)
(alternate behavior: stop loop when you hit the end of the shorter list & exclude extra elements from longer)
        
RETURN result

END
'''