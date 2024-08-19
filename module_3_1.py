calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(stroke):
    my_tuple = (len(stroke), stroke.upper(), stroke.lower())
    count_calls()
    return my_tuple


def is_contains(stroke, list_to_search):
    new_list = []
    for s in list_to_search:
        new_list.append(s.lower())
    if stroke.lower() in new_list:
        count_calls()
        return True
    else:
        count_calls()
        return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic'])) 
print(calls)
