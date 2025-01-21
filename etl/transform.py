def transform(data):
    """Transform data by adding a full_name field."""
    for row in data:
        row["full_name"] = f"{row['first_name']} {row['last_name']}"
    print("Data transformed successfully.")
    return data
