import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
     # Apply string capitalization to the 'name' column
    users['name'] = users['name'].str.capitalize()
    # Sort the DataFrame by 'user_id'
    result = users.sort_values(by='user_id').reset_index(drop=True)
    return result

# Re Commit