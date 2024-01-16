import sys
from data import DATA

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 5 or sys.argv[1] != "-f" or sys.argv[3] != "-t":
    print("Usage: python3 gate.py -f <input_file> -t <method>")
    sys.exit(1)

# Extract input file and method from command-line arguments
input_file = sys.argv[2]
method = sys.argv[4]

# Instantiate DATA or use an existing instance
data_instance = DATA(input_file)

# Call the specified method and write the result to the standard output
if method == "stats":
    result1 = data_instance.mid()
    result2 = data_instance.print_cols()
    sys.stdout.write(str(result1.cells))
    sys.stdout.write(str(result2))
else:
    print(f"Error: Unknown method '{method}'")
    sys.exit(1)
