import pandas as pd
import numpy as np




def to_list(df):
    """
    Create list of track & artists
    """
    combined = df['combined']
    track_artist = combined.tolist()
    return track_artist