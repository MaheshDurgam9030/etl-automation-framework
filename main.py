from etl.extract import extract
from etl.transform import transform
from etl.load import load


def main():
    source_file = "data/source.csv"
    target_file = "data/target.csv"

    # Step 1: Extract
    data = extract(source_file)

    # Step 2: Transform
    transformed_data = transform(data)

    # Step 3: Load
    load(transformed_data, target_file)


if __name__ == "__main__":
    main()
