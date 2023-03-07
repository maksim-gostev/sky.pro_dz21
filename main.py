
from request import Request
from utils import create_store, create_shop, is_stop


def run():
    store = create_store()
    shop = create_shop()

    while True:

        print("Введите строку вида: 'Доставить 3 печеньки из склад в магазин'")
        user_input = input()

        if user_input:

            if is_stop(user_input):
                print('Всего доброго')
                break

            if checking_validity_string(user_input):

                request = Request([store, shop], user_input)

                request.working_with_moving()
                print("=" * 30)
                print(f"На складе хранится:")
                print(store.get_items())
                print(f"\nВ магазине хранится:")
                print(shop.get_items())
            else:
                print('Вы ввели не корректные данные попробуйте снова')

        else:
            print('Вы ничего не ввели')


def checking_validity_string(user_str: str) -> bool:
    """
    вповеряет правельность строки от пользователя
    :param user_str: str
    :return: bool
    """
    user_list = user_str.split(' ')
    if user_list[4] in ['склад', 'магазин'] and user_list[-1] in ['склад', 'магазин'] and user_list[1].isdigit():
        return True
    else:
        return False


if __name__ == '__main__':
    run()
