import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(employee, how='left', left_on='managerId', right_on='id')
    res = merged[merged['salary_x'] > merged['salary_y']][['name_x']]
    return res.rename(columns={'name_x': 'Employee'})
    