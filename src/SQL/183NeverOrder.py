import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    naCustomers = df['customerId'].isna()
    res = df[naCustomers]
    return res[['name']].rename(columns={'name': 'Customers'})