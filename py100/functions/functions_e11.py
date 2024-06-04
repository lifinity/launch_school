# internationalization 2
def greet(iso_code):
    match iso_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        case _:
            return 'Language not found. o/'
        
def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('_')[1].split('.')[0]

def local_greet(locale):
    lang = extract_language(locale)
    region = extract_region(locale)
    match (lang, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case ('en', 'CA'):
            return 'Hi!'
        case _:
            return greet(lang)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('en_CA.UTF-8'))       # Hi!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!