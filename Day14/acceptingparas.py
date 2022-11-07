# Decorators that accept parameters
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print('I live in {}'.format (para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(firstname, lastname, country):
    print('I am {} {}. I love Cattle.'.format(firstname, lastname, country))

print_full_name("Totona", "Lonyeiye", "Kenya")