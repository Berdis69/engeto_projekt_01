"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Pavel Berounský
email: berounsky.pavel@gmail.com
"""
# texty k analýze
TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

spacer = ("=" * 50)
text_count = len(TEXTS)
registered_users = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123",
    }



# ověření uživatele a hesla
user_name = input("Insert your name: ").lower()
password = input("Insert your password: ")
print(spacer)
if user_name not in registered_users or password != registered_users[user_name]:
    print("Your username or password are wrong, program will be terminated")
    exit()
else:
    print(f"Welcome to the app, {user_name.capitalize()},\nWe have {text_count} texts to be analyzed")
print(spacer)

# výběr textu k analýze
user_input = input(f"Enter a number btw. 1 and {text_count} to select: ")

if not user_input.isdigit():
    print("Wrong choice, program will be terminated")
    exit()

text_nr = int(user_input)

if text_nr < 1 or text_nr > text_count:
    print("Wrong number, program will be terminated")
    exit()

print(spacer)
print("This text will be analyzed")
print(TEXTS[text_nr - 1])

# analýza
cleared = []
titlecase = []
uppercase = []
lowercase = []
numeric = []
numbers = []
freq = {}

words = TEXTS[text_nr - 1].split()
for clear_word in words:
    if clear_word:
        clear_word = clear_word.strip(",._!?")
        cleared.append(clear_word)
for word in cleared:
        word_lenght = len(word)
        if word_lenght in freq:
            freq[word_lenght] += 1
        else:
            freq[word_lenght] = 1
        if word.istitle():
            titlecase.append(word)
        elif word.isupper():
            uppercase.append(word)
        elif word.islower():
            lowercase.append(word)
        elif word.isnumeric():
            numeric.append(word)
freq_sort = dict(sorted(freq.items()))

# prvod číselného stringu na float
for number in numeric:
    numbers.append(float(number))

print(spacer)
print(f"There are {len(cleared)} words in selected text.")
print(f"There are {len(titlecase)} titlecase words in selected text.")
print(f"There are {len(uppercase)} uppercase words in selected text.")
print(f"There are {len(lowercase)} lowercase words in selected text.")
print(f"There are {len(numeric)} numeric strings in selected text.")
print(f"The sum of all numbers: {sum(numbers)}")
print(spacer)
print("LEN | OCURENCES           | NR")
print(spacer)

# graf
for length, count in freq_sort.items():
    stars = '*' * count
    print(f"{length:>3} | {stars:<19} | {count:>5}")
