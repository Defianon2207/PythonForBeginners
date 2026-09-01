from multiprocessing.managers import BaseManager, BaseProxy


class Calculator:
    def add(self, a, b):
        return a + b


class CalculatorProxy(BaseProxy):
    _exposed_ = ("add",)

    def add(self, a, b):
        return self._callmethod("add", (a, b))


class CalculatorManager(BaseManager):
    pass


CalculatorManager.register(
    "Calculator",
    callable=Calculator,
    proxytype=CalculatorProxy
)


if __name__ == "__main__":
    with CalculatorManager() as manager:
        calculator = manager.Calculator()

        print(calculator.add(10, 20))