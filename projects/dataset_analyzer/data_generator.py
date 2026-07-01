import numpy as np

def generate_dataset(rows, cols):
    return np.random.randint(1, 101, size=(rows, cols))  # 101 because the upper bound is exclusive
    