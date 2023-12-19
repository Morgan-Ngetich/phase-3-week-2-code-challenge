from customer import Customer
from restaurant import Restaurant


class Review:
  reviews = [] # List to hold reviews instances
  
  def __init__(self, customer, restaurant, rating): 
    self.customer_obj = customer  # Initialize customer associated with the review
    self.restaurant_obj =restaurant   # Initialize restaurant assocaited with the review
    self.rating_val = rating  # Initialize review rating
    customer.review_list.append(self)  # Add the review to the customer's authored reviews
    restaurant.reviews_received.append(self)  # Add the review to the restaurant's received reviews.
    Review.reviews.append(self) # Add the new review to the list
    
  # Getter method for attributes  --> [review rating]
  def rating(self): 
    return self.rating_val
  
  def customer(self):   # Returns the customer associated with the review
    return self.customer_obj
  
  def restaurant(self):
    return self.restaurant_obj  # Returns the restaurant associated with the review
  
  @classmethod
  def all(cls): 
    return cls.reviews   # Returns lists of all review instances
  
  

# # Create instances of customers and restaurants
# # customer1 = Customer("John", "Doe")
# # customer2 = Customer("Alice", "Smith")
# # customer3 = Customer("Bob", "Johnson")

# # restaurant1 = Restaurant("Restaurant A")
# # restaurant2 = Restaurant("Restaurant B")
# # restaurant3 = Restaurant("Restaurant C")

# # Create reviews with instances
# review1 = Review(customer1, restaurant1, 4)
# review2 = Review(customer2, restaurant1, 5)
# review3 = Review(customer2, restaurant2, 3)
# review4 = Review(customer3, restaurant3, 2)
# review5 = Review(customer1, restaurant2, 4)

# # Test methods
# print("--- Testing Review Methods ---")
# print(review1.rating())  # Rating for review1
# print(review2.customer().full_name())  # Full name of customer for review2
# print(review3.restaurant().name())  # Name of restaurant for review3
# print([str(review.customer().full_name()) for review in Review.all()])  # List of all reviews' customer names
  
    