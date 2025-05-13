# Example 4: Data Flows in Software Applications
# This demonstrates how data moves through an application with validation and transformation

# =============================================================================
# DATA FLOW CONCEPT: Input Validation, Transformation, and Storage
# =============================================================================
# This example shows a typical data flow for user registration:
# 1. Collect input data
# 2. Validate the data
# 3. Transform/clean the data
# 4. Store the data
# 5. Return a response

def is_valid_email(email):
    """Validate email format"""
    # Basic validation: check for @ symbol and at least one dot after it
    if not "@" in email:
        return False
    
    # Split email into username and domain parts
    username, domain = email.split("@", 1)
    
    # Check that username and domain are not empty
    if not username or not domain:
        return False
    
    # Check that domain has at least one dot
    if not "." in domain:
        return False
    
    return True

def is_strong_password(password):
    """Validate password strength"""
    # Check length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    return True

def validate_registration_data(data):
    """Validate all registration data"""
    errors = []
    
    # Required fields
    if not data.get("username"):
        errors.append("Username is required")
    
    if not data.get("email"):
        errors.append("Email is required")
    else:
        if not is_valid_email(data["email"]):
            errors.append("Email format is invalid")
    
    if not data.get("password"):
        errors.append("Password is required")
    else:
        if not is_strong_password(data["password"]):
            errors.append("Password must be at least 8 characters with an uppercase letter and a number")
    
    return errors

def transform_registration_data(data):
    """Clean and transform registration data"""
    transformed_data = {}
    
    # Normalize username (lowercase, strip spaces)
    if "username" in data:
        transformed_data["username"] = data["username"].lower().strip()
    
    # Normalize email (lowercase)
    if "email" in data:
        transformed_data["email"] = data["email"].lower().strip()
    
    # Password (will be hashed in a real application)
    if "password" in data:
        # In a real app, you'd use a secure hashing function like:
        # transformed_data["password_hash"] = hash_password(data["password"])
        transformed_data["password"] = f"HASHED_{data['password']}"  # Placeholder for demonstration
    
    # Add additional fields with defaults
    transformed_data["registration_date"] = "2025-05-12"  # In real code: datetime.now()
    transformed_data["is_active"] = True
    
    return transformed_data

def store_user_data(transformed_data):
    """Store the transformed user data (simulated)"""
    # In a real application, this would save to a database
    print(f"Storing user data in database...")
    print(f"New user created: {transformed_data['username']}")
    print(f"Email: {transformed_data['email']}")
    print(f"Registration date: {transformed_data['registration_date']}")
    return {"user_id": 12345}  # Simulated database ID

def registration_flow(user_data):
    """Complete flow for user registration"""
    print("\n--- Starting Registration Flow ---")
    
    # Step 1: Validate the input data
    print("Validating input data...")
    validation_errors = validate_registration_data(user_data)
    
    if validation_errors:
        print("Validation failed with errors:")
        for error in validation_errors:
            print(f"- {error}")
        return {"success": False, "errors": validation_errors}
    
    # Step 2: Transform/clean the data
    print("Transforming data...")
    transformed_data = transform_registration_data(user_data)
    
    # Step 3: Store the data
    print("Storing data...")
    storage_result = store_user_data(transformed_data)
    
    # Step 4: Return a response
    return {
        "success": True,
        "user_id": storage_result["user_id"],
        "message": f"User {transformed_data['username']} registered successfully!"
    }

# Example usage:
# Valid registration data
good_user_data = {
    "username": "JohnDoe",
    "email": "john.doe@example.com",
    "password": "SecurePass123"
}

# Invalid registration data
bad_user_data = {
    "username": "Jane",
    "email": "not-an-email",
    "password": "weak"
}

# Process both examples
result1 = registration_flow(good_user_data)
print("\nResult:", result1)

result2 = registration_flow(bad_user_data)
print("\nResult:", result2)

# =============================================================================
# KEY CONCEPTS DEMONSTRATED:
# =============================================================================
# 1. Input Validation: Checking data before processing it
# 2. Data Transformation: Cleaning and normalizing data
# 3. Data Storage: Persisting data (simulated here)
# 4. Error Handling: Detecting and reporting errors
# 5. Functional Separation: Breaking the process into distinct steps
# 6. Data Flow Pipeline: Connecting the steps in a logical sequence