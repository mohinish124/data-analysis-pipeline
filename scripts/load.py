import os

def load_data(warehouse_dir, tables):
    os.makedirs(warehouse_dir, exist_ok=True)
    for name, df in tables.items():
        df.to_csv(os.path.join(warehouse_dir, f"{name}.csv"), index=False)