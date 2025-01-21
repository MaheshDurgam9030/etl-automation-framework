import csv

def load(data, target_file):
    """Load the transformed data into a target CSV file."""
    if not data:
        print("No data to load.")
        return

    fieldnames = data[0].keys()  # Get the headers from the data
    with open(target_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data loaded successfully into {target_file}.")
