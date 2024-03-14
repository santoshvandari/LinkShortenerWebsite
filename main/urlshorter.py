import string,random
from main.models import URLTable

def random_string_generator(N):
    res = ''.join(random.choices(string.ascii_uppercase, k = N))
    return res

def shorttext():
    text=random_string_generator(2)
    text=check(text)
    return text

def check(text):
    if URLTable.objects.filter(short_url=text).exists():
        text=text+random_string_generator(1)
        return check(text)
    return text    