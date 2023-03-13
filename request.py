from storage import Storage


class Request:
    def __init__(self, storage_dict: dict[Storage], request: str):
        self.storage_dict = storage_dict
        self.from_ = request.split()[4]
        self.to = request.split()[-1]
        self.amount = int(request.split()[1])
        self.product = request.split()[2]

    def working_with_moving(self) -> None:
        if not self.storage_dict[self.from_].is_in_storage(self.product):
            print('Такого продукьа нет на складе')


        if not self.storage_dict[self.from_].remove(self.product, self.amount):
            print('Нужнова количества нет на складе')

        print('Нужное количество есть на складе')
        print(f'Курьер забирает {self.amount} {self.product} со {self.from_}а')
        print(f'Курьер везет {self.amount} {self.product} со {self.from_}а в {self.to}')

        if self.storage_dict[self.to].add(self.product, self.amount):
            print(f'Курьер доставил {self.amount} {self.product} в {self.to}')
        else:
            print('В магазине недостаточно места')
