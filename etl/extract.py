import csv

def extract(file_path):
    """Extract data from the source CSV file."""
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    print("Data extracted successfully.")
    return data
