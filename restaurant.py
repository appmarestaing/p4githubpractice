restaurants = []

def get_input():
    answer = input("give me a restaurant: ")
    return answer


def add_restaurants(allow_repeats):
    new_restaurant = get_input()
    while new_restaurant != "stop":
        if allow_repeats == False and new_restaurant in restaurants:
            print("pick a different restaurant")
        else:
            restaurants.append(new_restaurant)
        new_restaurant = get_input()

add_restaurants(False)
print(restaurants)