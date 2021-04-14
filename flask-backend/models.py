import pandas as pd
import numpy as np




def to_list(df):
    """
    Create list of NFTs
    """
    combined = df['combined']
    NFT_id = combined.tolist()
    return NFT_id