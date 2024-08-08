import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    res = person.groupby('email')['id'].count()
    res = res.reset_index()
    res = res[res['id'] > 1][['email']]
    return res