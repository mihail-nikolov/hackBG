def add_eggs(n):
    eggs = ''
    if n % 5 == 0:
        eggs += 'eggs'
    return eggs


def add_spam(n):
    spam = ''
    while n % 3 == 0:
        spam += 'spam '
        n = n / 3
    return spam


def prepare_meal(n):
    spam_str = add_spam(n)
    eggs_str = add_eggs(n)
    end_string = ''
    if len(spam_str) > 0 and len(eggs_str) > 0:
        end_string = spam_str + "and " + eggs_str
    else:
        end_string = spam_str + eggs_str
    return end_string

print(prepare_meal(45))
