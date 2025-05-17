# Code-Challenge---Coffee-Shop-Object-Relationships---Compulsory

# Scenario:

# You are tasked with building a domain model for a Coffee Shop. Your model will consist of three main entities: `Customer`, `Coffee`, and `Order`. The relationships are as follows:

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

# The `Customer` and `Coffee` entities have a many-to-many relationship through the `Order` entity.

# Instructions

1. Setup and Preparation
2. Domain Model Design
3. Create Class Files
4. Implement Initializers and Properties
5. Define Object Relationship Methods and Properties
6. Implement Aggregate and Association Methods
7. Implement a class method
8. Bonus Task - Optional (Testing)

# - Create a `tests` directory in your project directory.

# - Add test files (`test_customer.py`, `test_coffee.py`, # test_order.py`) to test each class and method.

# - Write test cases to validate that each method and property works correctly.

# - Use `pytest` to run your tests:

# ```bash

# pytest

    ```

9. Handle Exceptions and Validate Inputs
10. Debugging and Refactoring
