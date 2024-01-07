from lib.Review import Review

# Creating  Customer class
class Customer:
    _all = []  # Initializing a class varible _all as an empty list

    # Constructor method for Customer class
    def __init__(self, name, family_name):
        self._name = name
        self._family_name = family_name
        Customer._all.append(self)  # Appending the instance for the _all list
        self._reviews = []  # Initializing an empty list for reviews

    # Method to return the customer's given name
    def given_name(self):
        return self._name

    # Method to return the customer's given name
    def family_name(self):
        return self._family_name

    # Method to return the full name of the customer
    def full_name(self):
        return f"{self._name} {self._family_name}"

    # Method returning all cutomer instances
    @classmethod
    def all(cls):
        return cls._all

    # Method to return a list of restaurant names reviewed by the customer
    def restaurants(self):
        return list({review.restaurant().name() for review in self._reviews})

    # Method to add a review for a restaurant by the customer
    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)  # Creating a new review instance
        self._reviews.append(new_review)   # Appending the new review to the customer's reviews

    # Method to return the total number of reviews by the customer
    def num_reviews(self):
        return len(self._reviews)

    # Method to find a customer by their full name
    @classmethod
    def find_by_name(cls, name):
        for customer in cls._all:
            if customer.full_name() == name:
                return customer.full_name()
        return None

    # Method to find customers by a given name
    @classmethod
    def find_all_by_given_name(cls, given_name):
        customers_with_given_name = []
        for customer in cls._all:
            if customer._name == given_name:
                customers_with_given_name.append(customer.full_name())
        return customers_with_given_name