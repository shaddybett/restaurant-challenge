from models import Restaurant, Customer, Review, session

# # Clear existing data from the tables
# session.query(Review).delete()
# session.query(Customer).delete()
# session.query(Restaurant).delete()
# session.commit()

# # Add restaurants
# restaurant1 = Restaurant(name='Choma Zone', price=3)
# restaurant2 = Restaurant(name='Pasta Palace', price=4)
# restaurant3 = Restaurant(name='Sushi Haven', price=5)
# session.add_all([restaurant1, restaurant2, restaurant3])
# session.commit()

# # Display all restaurants
# all_restaurants = session.query(Restaurant).all()
# print("Restaurants:")
# for restaurant in all_restaurants:
#     print(f"ID: {restaurant.id}, Name: {restaurant.name}, Price: {restaurant.price}")

# # Add customers
# customer1 = Customer(first_name='Bob', last_name='Kai')
# customer2 = Customer(first_name='Alice', last_name='Smith')
# customer3 = Customer(first_name='Charlie', last_name='Brown')
# customer4 = Customer(first_name='David', last_name='Johnson')
# customer5 = Customer(first_name='Eva', last_name='Miller')
# session.add_all([customer1, customer2, customer3, customer4, customer5])
# session.commit()

# # Display all customers
# all_customers = session.query(Customer).all()
# print("\nCustomers:")
# for customer in all_customers:
#     print(f"ID: {customer.id}, Name: {customer.full_name()}")

# # Add reviews
# review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=4)
# review2 = Review(restaurant=restaurant2, customer=customer2, star_rating=5)
# review3 = Review(restaurant=restaurant3, customer=customer3, star_rating=3)
# review4 = Review(restaurant=restaurant1, customer=customer4, star_rating=4)
# review5 = Review(restaurant=restaurant2, customer=customer5, star_rating=5)
# session.add_all([review1, review2, review3, review4, review5])
# session.commit()

# # Display all reviews
# all_reviews = session.query(Review).all()
# print("\nReviews:")
# for review in all_reviews:
#     print(review.full_review())
