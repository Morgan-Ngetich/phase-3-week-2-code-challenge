from lib.Review import Review

class Customer:
    _all = []

    def __init__(self, name, family_name):
        self._name = name
        self._family_name = family_name
        Customer._all.append(self)
        self._reviews = []

    def given_name(self):
        return self._name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls._all

    def restaurants(self):
        return list({review.restaurant().name() for review in self._reviews})

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self._reviews.append(new_review)

    def num_reviews(self):
        return len(self._reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls._all:
            if customer.full_name() == name:
                return customer.full_name()
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        customers_with_given_name = []
        for customer in cls._all:
            if customer._name == given_name:
                customers_with_given_name.append(customer.full_name())
        return customers_with_given_name