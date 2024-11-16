import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Define a regex pattern for valid email addresses
    email_pattern = r'^[a-zA-Z][\w.-]*@leetcode\.com$'
    # Filter rows where 'email' matches the regex pattern
    valid_users = users[users['mail'].str.match(email_pattern, na=False)]
    return valid_users