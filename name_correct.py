import re

def is_name_correct(name):
    pattern = re.compile(r'^[a-zA-Zа-яА-Я0-9 \-]+$')
    return bool(pattern.match(name))