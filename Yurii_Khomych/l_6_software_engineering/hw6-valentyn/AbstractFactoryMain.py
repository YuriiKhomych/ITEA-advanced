from abc import abstractmethod, ABC


class Chair(ABC):
    @abstractmethod
    def get_price(self):
        pass


class Table(ABC):
    @abstractmethod
    def get_view(self):
        pass

    @abstractmethod
    def get_price_with_tax(self, collaborator: Chair):
        pass


class OfficeChair(Chair):
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return f"Price = {self.price}"


class KitchenChair(Chair):
    def get_price(self):
        return "Kitchen chair result of function."


class OfficeTable(Table):
    def get_view(self):
        return "Created Office table"

    def get_price_with_tax(self, collaborator: Chair):
        result = collaborator.get_price()
        return f"Result of some function in Office Chair inside Office Table ({result})"


class KitchenTable(Table):
    def get_view(self):
        return "Kitchen table created"

    def get_price_with_tax(self, collaborator: Chair):
        result = collaborator.get_price()
        return f"Result of some function in Kitchen Chair inside Kitchen Table  ({result})"


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_chair(self):
        pass

    @abstractmethod
    def create_product_table(self):
        pass


class OfficeOrder(AbstractFactory):
    def create_product_chair(self,price):
        return OfficeChair(price)

    def create_product_table(self):
        return OfficeTable()


class KitchenOrder(AbstractFactory):
    def create_product_chair(self,price):
        return KitchenChair()

    def create_product_table(self):
        return KitchenTable()


def client_order_creating(factory: AbstractFactory):
    product_c = factory.create_product_chair(10)
    product_t = factory.create_product_table()

    print(f"{product_t.get_view()}")
    print(f"{product_t.get_price_with_tax(product_c)}", end="")


if __name__ == "__main__":    
    print("Ordering Office furniture:")
    client_order_creating(OfficeOrder())

    print("\n")

    print("Ordering Kitchen furniture:")
    client_order_creating(KitchenOrder())
