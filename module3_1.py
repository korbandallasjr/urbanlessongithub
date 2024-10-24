my_string = ''
calls = 0
string_elements = ()


def count_calls():
    global calls
    calls += 1


def string_info(my_string):
    count_calls()
    global string_elements
    string_elements = (len(my_string), my_string.upper(), my_string.lower())
    return string_elements


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    lowercase_list = [s.lower() for s in list_to_search]
    if string in lowercase_list:
        return True
    else:
        return False


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)
