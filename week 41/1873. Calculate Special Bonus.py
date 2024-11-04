import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0  # Default bonus is 0
    employees.loc[
        (employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M')),
        'bonus'
    ] = employees['salary']  # Set bonus to 100% of salary where conditions are met
    # Return the result ordered by employee_id
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')