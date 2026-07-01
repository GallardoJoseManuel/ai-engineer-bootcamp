from data_generator import generate_dataset
from analyzer import calculate_statistics, display_statistics
def main():
    rows = int(input("Type number of rows\n"))
    columns = int(input("Type number of columns\n"))
    matrix = generate_dataset(rows,columns)
    print(matrix)
    print()
    stats = calculate_statistics(matrix)
    print("==== STATISTICS ====\n")
    display_statistics(stats)


if __name__ == "__main__":
    main()