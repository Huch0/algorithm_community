import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    over100=animals.loc[animals['weight']>100].sort_values(by='weight', ascending=False)[['name']]
    return over100
    