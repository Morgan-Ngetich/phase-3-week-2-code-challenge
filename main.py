from tabulate import tabulate

class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.review_list = []
        Customer.customers.append(self)

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

# Fixed customer names
customer_names = [
    ("John", "Doe"),
    ("Alice", "Smith"),
    ("Bob", "Johnson"),
    ("Emma", "Lee"),
    ("Michael", "Brown")
]

# Create customers
customers = [Customer(given_name, family_name) for given_name, family_name in customer_names]

# Display customer data as a table using tabulate
print("\nCustomer Data:")
customer_table = [[f"Customer_{i + 1}", customer.full_name()] for i, customer in enumerate(customers)]
print(tabulate(customer_table, headers=["ID", "Full Name"], tablefmt="grid"))

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews_received = []

# Fixed restaurant names
restaurant_names = [
    "Restaurant A",
    "Restaurant B",
    "Restaurant C",
    "Restaurant D",
    "Restaurant E"
]

# Create restaurants
restaurants = [Restaurant(name) for name in restaurant_names]

# Display restaurant data as a table using tabulate
print("\nRestaurant Data:")
restaurant_table = [[f"Restaurant_{i + 1}", name] for i, name in enumerate(restaurant_names)]
print(tabulate(restaurant_table, headers=["ID", "Name"], tablefmt="grid"))

class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer_obj = customer
        self.restaurant_obj = restaurant
        self.rating_val = rating
        customer.review_list.append(self)
        restaurant.reviews_received.append(self)
        Review.reviews.append(self)

# Fixed reviews
reviews_data = [
    (0, 0, 4),
    (1, 0, 5),
    (1, 1, 3),
    (2, 2, 2),
    (0, 1, 4)
]

# Create reviews
reviews = [Review(customers[c], restaurants[r], rating) for c, r, rating in reviews_data]

# Display review data as a table using tabulate
print("\nReview Data:")
review_table = [
    [
        f"Review {i + 1}",
        reviews[i].customer_obj.full_name(),
        reviews[i].restaurant_obj.name,
        reviews[i].rating_val
    ] for i in range(len(reviews))
]
print(tabulate(review_table, headers=["ID", "Customer", "Restaurant", "Rating"], tablefmt="grid"))
