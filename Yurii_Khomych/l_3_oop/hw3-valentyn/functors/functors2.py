class Prod:
    def __init__(self, value):  # Принимает единственный аргумент
        self.value = value

    def __call__(self, other):
        return self.value * other


X = Prod(2)  # Запоминает 2 в своей области видимости
print(X.value)
print(X(3))  # 3 (передано) * 2 (сохраненное значение)
print(X(4))  # 4 (передано) * 2 (сохраненное значение)
