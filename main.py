from customer import Customer
from restaurant import Restaurant
from review import Review

# Create instances of customers and restaurants
customer1 = Customer("John", "Doe")
customer2 = Customer("Alice", "Smith")
customer3 = Customer("Bob", "Johnson")

restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")
restaurant3 = Restaurant("Restaurant C")

# Create reviews with instances
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)
review3 = Review(customer2, restaurant2, 3) 
review4 = Review(customer3, restaurant3, 2)
review5 = Review(customer1, restaurant2, 4)

# Test methods
print("--- Testing Review Methods ---")
print(review1.rating())
print(review2.customer().full_name())
print(review3.restaurant().get_name())
print([str(review.customer().full_name()) for review in Review.all()])