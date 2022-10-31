import click
import constants
from random import randint
from typing import Callable

from class_pizza import Pizza


@click.group()
def cli():
    '''main function which we call'''
    return 0


@cli.command()
def menu() -> None:
    '''print menu'''
    for pizza_name, ingredients in constants.receipts_data.items():
        print(f'— {pizza_name} {constants.emo_data[pizza_name]} : {", ".join(ingredients)}')
    print(f'Available sizes: {", ".join(constants.available_sizes)}')


def log(text: str) -> Callable:
    '''make logging for bake, delivery and pickup'''

    def decorator(func: Callable) -> Callable:
        def wrapper(pizza):
            cooking_time = randint(1, 10)
            print(text.format(pizza.name, pizza.size, cooking_time))

        return wrapper

    return decorator


@log('\U0001F373 Приготовили {} {} за {}c!')
def bake(pizza) -> int:
    '''simulation of cooking pizza'''
    return 0


@log('\U0001F9BC Доставили {} {} за {}c!')
def delivery_pizza(pizza) -> int:
    '''simulation of delivery pizza'''
    return 0


@log('\U0001F5FF Забрали {} {} за {}c!')
def pickup_pizza(pizza) -> int:
    '''simulation of pickup pizza'''
    return 0


@cli.command()
@click.option('--pickup', default=True, is_flag=True)
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', default='L', nargs=1)
def order(pizza: str, size: str, delivery: bool, pickup: bool) -> None:
    '''make the order or show error'''
    if pizza in constants.receipts_data and size in ['XL', 'L']:
        pizza_instance = Pizza(pizza, size)
        bake(pizza_instance)
        if delivery:
            delivery_pizza(pizza_instance)
        else:
            pickup_pizza(pizza_instance)
    else:
        print(constants.error_messages['non_existing_pizza'])


if __name__ == '__main__':
    cli()
