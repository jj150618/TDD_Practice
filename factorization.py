class Factorization:
    def __init__(self):
        pass

    def get_factorization(self, number: int) -> list:
        element = list()

        divider = 2
        while number > 1:
            while number % divider == 0:
                element.append(divider)
                number = number // divider
            divider += 1
        return element
