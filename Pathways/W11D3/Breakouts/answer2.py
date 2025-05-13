# Breakout Room 2: Implementing Data Flows
# INSTRUCTOR ANSWER SHEET

# =============================================================================
# SCENARIO: BOOK REVIEW SUBMISSION SYSTEM
# =============================================================================
# This is a sample solution for implementing a data flow for submitting
# book reviews in an online bookstore.

# =============================================================================
# TASK 1: DEFINE THE DATA MODEL (Sample Answer)
# =============================================================================

import datetime

class BookReview:
    def __init__(self, review_id=None, book_id=None, user_id=None, rating=None, comment=None, 
                 timestamp=None, status=None):
        self.review_id = review_id
        self.book_id = book_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        self.timestamp = timestamp or datetime.datetime.now()
        self.status = status or "pending"
        
    def is_valid(self):
        """Check if the review contains required fields with valid values"""
        if not self.book_id or not isinstance(self.book_id, int) or self.book_id <= 0:
            return False
        
        if not self.user_id or not isinstance(self.user_id, int) or self.user_id <= 0:
            return False
        
        if (not self.rating or not isinstance(self.rating, int) or 
                self.rating < 1 or self.rating > 5):
            return False
        
        return True
    
    def display(self):
        """Display the review information"""
        print(f"Review ID: {self.review_id}")
        print(f"Book ID: {self.book_id}")
        print(f"User ID: {self.user_id}")
        print(f"Rating: {self.rating} stars")
        if self.comment:
            print(f"Comment: {self.comment}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Status: {self.status}")

# =============================================================================
# TASK 2: IMPLEMENT INPUT VALIDATION (Sample Answer)
# =============================================================================

def validate_review_data(review_data):
    """
    Validate the review data before processing
    Return a list of error messages (empty if valid)
    """
    errors = []
    
    # Check if book_id is provided and valid
    if "book_id" not in review_data:
        errors.append("Book ID is required")
    else:
        try:
            book_id = int(review_data["book_id"])
            if book_id <= 0:
                errors.append("Book ID must be a positive number")
        except (ValueError, TypeError):
            errors.append("Book ID must be a number")
    
    # Check if user_id is provided and valid
    if "user_id" not in review_data:
        errors.append("User ID is required")
    else:
        try:
            user_id = int(review_data["user_id"])
            if user_id <= 0:
                errors.append("User ID must be a positive number")
        except (ValueError, TypeError):
            errors.append("User ID must be a number")
    
    # Check if rating is provided and valid
    if "rating" not in review_data:
        errors.append("Rating is required")
    else:
        try:
            rating = int(review_data["rating"])
            if rating < 1 or rating > 5:
                errors.append("Rating must be between 1 and 5")
        except (ValueError, TypeError):
            errors.append("Rating must be a number")
    
    # Check if comment is valid (if provided)
    if "comment" in review_data and review_data["comment"]:
        comment = str(review_data["comment"])
        if len(comment) > 500:
            errors.append("Comment must be less than 500 characters")
    
    return errors

# =============================================================================
# TASK 3: IMPLEMENT DATA TRANSFORMATION (Sample Answer)
# =============================================================================

def transform_review_data(review_data):
    """
    Transform and clean the review data
    Return the transformed data
    """
    transformed_data = {}
    
    # Convert IDs to integers
    if "book_id" in review_data:
        transformed_data["book_id"] = int(review_data["book_id"])
    
    if "user_id" in review_data:
        transformed_data["user_id"] = int(review_data["user_id"])
    
    if "rating" in review_data:
        transformed_data["rating"] = int(review_data["rating"])
    
    # Trim whitespace from comment
    if "comment" in review_data and review_data["comment"]:
        transformed_data["comment"] = str(review_data["comment"]).strip()
    
    # Add timestamp and status
    transformed_data["timestamp"] = datetime.datetime.now()
    transformed_data["status"] = "pending"
    
    # Generate a review ID (in a real system, this would come from the database)
    import random
    transformed_data["review_id"] = random.randint(10000, 99999)
    
    return transformed_data

