# ===== utils.py =====
import pandas as pd
import numpy as np
import random

def sequential_store(n):
    df = pd.DataFrame({
        "ID": range(1, n+1),
        "Name": [f"Record_{i}" for i in range(1, n+1)],
        "Value": [random.randint(10, 100) for _ in range(n)]
    })
    stats = pd.DataFrame({"Metric":["Access Time","Memory Usage"], "Value":[round(n*0.5,2), round(n*0.1,2)]})
    return df, stats

def indexed_store(n):
    df = pd.DataFrame({
        "ID": range(1, n+1),
        "Name": [f"Indexed_{i}" for i in range(1, n+1)],
        "Value": [random.randint(100, 500) for _ in range(n)]
    })
    stats = pd.DataFrame({"Metric":["Access Time","Memory Usage"], "Value":[round(n*0.3,2), round(n*0.2,2)]})
    return df, stats

def direct_store(n):
    df = pd.DataFrame({
        "ID": np.random.permutation(range(1, n+1)),
        "Name": [f"Direct_{i}" for i in range(1, n+1)],
        "Value": [random.randint(200, 700) for _ in range(n)]
    })
    stats = pd.DataFrame({"Metric":["Access Time","Memory Usage"], "Value":[round(n*0.2,2), round(n*0.25,2)]})
    return df, stats

def btree_store(n):
    df = pd.DataFrame({
        "ID": sorted(np.random.permutation(range(1, n+1))),
        "Name": [f"BTree_{i}" for i in range(1, n+1)],
        "Value": [random.randint(50, 600) for _ in range(n)]
    })
    stats = pd.DataFrame({"Metric":["Access Time","Memory Usage"], "Value":[round(n*0.1,2), round(n*0.3,2)]})
    return df, stats
