from FancyGrocery import FancyFoodItem

def create_food_list():
    food_list = []
    print("Food prices per pound = \n'Dry Cured Iberian Ham': 177.80,\n'Wagyu Steaks': 450.00,\n'Matsutake Mushrooms': 272.00,\n'Kopi Luwak Coffee': 306.50,\n'Moose Cheese': 487.20,\n'White Truffles': 3600.00,\n'Blue Fin Tuna': 3603.00,\n'Le Bonnotte Potatoes': 270.81,\n")
    num_items = int(input("How many items will you order today? "))
    while num_items < 1:
        print("Number of items must be at least 1.")
        num_items = int(input("How many items will you order today? "))

    for i in range(1, num_items + 1):
        print(f"Item #{i}-")
        food_name = input("Enter food: ")
        amount_in_pounds = float(input("Enter amount of pounds: "))
        while amount_in_pounds <= 0:
            print("Amount of pounds must be greater than 0.")
            amount_in_pounds = float(input("Enter amount of pounds: "))

        food_item = FancyFoodItem(food_name, amount_in_pounds)
        food_list.append(food_item)

    return food_list

def display_food_list(food_list):
    for item in food_list:
        print(item)
        print()

def calculate_total_cost(food_list):
    total_cost = sum(item.calculate_cost() for item in food_list)
    return total_cost

def main():
    items_list = create_food_list()
    display_food_list(items_list)
    total_cost = calculate_total_cost(items_list)
    print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
