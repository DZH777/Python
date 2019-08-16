def greet_user(user):
    """Выводит простое приветствие."""
    print("Hello "+user.title()+"!")
    
greet_user('Igor')


def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    """Возвращает аккуратно отформатированное полное имя."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def print_models(unprinted_designs, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Имитация печати модели на 3D-принтере.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def make_pizza(*toppings):
    """Вывод списка заказанных дополнений."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)

