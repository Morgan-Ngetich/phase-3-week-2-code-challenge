from lib.Review import Review

class Restaurant:
    _all = []

    # Initializes a Restaurant instances
    def __init__(self, name):
        self._name = name
        Restaurant._all.append(self)
        self._reviews = []
       
    # Returns all restaurant instances
    @classmethod 
    def all(cls):
        return cls._all

    # Returns the name of the restaurant
    def name(self):
        return self._name

    # Returns a list of cutomers' full names who reviewed the restaurant
    def reviews(self):
        return [review.customer().full_name() for review in self._reviews]

    # Retunrs unique list of cutomers who reviewed the restaurant
    def customers(self):
        return list({review.customer() for review in self._reviews})

    # Calculates the average star rating for the restaurant
    def average_star_rating(self):
        if not self._reviews:
            return 0
        total_rating = sum(review.rating() for review in self._reviews)
        return total_rating / len(self._reviews)
