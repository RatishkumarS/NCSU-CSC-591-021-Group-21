import subprocess
from config import CONFIG

# Define k and m values
k_values = [0, 1, 2, 3]
m_values = [0, 1, 2, 3]

print("Results for soybean.csv dataset")
print("|   k   |   m   |   Accuracy   |")

# Iterate over k and m
temp = CONFIG()
for k in k_values:
    temp.setthe("k", k)
    for m in m_values:
        temp.setthe("m", m)
        # Command to run main.py
        command = f"python main.py --file \"soybean.csv\""
        # print(temp.the["k"], temp.the["m"])

        # Capture output
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # print(result)

        accuracy_line = [line for line in result.stdout.split('\n') if 'Accuracy' in line]
        accuracy = float(accuracy_line[0].split()[-1]) if accuracy_line else None

        accuracy_str = f"{accuracy:.2f}%" if accuracy is not None else "N/A"
        print(f"|   {k}   |   {m}   |   {accuracy_str}   |")