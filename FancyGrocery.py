class FancyFoodItem:
    def __init__(self, food, amount):
        self.__food_name = food
        self.__amount_in_pounds = amount
        self.__standard_price = 0.0
        self.__calculated_price = 0.0
        self.PriceList()

    def PriceList(self):
        food_prices = {
            'dry cured iberian ham': 177.80,
            'wagyu steaks': 450.00,
            'matsutake mushrooms': 272.00,
            'kopi luwak coffee': 306.50,
            'moose cheese': 487.20,
            'white truffles': 3600.00,
            'blue fin tuna': 3603.00,
            'le bonnotte potatoes': 270.81,
        }

        lower_case_food_name = self.__food_name.lower()
        self.__standard_price = food_prices.get(lower_case_food_name, 0.00)

    def calculate_cost(self):
        self.__calculated_price = self.__amount_in_pounds * self.__standard_price
        return self.__calculated_price

    def get_food_name(self):
        return self.__food_name

    def get_amount_in_pounds(self):
        return self.__amount_in_pounds

    def get_standard_price(self):
        return self.__standard_price

    def get_calculated_price(self):
        return self.__calculated_price

    def __str__(self):
        return f"Item: {self.__food_name}\nAmount ordered: {self.__amount_in_pounds} pounds\nPrice per pound: ${self.__standard_price:.2f}\nPrice of order: ${self.__calculated_price:.2f}"