# =============================================================================
# TASK 4: IMPLEMENT ERROR HANDLING (Sample Answer)
# =============================================================================

def handle_review_error(error_type, details):
    """
    Handle errors that occur during the review submission process
    """
    if error_type == "validation":
        # Return friendly error messages to the user
        return {
            "success": False,
            "error_type": "validation",
            "message": "Please fix the following issues:",
            "details": details
        }
    
    elif error_type == "database":
        # Log the error and return a generic message
        print(f"DATABASE ERROR: {details}")  # In a real system, use proper logging
        return {
            "success": False,
            "error_type": "system",
            "message": "Unable to save your review. Please try again later.",
            "reference_id": generate_error_reference()
        }
    
    elif error_type == "system":
        # Log the error and alert an administrator
        print(f"CRITICAL SYSTEM ERROR: {details}")  # In a real system, use proper logging
        alert_administrator(details)  # This would be implemented in a real system
        return {
            "success": False,
            "error_type": "system",
            "message": "A system error occurred. Support has been notified.",
            "reference_id": generate_error_reference()
        }
    
    else:
        # Unknown error type
        print(f"UNKNOWN ERROR TYPE: {error_type}, Details: {details}")
        return {
            "success": False,
            "error_type": "unknown",
            "message": "An unexpected error occurred. Please try again."
        }

def generate_error_reference():
    """Generate a unique reference ID for error tracking"""
    import random
    import string
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(8))

def alert_administrator(details):
    """Alert system administrator about a critical error"""
    # In a real system, this might send an email, text message, or create a ticket
    print(f"ALERT: Administrator notified about: {details}")

# =============================================================================
# TASK 5: IMPLEMENT THE FULL DATA FLOW (Sample Answer)
# =============================================================================

def submit_review_flow(review_data):
    """
    Process the full flow of submitting a review
    Return the result of the operation
    """
    print("\n--- Starting Review Submission Flow ---")
    
    # Step 1: Validate the input data
    print("Validating review data...")
    validation_errors = validate_review_data(review_data)
    
    # Step 2: If validation fails, handle the errors and return
    if validation_errors:
        print("Validation failed with errors:")
        for error in validation_errors:
            print(f"- {error}")
        return handle_review_error("validation", validation_errors)
    
    try:
        # Step 3: Transform the data
        print("Transforming review data...")
        transformed_data = transform_review_data(review_data)
        
        # Step 4: Create a BookReview object
        print("Creating review object...")
        review = BookReview(
            review_id=transformed_data["review_id"],
            book_id=transformed_data["book_id"],
            user_id=transformed_data["user_id"],
            rating=transformed_data["rating"],
            comment=transformed_data.get("comment", ""),
            timestamp=transformed_data["timestamp"],
            status=transformed_data["status"]
        )
        
        # Step 5: Simulate storing the review
        print("Storing review in database...")
        # In a real system, this would save to a database
        # For this example, we'll just display the review
        review.display()
        
        # Simulate database error (uncomment to test error handling)
        # if review.rating == 2:
        #     raise Exception("Database connection failed")
        
        # Step 6: Return a success message
        return {
            "success": True,
            "review_id": review.review_id,
            "message": "Thank you for your review! It has been submitted for approval."
        }
        
    except Exception as e:
        # Handle any unexpected errors
        return handle_review_error("system", str(e))

# =============================================================================
# TASK 6: TEST YOUR IMPLEMENTATION (Sample Answer)
# =============================================================================

# Example test data (valid)
valid_review = {
    "book_id": 123,
    "user_id": 456,
    "rating": 4,
    "comment": "This book was very helpful and well-written."
}

# Example test data (invalid)
invalid_review = {
    "book_id": "not_a_number",
    "rating": 7,  # Out of range
    "comment": "Too short"
    # Missing user_id
}

# Test the implementation
print("\n=== Testing Valid Review ===")
result1 = submit_review_flow(valid_review)
print("Result for valid review:", result1)

print("\n=== Testing Invalid Review ===")
result2 = submit_review_flow(invalid_review)
print("Result for invalid review:", result2)