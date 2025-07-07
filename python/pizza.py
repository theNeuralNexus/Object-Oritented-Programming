class PizzaShop:
    """
    Implementation of a pizza shop from the real world.
    """

    def __init__(
        self,
        name: str,
        location: str,
        rating: int,
        toppings: list[str],
        delivery: bool = True,
    ) -> None:
        """
        Initiliazing current object's instance varibles

        Args:
            name (str): Name of the pizza shop
            location (str): Location of the pizza shop
            rating (int): Rating of the pizza shop
            toppings (list[str]): All the toppings available
            delivery (bool, optional): Is delivery available. Defaults to True.

        Raises:
            ValueError: If the rating is not valid
        """
        if rating not in [1, 2, 3, 4, 5]:
            raise ValueError("This is an invalid rating.")
        self.name = name
        self.location = location
        self.rating = rating
        self.toppings = toppings
        self.delivery = delivery

    def order_pizza(self) -> None:
        """Customers can order pizza"""
        print("---")
        print("Costomer wants to order a pizza.")
        print(f"Delivering a pizza from {self.name}, {self.location}.")
        print("Here is your pizza. Thanks! for ordering.")
        print("---")

    def __str__(self) -> str:
        """
        String representation of the current object

        Returns:
            str: Name, Location and Rating of the pizza
        """
        return f"{self.name}, {self.location} has {self.rating} star rating."


pizzashop = PizzaShop(
    "PyPizza", "Italy", 4, ["cheese", "sauce", "pesto sauce", "egg plants", "basil"]
)
pizzashop.order_pizza()
print(pizzashop)
