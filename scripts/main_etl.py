import os
from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    base_dir = os.getcwd()
    data_dir = os.path.join(base_dir, 'data')
    warehouse_dir = os.path.join(base_dir, 'warehouse')

    print("Extracting data...")
    data = extract_data(data_dir)
    print("Transforming data...")
    tables = transform_data(data)
    print("Loading data to warehouse...")
    load_data(warehouse_dir, tables)
    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    main()