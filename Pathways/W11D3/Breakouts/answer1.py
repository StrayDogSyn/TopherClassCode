# Breakout Room 1: Designing a Simple Database Schema
# INSTRUCTOR ANSWER SHEET

# =============================================================================
# SCENARIO: ONLINE BOOKSTORE DATABASE
# =============================================================================
# This is a sample solution for the online bookstore database schema design.
# You may see different solutions from students, which might also be valid.
# Focus on whether they've understood the core concepts of data modeling.

# =============================================================================
# TASK 1: ENTITY IDENTIFICATION (Sample Answer)
# =============================================================================
entities = [
    "Book",           # Main product being sold
    "Author",         # Creator of books
    "Customer",       # User who purchases books
    "Order",          # Transaction record
    "OrderItem",      # Individual items within an order
    "Review",         # Customer feedback on books
    "Category"        # Genre/classification of books
]

# =============================================================================
# TASK 2: ENTITY ATTRIBUTES (Sample Answer)
# =============================================================================

book_attributes = {
    "book_id": "integer (primary key)",
    "title": "string",
    "isbn": "string",
    "publication_date": "date",
    "price": "decimal",
    "publisher": "string",
    "stock_quantity": "integer",
    "description": "text"
}

author_attributes = {
    "author_id": "integer (primary key)",
    "first_name": "string",
    "last_name": "string",
    "biography": "text",
    "birth_date": "date"
}

customer_attributes = {
    "customer_id": "integer (primary key)",
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "password": "string (hashed)",
    "shipping_address": "string",
    "billing_address": "string",
    "phone_number": "string",
    "registration_date": "date"
}

order_attributes = {
    "order_id": "integer (primary key)",
    "customer_id": "integer (foreign key)",
    "order_date": "datetime",
    "status": "string",
    "shipping_address": "string",
    "payment_method": "string",
    "total_amount": "decimal"
}

order_item_attributes = {
    "order_item_id": "integer (primary key)",
    "order_id": "integer (foreign key)",
    "book_id": "integer (foreign key)",
    "quantity": "integer",
    "unit_price": "decimal",
    "subtotal": "decimal"
}

review_attributes = {
    "review_id": "integer (primary key)",
    "book_id": "integer (foreign key)",
    "customer_id": "integer (foreign key)",
    "rating": "integer",
    "comment": "text",
    "review_date": "datetime"
}

category_attributes = {
    "category_id": "integer (primary key)",
    "name": "string",
    "description": "text"
}

# =============================================================================
# TASK 3: RELATIONSHIPS (Sample Answer)
# =============================================================================

relationships = [
    "Book to Author: Many-to-Many (A book can have multiple authors, and an author can write multiple books)",
    "Book to Category: Many-to-Many (A book can belong to multiple categories, and a category can contain multiple books)",
    "Customer to Order: One-to-Many (A customer can place multiple orders, but each order belongs to only one customer)",
    "Order to OrderItem: One-to-Many (An order can contain multiple order items, but each order item belongs to only one order)",
    "Book to OrderItem: One-to-Many (A book can appear in multiple order items, but each order item refers to only one book)",
    "Book to Review: One-to-Many (A book can have multiple reviews, but each review is for only one book)",
    "Customer to Review: One-to-Many (A customer can write multiple reviews, but each review is written by only one customer)"
]

# =============================================================================
# TASK 4: PYTHON REPRESENTATION (Sample Answer)
# =============================================================================

class Book:
    def __init__(self, book_id, title, isbn, publication_date, price, publisher, stock_quantity, description):
        self.book_id = book_id
        self.title = title
        self.isbn = isbn
        self.publication_date = publication_date
        self.price = price
        self.publisher = publisher
        self.stock_quantity = stock_quantity
        self.description = description
        self.authors = []  # List to store relationships to Author objects
        self.categories = []  # List to store relationships to Category objects
        self.reviews = []  # List to store relationships to Review objects
    
    def add_author(self, author):
        """Associate an author with this book"""
        self.authors.append(author)
        
    def add_to_category(self, category):
        """Add this book to a category/genre"""
        self.categories.append(category)
        
    def add_review(self, review):
        """Add a customer review to this book"""
        self.reviews.append(review)
        
    def update_stock(self, quantity):
        """Update the available stock quantity"""
        self.stock_quantity = quantity
        
    def is_in_stock(self):
        """Check if the book is currently available"""
        return self.stock_quantity > 0
        
    def display_info(self):
        """Display basic information about the book"""
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"ISBN: {self.isbn}")
        print(f"Price: ${self.price}")
        print(f"In Stock: {self.stock_quantity} copies")
        
        if self.authors:
            author_names = [f"{author.first_name} {author.last_name}" for author in self.authors]
            print(f"Authors: {', '.join(author_names)}")
            
        if self.categories:
            category_names = [category.name for category in self.categories]
            print(f"Categories: {', '.join(category_names)}")