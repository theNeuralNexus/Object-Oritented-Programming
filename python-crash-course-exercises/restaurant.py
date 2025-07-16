class Restaurant:
    """
    Modeling real world restaurant.
    """

    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        """
        Initializing the restaurant class attributes

        Args:
            restaurant_name (str): Name of the restaurant
            cuisine_type (str): Type of the cuisine
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """
        Describe the restaurant
        """
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        """
        Open the restaurant
        """
        print("Restaurant is open.")


restaurant_1 = Restaurant("Py Pizza", "Italian")


restaurant_1.open_restaurant()
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("Atmoic Steak", "BBQ")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("Sea Eaters", "Sea Food")
restaurant_3.describe_restaurant()