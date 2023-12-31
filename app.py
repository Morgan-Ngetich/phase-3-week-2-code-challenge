from lib.Customer import Customer
from lib.Restaurant import Restaurant
from lib.Review import Review

if __name__ == '__main__':
    # Create customers
    john = Customer("John", "Doe")
    alice = Customer("Alice", "Smith")
    bob = Customer("Bob", "Johnson")

    # Create restaurants
    restaurant_1 = Restaurant("Restaurant One")
    restaurant_2 = Restaurant("Restaurant Two")

    # Customers adding reviews for restaurants
    john.add_review(restaurant_1, 4)
    john.add_review(restaurant_2, 3)
    alice.add_review(restaurant_1, 5)
    bob.add_review(restaurant_2, 2)

    # Display Customers
    print("CUSTOMERS:")
    print("All Customers:")
    all_customers = Customer.all()
    for customer in all_customers:
        print(f"- {customer.full_name()}")

    print(f"(Full name of John): {john.full_name()}")
    print(f"(Restaurants reviewed by Alice): {', '.join(alice.restaurants())}")

    # Display Restaurants
    print("\nRESTAURANTS:")
    print("All Restaurants:")
    all_restaurants = Restaurant.all()
    for restaurant in all_restaurants:
        print(f"- {restaurant.name()}")

    print("\nReviews for Restaurant One:")
    reviews_restaurant_1 = restaurant_1.reviews()
    for customer_name in reviews_restaurant_1:
        print(f"- Reviewed by: {customer_name}")

    print(f"\nAverage star rating for Restaurant Two: {restaurant_2.average_star_rating()}")

    # Display Reviews
    print("\nREVIEWS:")
    all_reviews = Review.all()
    for review in all_reviews:
        print(str(review))  # This will use the __str__() method to print review information

    print(f"\nNumber of reviews by John: {john.num_reviews()}")

    # Finding Customers
    print("\nFinding customers:")
    print(f"Customer with name 'John Doe': {Customer.find_by_name('John Doe')}")
    print(f"Customers with given name 'Alice': {', '.join(Customer.find_all_by_given_name('Alice'))}")
