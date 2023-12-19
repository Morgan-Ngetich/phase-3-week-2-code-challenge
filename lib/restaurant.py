class Restaurant:
  def __init__(self, name): 
    self.name = name  # Initializr restaurant name
    self.reviews_received = []  # List to store reviews recieved by the restaurant
    
  # Getter methods to return attributes
  def get_name(self): 
    return self.name  # Return names
  
  def get_reviews(self):
    return self.reviews_received # Returns all reviews received by the restaurant

  # Return a list of unique customers who reviewed this restaurant.
  def customers(self):
    return list(set(review.customer() for review in self.reviews_received))

  # Calculated & returns the average star rating for the restaurant
  def average_star_rating(self):
    if not self.reviews_received:
      return 0  # Return 0 if no reviews are present
    total_rating = sum(review.rating() for review in self.reviews_received)
    return total_rating / len(self.reviews_received)



# # Create restaurants
# restaurant1 = Restaurant("Restaurant A")
# restaurant2 = Restaurant("Restaurant B")
# restaurant3 = Restaurant("Restaurant C")


# # Test methods
# print("--- Testing Restaurant Methods ---")
# print(restaurant1.name)  # Restaurant A
# print([str(customer) for customer in restaurant2.customers()])  # List of customers who reviewed restaurant2
# print(restaurant3.average_star_rating())  # Average rating for restaurant3
