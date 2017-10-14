''' Write a function that will return the number of digits in an integer. '''

def len_of_int(number):
    ''' returns the number of digits in an integer '''
    return len(str(number))

def remove_first_occurrence(substring, original_string):
    ''' returns string '''
    return original_string.replace(substring, '', 1)

def reverse(text):
    ''' returns '''
    return text[::-1]

def is_palindrome(text):
    ''' Test a string to see if it is a palindrome '''
    return reverse(text.lower().replace(' ','')) == text.replace(' ','')

def mirror(text):
    ''' mirrors the given string '''
    return text + reverse(text)

def encript(original_string, mapping):
    ''' a crummy cypher '''
    temp_string = ''
    for char in original_string.lower():
        temp_string += mapping[ord(char)- 97] if not char == ' ' else ' ' 
    return temp_string

def main():
    ''' main entry point '''
    print("len_of_int(): " + str(len_of_int(7684)))
    print(remove_first_occurrence("an", "banana"))
    print(reverse("Jason"))
    print(is_palindrome("I am a cat"))
    print(is_palindrome("race car"))
    print(mirror("Jason"))
    print(encript("jason was here", "bcdefghijklmnopqrstuvwxyza"))
if __name__ == "__main__":
    main()
