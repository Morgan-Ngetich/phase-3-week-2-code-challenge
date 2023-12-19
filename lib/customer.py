class Customer:
  customers = [] # List to hold all the customer instances
  
  def __init__(self, given_name, family_name): # Initialise Customer instances with given & family names.
    self._given_name = given_name  # Initialize given name
    self._family_name = family_name  # Initailize family name
    self.review_list = []  # List to store the reviews by customers
    Customer.customers.append(self)  # Add the new customer to the customer's list
    
  # Getter method to get name attributes
  def given_name(self):  #Returns the customer's given name
    return self._given_name
  
  def family_name(self): # Return the customer's family name
    return self._family_name
  
  # Concatenate given & family names to form full name
  def full_name(self): 
    return f"{self._given_name} {self._family_name}"  
  
  
  @classmethod
  def all(cls):  
    return cls.customers # Return all instances of customers created.
  
  # Return the total number of reviews by the customers
  def num_reviews(self):
    return len(self.review_list)
  
  # Class method to find a customer by full name
  @classmethod
  def find_by_name(cls, name):
    for customer in cls.customers:
      if customer.full_name() == name:
        return customer
    return None

  # Class method to find all customers by given name
  @classmethod
  def find_all_by_given_name(cls, name):
    return [customer for customer in cls.customers if customer.given_name == name]

  # Display information on all customers in 'str' format.
  def __str__(self):
    return f"Customer: {self._given_name} {self._family_name}"
  
# # Create customers
# customer1 = Customer("John", "Doe")
# customer2 = Customer("Alice", "Smith")
# customer3 = Customer("Bob", "Johnson")


# # Test methods
# print("--- Testing Customer Methods ---")
# print(customer1._given_name)  # John
# print(customer2._family_name)  # Smith
# print(customer3.full_name())  # Bob Johnson
# print([str(customer) for customer in Customer.all()])  # List of all customers
# print(customer1.num_reviews())  # Number of reviews by customer1