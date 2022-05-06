from collections import Counter

def any_palindrome(myString):
    alpha_chars_only = [x for x in myString.lower() if x.isalpha()]
    counts = Counter(alpha_chars_only)
    number_of_odd = sum(1 for letter, cnt in counts.items() if cnt%2)
    return number_of_odd <= 1
    
if __name__ == '__main__':
    s = "intn i"
    print(any_palindrome(s))