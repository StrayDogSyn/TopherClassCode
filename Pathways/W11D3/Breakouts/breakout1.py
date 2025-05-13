# Breakout Room 1: Designing a Simple Database Schema
# Student Worksheet

# =============================================================================
# SCENARIO: ONLINE BOOKSTORE DATABASE
# =============================================================================
# Your team needs to design a database schema for a new online bookstore.
# The bookstore needs to manage books, customers, orders, and reviews.
# Together, you'll identify entities, attributes, and relationships,
# then represent one entity as a Python class.

# =============================================================================
# TASK 1: ENTITY IDENTIFICATION
# =============================================================================
# List all the main entities (objects) that should be in your database.
# Add at least 4-5 entities below:

entities = [
    # Example: "Book"
    # Add more entities here...
]

# =============================================================================
# TASK 2: ENTITY ATTRIBUTES
# =============================================================================
# For each entity, list the attributes (properties) they should have.
# Include data types and note which attribute would be the primary key.

# Example format:
book_attributes = {
    "book_id": "integer (primary key)",
    # Add more attributes here...
}

customer_attributes = {
    # Add attributes here...
}

# Add more entities and their attributes...

# =============================================================================
# TASK 3: RELATIONSHIPS
# =============================================================================
# Identify how the entities relate to each other.
# Describe each relationship and its type (One-to-One, One-to-Many, Many-to-Many)

relationships = [
    # Example: "Book to Author: Many-to-Many (A book can have multiple authors, and an author can write multiple books)"
    # Add more relationships here...
]

# =============================================================================
# TASK 4: PYTHON REPRESENTATION
# =============================================================================
# Choose one entity and implement it as a Python class.
# Include attributes as instance variables and add appropriate methods.

# Example (incomplete - you need to finish it):
class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        # Add more attributes here...
        
    # Add methods here...
    # For example: display_info, update_stock, add_author, etc.

# =============================================================================
# TASK 5: DISCUSSION QUESTIONS
# =============================================================================
# Discuss these questions as a group and write your answers as comments:

# 1. What challenges did you encounter when designing this schema?
# Answer: 

# 2. What trade-offs did you make in your design?
# Answer: 

# 3. How might your schema need to evolve as the bookstore grows?
# Answer: 

# 4. What potential data integrity issues should you watch out for?
# Answer: 

# 5. How would queries for common information (like a customer's order
#    history or all reviews for a book) work with your schema?
# Answer: