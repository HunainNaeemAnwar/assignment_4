from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """stored_logins is a dictionary where hashed email and passwords are saved."""
    
    # Convert the email to lowercase and strip extra spaces to avoid issues with case sensitivity and extra spaces
    email = email.strip().lower()  # stripping spaces and converting to lowercase
    
    # Check if the email exists in stored_logins
    if email in stored_logins:
        hashed_password = stored_logins[email]
        hashed_input_password = hash_password(password_to_check)
        
 
        
        # Return True if the hashed password matches
        if hashed_password == hashed_input_password:
            return True
    
    return False

def hash_password(password_to_Check):
    """Returns the SHA256 hashed value for the given password."""
    return sha256(password_to_Check.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "hunain@gmail.com": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",  # "123"
        "hunainnaeemanwar@gmail.com": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"   # "123"
    }

    email = input("Enter Email: ").strip()  
    password = input("Enter Password: ").strip()

    print(login(email, stored_logins, password))

if __name__ == '__main__':
    main()
