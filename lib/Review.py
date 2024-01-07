# from lib.Customer import Customer

class Review:
    _all = []  # Initializes a Review instance with customer, restaurant and rating

    # Initializes a Review instances wiht customer, restaurant, and rating
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review._all.append(self)  # Adds this review instance to the list of all reviews
        restaurant._reviews.append(self) # Appends this review to the list of restaurant's reviews
        customer._reviews.append(self)  # Appends this review to the list of customer's reviews

    # Returns the rating given in the review
    def rating(self):
        return self._rating

    # Returns a string representation of the review
    def __str__(self):
        return f"Review by ({self._customer.full_name()}) for ({self._restaurant.name()}) with rating [{self._rating}]."
    
    # Returns all instances of the Review
    @classmethod
    def all(cls):
        return cls._all

    # Returns the customer associated with the review# 
    def customer(self):
        return self._customer

    # Returns the restaurant associated with the review
    def restaurant(self):
        return self._restaurant
