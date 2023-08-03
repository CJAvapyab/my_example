def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
def make_car(maker,models,**user_info):
    """显示一辆车的制造商，型号和其他"""
    user_info['maker'] = maker
    user_info['models'] = models
    return user_info