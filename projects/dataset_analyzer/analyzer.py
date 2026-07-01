def display_statistics(stats):
    print(f"Array shape = {stats['shape']}")
    print(f"Type of elements = {stats['dtype']}")
    print(f"Memory usage = {stats['memory_usage']}") 
    print(f"Columns mean = {stats['columns_mean']}")
    print(f"Rows mean = {stats['rows_mean']}")
    print(f"Columns max = {stats['columns_max']}")
    print(f"Rows max = {stats['rows_max']}")
    print(f"Columns min = {stats['columns_min']}")
    print(f"Rows min = {stats['rows_min']}")
    print(f"Columns std = {stats['columns_std']}")
    print(f"Rows std = {stats['rows_std']}")


def calculate_statistics(dataset):
    columns_mean = dataset.mean(axis = 0)
    rows_mean = dataset.mean(axis = 1)
    columns_max = dataset.max(axis = 0)
    rows_max = dataset.max(axis = 1)
    columns_min = dataset.min(axis = 0)
    rows_min = dataset.min(axis = 1)
    columns_std = dataset.std(axis = 0)
    rows_std = dataset.std(axis = 1)
    return {
        "shape": dataset.shape,
        "dtype": dataset.dtype,
        "memory_usage": dataset.nbytes,
        "columns_mean": columns_mean,
        "rows_mean": rows_mean,
        "columns_max": columns_max,
        "rows_max": rows_max,
        "columns_min": columns_min,
        "rows_min": rows_min,
        "columns_std": columns_std,
        "rows_std": rows_std
        }
