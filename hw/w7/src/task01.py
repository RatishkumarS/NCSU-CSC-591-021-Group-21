def generate_ascii_table(csv_file_path):
    # Function to read CSV file and count the number of rows for each class
    def count_class_rows(file_path):
        print("\n")
        class_counts = {}
        total_rows = 0
        with open(file_path, "r") as file:
            header = next(file)
            for line in file:
                total_rows += 1
                columns = line.strip().split(",")
                class_label = columns[-1]
                class_counts[class_label] = class_counts.get(class_label, 0) + 1
        return class_counts, total_rows

    # Get class counts and total rows
    class_counts, total_rows = count_class_rows(csv_file_path)

    print("Total number of Rows in the dataset:", total_rows)

    # Convert counts to percentage
    class_percentage = {
        key: (value / total_rows) * 100 for key, value in class_counts.items()
    }

    # Determine the maximum width for formatting
    max_width_class = max(
        len("Class"), max(len(class_label) for class_label in class_counts)
    )
    max_width_rows = max(
        len("Number of Rows"), max(len(str(count)) for count in class_counts.values())
    )
    max_width_percentage = max(
        len("Class Percentage"),
        max(len(f"{percentage:.2f}%") for percentage in class_percentage.values()),
    )

    # Generate and print ASCII table
    print(
        f"{ 'Class':<{max_width_class}} | {'Number of Rows':<{max_width_rows}} | {'Class Percentage':<{max_width_percentage}}"
    )
    print("-" * (max_width_class + max_width_rows + max_width_percentage + 7))

    for class_label, count in class_counts.items():
        percentage = class_percentage[class_label]
        print(
            f"{class_label:<{max_width_class}} | {count:<{max_width_rows}} | {percentage:.2f}%"
        )


csv_file_path_diabetes = "../../Data/diabetes.csv"
csv_file_path_soybean = "../../Data/soybean.csv"


print("Diabetes Dataset")
generate_ascii_table(csv_file_path_diabetes)
print("\n\nSoybean Dataset")
generate_ascii_table(csv_file_path_soybean)
