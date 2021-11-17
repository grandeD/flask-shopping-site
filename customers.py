"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    # __init__() method that can be passed a first name, last name, email address, and password
    def __init__ (self, first_name, last_name, email, password):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = hash(password)

    # __repr()__ method: print useful information about customer
    def __repr__(self):
        return f"<Customer: {self.first_name} {self.last_name}, {self.email}, {self.password}>"

# read_customers_from_file return dict {email: Customer() }
# format of file: first-name | last-name | email | password

def read_customers_from_file(filepath):

    customer_emails = {}
    with open(filepath) as file:
        for line in file:
            line = line.strip().split("|")
            first_name = line[0]
            last_name = line[1]
            email = line[2]
            password = line[3]
            customer_emails[email] = Customer(first_name, last_name, email, password)
    return customer_emails

# get_by_email() takes in email dictionary and returns Customer with that email
def get_by_email(emails, email):
    return emails.get(email, None)