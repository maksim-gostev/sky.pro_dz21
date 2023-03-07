from storage import Storage


class Request:
    def __init__(self, storage_list: list[Storage], request: str):
        self.storage_list = storage_list
        self.from_ = request.split()[4]
        self.to = request.split()[-1]
        self.amount = int(request.split()[1])
        self.product = request.split()[2]

    def working_with_moving(self) -> None:
        if self.from_ == "склад" and self.to == "магазин":
            if self.storage_list[0].is_in_storage(self.product):

                if self.storage_list[0].remove(self.product, self.amount):
                    print('Нужное количество есть на складе')
                    print(f'Курьер забирает {self.amount} {self.product} со {self.from_}а')
                    print(f'Курьер везет {self.amount} {self.product} со {self.from_}а в {self.to}')

                    if self.storage_list[1].add(self.product, self.amount):
                        print(f'Курьер доставил {self.amount} {self.product} в {self.to}')
                    else:
                        print('В магазине недостаточно места')
                else:
                    print('Нужнова количества нет на складе')

            else:
                print('Такого продукьа нет на складе')



        else:
            if self.storage_list[1].is_in_storage(self.product):

                if self.storage_list[1].remove(self.product, self.amount):
                    print('Нужное количество есть в магазине')
                    print(f'Курьер забирает {self.amount} {self.product} из {self.from_}а')
                    print(f'Курьер везет {self.amount} {self.product} из {self.from_}а на{self.to}')

                    if self.storage_list[0].add(self.product, self.amount):
                        print(f'Курьер доставил {self.amount} {self.product} на {self.to}')
                    else:
                        print('На складе недостаточно места')
                else:
                    print('Нужнова количества нет в магазине')

            else:
                print('Такого продукьа нет в магазине')
