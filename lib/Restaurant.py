from lib.Review import Review

class Restaurant:
    _all = []

    def __init__(self, name):
        self._name = name
        Restaurant._all.append(self)
        self._reviews = []
       
    @classmethod 
    def all(cls):
        return cls._all

    def name(self):
        return self._name

    def reviews(self):
        return [review.customer().full_name() for review in self._reviews]

    def customers(self):
        return list({review.customer() for review in self._reviews})

    def average_star_rating(self):
        if not self._reviews:
            return 0
        total_rating = sum(review.rating() for review in self._reviews)
        return total_rating / len(self._reviews)
