# from lib.Customer import Customer

class Review:
    _all = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review._all.append(self)
        restaurant._reviews.append(self)
        customer._reviews.append(self)

    def rating(self):
        return self._rating

    def __str__(self):
        return f"Review by ({self._customer.full_name()}) for ({self._restaurant.name()}) with rating [{self._rating}]."
    
    @classmethod
    def all(cls):
        return cls._all

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant
