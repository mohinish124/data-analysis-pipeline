# Data Analysis Pipeline

## Project Description

A modular ETL and analytics pipeline for a game app, built in Python 3.13.5.  
This project extracts, transforms, and loads raw game data into a local data warehouse (star schema), runs data quality tests, and generates business insights for forecasting and user behavior analysis.

---

## Features

- Modular ETL pipeline (Extract, Transform, Load)
- Star schema data warehouse (CSV output)
- Data quality and integrity tests
- Business insights and analytics scripts
- Easily extensible for new data sources and requirements

---

## Project Structure

```
data-analysis-pipeline/
│
├── data/                # Raw input CSV files (see below for required files)
├── warehouse/           # Output data warehouse tables (CSV)
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── main_etl.py
│   └── data_insights.py
├── tests/
│   └── test_etl.py
├── requirements.txt
└── README.md
```

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/mohinish124/data-analysis-pipeline.git
   cd data-analysis-pipeline
   ```

2. **Install dependencies (Python 3.13.5):**
   ```sh
   pip install -r requirements.txt
   ```

3. **Add your raw CSV files to the `data/` folder.**

---

## Required Input Files

Please add the following CSV files to the `/data` folder before running the ETL pipeline:

- `user.csv`
- `channel_code.csv`
- `plan_payment_frequency.csv`
- `plan.csv`
- `status_code.csv`
- `user_registration.csv`
- `user_plan.csv`
- `user_payment_detail.csv`
- `user_play_session.csv`

> **Note:**  
> Due to probable copyright and data privacy, the raw data input files are **not** included in this repository.  


---

## Example Commands

**Run the ETL pipeline:**
```sh
python scripts/main_etl.py
```

**Run data quality tests:**
```sh
python tests/test_etl.py
```

**Generate business insights:**
```sh
python scripts/data_insights.py
```

---

## Testing

- All data quality and integrity tests are in `tests/test_etl.py`.
- Run all tests and see readable results in the console:
  ```sh
  python tests/test_etl.py
  ```

---

## Output Files

After running the ETL pipeline, the following files will be generated in the `/warehouse` folder:

- `dim_user.csv`
- `dim_channel.csv`
- `dim_plan.csv`
- `dim_status.csv`
- `dim_platform.csv`
- `fact_user_registration.csv`
- `fact_user_plan.csv`
- `fact_user_payment.csv`
- `fact_play_session.csv`

These files represent the star schema data warehouse tables created from your raw input data.

---

## Test Case Output

All data quality test results are printed directly to the console when you run:

```sh
python tests/test_etl.py
```



```sh
python tests/test_etl.py 
```

---

## License

This project is licensed under the MIT License.

---

## Authors & Acknowledgements

Developed by [Mohinish Srivastava](https://github.com/mohinish124/data-analysis-pipeline).

