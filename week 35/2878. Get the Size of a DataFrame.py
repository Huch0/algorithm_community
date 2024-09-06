import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df_rows, df_cols = players.shape
    return [df_rows,df_cols]