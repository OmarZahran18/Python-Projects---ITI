def counter_vowels(text):
    v = "aeiouAEIOU"
    counter = 0
    for i in text:
        if i in v:
            counter += 1
    print("Vowel count:", counter)
    
    
def location_of_i(text):
    for i in range(len(text)):
        if text[i] == 'i':
            print("Index of 'i':", i)
