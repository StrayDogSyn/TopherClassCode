# Example 5: Practical Data Modeling Patterns
# This demonstrates common patterns for organizing and accessing data

# =============================================================================
# DESIGN PATTERN: Repository Pattern
# =============================================================================
# The Repository Pattern separates the logic that retrieves data from the
# underlying storage, allowing for more modular and testable code.

class Book:
    """Book entity representing a book in our bookstore"""
    def __init__(self, book_id, title, author, price, stock):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
    
    def __str__(self):
        return f"{self.title} by {self.author} (${self.price:.2f})"


class BookRepository:
    """Repository for managing book data"""
    def __init__(self):
        # This would connect to a database in a real application
        # For this example, we'll use an in-memory dictionary
        self._books = {}
    
    def add(self, book):
        """Add a book to the repository"""
        self._books[book.book_id] = book
        return book.book_id
    
    def get(self, book_id):
        """Get a book by ID"""
        return self._books.get(book_id)
    
    def get_all(self):
        """Get all books"""
        return list(self._books.values())
    
    def update(self, book):
        """Update a book's information"""
        if book.book_id in self._books:
            self._books[book.book_id] = book
            return True
        return False
    
    def delete(self, book_id):
        """Remove a book from the repository"""
        if book_id in self._books:
            del self._books[book_id]
            return True
        return False
    
    def find_by_title(self, title):
        """Find books by title (case-insensitive partial match)"""
        title = title.lower()
        return [book for book in self._books.values() 
                if title in book.title.lower()]
    
    def find_by_author(self, author):
        """Find books by author (case-insensitive partial match)"""
        author = author.lower()
        return [book for book in self._books.values() 
                if author in book.author.lower()]


# =============================================================================
# DESIGN PATTERN: Data Transfer Objects (DTOs)
# =============================================================================
# DTOs are objects that carry data between processes, often used to transfer
# data between the application and the user interface.

class BookDTO:
    """Data Transfer Object for Book entity"""
    def __init__(self, book):
        self.id = book.book_id
        self.title = book.title
        self.author = book.author
        self.price = book.price
        # Note: We might exclude some internal fields like stock
    
    def to_dict(self):
        """Convert DTO to dictionary (useful for JSON conversion)"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "price": self.price
        }


# =============================================================================
# DESIGN PATTERN: Service Layer
# =============================================================================
# The Service Layer contains business logic and coordinates between repositories
# and the application's interface.

class BookService:
    """Service for managing book operations"""
    def __init__(self, book_repository):
        self.repo = book_repository
    
    def add_new_book(self, title, author, price, initial_stock=0):
        """Business logic for adding a new book"""
        # Generate a new ID (simplified for example)
        book_id = len(self.repo.get_all()) + 1
        
        # Create the book entity
        new_book = Book(book_id, title, author, price, initial_stock)
        
        # Use the repository to store it
        self.repo.add(new_book)
        
        # Return a DTO with the new book's data
        return BookDTO(new_book)
    
    def get_book_details(self, book_id):
        """Get details for a specific book"""
        book = self.repo.get(book_id)
        if not book:
            return None
        return BookDTO(book)
    
    def search_books(self, search_term):
        """Search for books by title or author"""
        # Search in both title and author fields
        title_matches = self.repo.find_by_title(search_term)
        author_matches = self.repo.find_by_author(search_term)
        
        # Combine results (avoiding duplicates)
        all_books = {}
        for book in title_matches + author_matches:
            all_books[book.book_id] = book
        
        # Convert to DTOs
        return [BookDTO(book) for book in all_books.values()]
    
    def update_book_price(self, book_id, new_price):
        """Update a book's price"""
        book = self.repo.get(book_id)
        if not book:
            return False
        
        # Maybe we have business rules about price changes
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        
        # Update the book
        book.price = new_price
        self.repo.update(book)
        return True
    
    def check_if_in_stock(self, book_id):
        """Check if a book is in stock"""
        book = self.repo.get(book_id)
        if not book:
            return False
        return book.stock > 0


# =============================================================================
# DESIGN PATTERN: Caching
# =============================================================================
# Caching stores frequently accessed data to improve performance.

class CachedBookRepository:
    """Repository with basic caching capability"""
    def __init__(self, repository):
        self.repository = repository
        self.cache = {}  # Simple in-memory cache
    
    def get(self, book_id):
        """Get a book, using cache if available"""
        # Check if the book is in the cache
        if book_id in self.cache:
            print(f"Cache hit for book {book_id}")
            return self.cache[book_id]
        
        # If not in cache, get from the repository
        print(f"Cache miss for book {book_id}")
        book = self.repository.get(book_id)
        
        # Store in cache for future use
        if book:
            self.cache[book_id] = book
        
        return book
    
    # Other methods would delegate to the repository
    # and update the cache as needed


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

# Create a repository and add some sample books
book_repo = BookRepository()
book_repo.add(Book(1, "Python Programming", "John Smith", 29.99, 10))
book_repo.add(Book(2, "Data Science Basics", "Jane Doe", 34.99, 5))
book_repo.add(Book(3, "Machine Learning Fundamentals", "John Smith", 49.99, 3))

# Create a service using the repository
book_service = BookService(book_repo)

# Add a new book
print("\n--- Adding a new book ---")
new_book = book_service.add_new_book("Advanced Python", "Sarah Johnson", 39.99, 7)
print(f"Added: {new_book.to_dict()}")

# Search for books
print("\n--- Searching for books by 'John' ---")
search_results = book_service.search_books("John")
for book in search_results:
    print(f"Found: {book.to_dict()}")

# Create a cached repository for improved performance
cached_repo = CachedBookRepository(book_repo)

# Demonstrate caching
print("\n--- Demonstrating caching ---")
print("First request:")
book1 = cached_repo.get(1)  # Cache miss
print(f"Retrieved: {book1}")

print("\nSecond request (should be from cache):")
book1_again = cached_repo.get(1)  # Cache hit
print(f"Retrieved: {book1_again}")

# =============================================================================
# KEY CONCEPTS DEMONSTRATED:
# =============================================================================
# 1. Repository Pattern: Abstracts data access logic
# 2. Data Transfer Objects: Separate internal and external data representations
# 3. Service Layer: Implements business logic and coordinates operations
# 4. Caching: Improves performance by reducing database access
# 5. Separation of Concerns: Each class has a single responsibility
# 6. Abstraction Layers: Different layers for different aspects of data handling