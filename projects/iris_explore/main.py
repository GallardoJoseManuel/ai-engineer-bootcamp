import pandas as pd


def main():
    df = pd.read_csv("data/iris.csv")

    print(df)
    print(df.shape)     # (150,5)
    print(df.columns)   # Returns a pandas object called Index to allow us to operate with columns
    print(df.dtypes)    # Returns a pandas object called Series
    print()
    df.info()
    print()
    print(df.describe())
    print(df["sepal.length"])                           # Returns a Series object with colum sepal.length
    print(df[["sepal.length", "petal.length"]])         # Double [] to indicate we are operating with a list 
    print(type(df["sepal.length"]))                     # Returns type = Series
    print(type(df[["sepal.length", "petal.length"]]))   # Returns type = DataFrame
    mask = df["petal.length"] > 5   
    print(mask)
    print(type(mask))                                       # Returns an object Series, boolean values true or false 
    print(df.groupby("variety").mean(numeric_only=True))    # group flowers per type (variety), calculates the mean of each feature and ignores those one which are not numeric (numeric_only = true)


if __name__ == "__main__":
    main()