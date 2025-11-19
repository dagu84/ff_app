import polars as pl
import pandas as pd
import nflreadpy as nfl

def load_player_stats(year: list) -> pd.DataFrame:
    data = nfl.load_player_stats(year)
    df = pd.DataFrame(data, columns=data.columns)
    return df
