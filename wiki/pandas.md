# Pandas

## What is Pandas?

Pandas is a Python library built on top of NumPy. It is mainly used for data analysis and manipulation.

Its main data structures are:

- Series (1D)
- DataFrame (2D)

---

## DataFrame vs Series

```python
df["column"]
```

Returns a **Series**.

```python
df[["column"]]
```

Returns a **DataFrame**.

---

## Useful methods

### shape

Returns a tuple with:

(rows, columns)

### columns

Returns the names of the columns.

### dtypes

Returns the data type of each column.

### info()

Displays information about the DataFrame structure.

### describe()

Computes descriptive statistics for numerical columns.

---

## Boolean masks

```python
mask = df["petal.length"] > 5
```

Returns a Series of booleans.

A mask can be used to filter rows.

```python
df[mask]
```

---

## Multiple conditions

Use:

- `&` → AND
- `|` → OR
- `~` → NOT

Example:

```python
df[(df["petal.length"] > 5) & (df["sepal.width"] > 3)]
```

---

## GroupBy

```python
df.groupby("variety").mean(numeric_only=True)
```

Groups rows by the values in the `variety` column and computes the mean for every numeric column.