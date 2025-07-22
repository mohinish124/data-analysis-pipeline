import pandas as pd
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

warehouse_dir = os.path.join(os.getcwd(), 'warehouse')

# Global test case counter
test_case_counter = [1]

def print_case(title, result, details=""):
    case_num = test_case_counter[0]
    print("\n" + "="*60)
    print(f"Test Case {case_num}: {title}")
    print(f"Result   : {result}")
    if details:
        print("-" * 60)
        print(details)
    print("="*60)
    test_case_counter[0] += 1

def test_dim_user_unique_ids():
    title = "Unique user_id in dim_user"
    try:
        df = pd.read_csv(os.path.join(warehouse_dir, 'dim_user.csv'))
        unique = df['user_id'].is_unique
        details = f"Rows: {len(df)}\nUnique user_ids: {df['user_id'].nunique()}"
        if unique:
            print_case(title, "PASS", details)
        else:
            print_case(title, "FAIL", details)
    except Exception as e:
        print_case(title, "ERROR", str(e))

def test_fact_user_ids_exist_in_dim():
    title = "All user_ids in fact_user_registration exist in dim_user"
    try:
        fact = pd.read_csv(os.path.join(warehouse_dir, 'fact_user_registration.csv'))
        dim = pd.read_csv(os.path.join(warehouse_dir, 'dim_user.csv'))
        missing = set(fact['user_id']) - set(dim['user_id'])
        details = f"Rows: {len(fact)}\nMissing user_ids: {len(missing)}"
        if not missing:
            print_case(title, "PASS", details)
        else:
            print_case(title, "FAIL", details)
    except Exception as e:
        print_case(title, "ERROR", str(e))

def test_no_missing_payments():
    title = "All payments have non-missing amounts"
    try:
        df = pd.read_csv(os.path.join(warehouse_dir, 'fact_user_payment.csv'))
        amount_col = None
        for col in df.columns:
            if 'amount' in col.lower() or 'cost' in col.lower():
                amount_col = col
                break
        if not amount_col:
            print_case(title, "INFO", "No amount/cost column found. Skipping.")
            return
        missing_count = df[amount_col].isnull().sum()
        details = f"Rows: {len(df)}\nMissing payment amounts: {missing_count}"
        if missing_count == 0:
            print_case(title, "PASS", details)
        else:
            print_case(title, "FAIL", details)
    except Exception as e:
        print_case(title, "ERROR", str(e))

def test_no_negative_payments():
    title = "No negative payment amounts"
    try:
        df = pd.read_csv(os.path.join(warehouse_dir, 'fact_user_payment.csv'))
        amount_col = None
        for col in df.columns:
            if 'amount' in col.lower() or 'cost' in col.lower():
                amount_col = col
                break
        if not amount_col:
            print_case(title, "INFO", "No amount/cost column found. Skipping.")
            return
        negatives = (df[amount_col] < 0).sum()
        details = f"Negative payment amounts: {negatives}"
        if negatives == 0:
            print_case(title, "PASS", details)
        else:
            print_case(title, "FAIL", details)
    except Exception as e:
        print_case(title, "ERROR", str(e))

def test_fact_user_plan_ids_exist_in_dim():
    title = "All plan_ids in fact_user_plan exist in dim_plan"
    try:
        fact = pd.read_csv(os.path.join(warehouse_dir, 'fact_user_plan.csv'))
        dim = pd.read_csv(os.path.join(warehouse_dir, 'dim_plan.csv'))
        missing = set(fact['plan_id']) - set(dim['plan_id'])
        details = f"Rows: {len(fact)}\nMissing plan_ids: {len(missing)}"
        if not missing:
            print_case(title, "PASS", details)
        else:
            print_case(title, "FAIL", details)
    except Exception as e:
        print_case(title, "ERROR", str(e))

def test_fact_play_session_platform_ids_exist_in_dim():
    title = "All platform_ids in fact_play_session exist in dim_platform"
    try:
        fact = pd.read_csv(os.path.join(warehouse_dir, 'fact_play_session.csv'))
        dim = pd.read_csv(os.path.join(warehouse_dir, 'dim_platform.csv'))
        missing = set(fact['platform_id']) - set(dim['platform_id'])
        details = f"Rows: {len(fact)}\nMissing platform_ids: {len(missing)}"
        if not missing:
            print_case(title, "PASS", details)
        else:
            print_case(title, "FAIL", details)
    except Exception as e:
        print_case(title, "ERROR", str(e))

def test_no_duplicate_play_sessions():
    title = "No duplicate play_session_id in fact_play_session"
    try:
        df = pd.read_csv(os.path.join(warehouse_dir, 'fact_play_session.csv'))
        duplicates = df.duplicated(subset=['play_session_id']).sum() if 'play_session_id' in df.columns else 0
        details = f"Duplicate play_session_id: {duplicates}"
        if duplicates == 0:
            print_case(title, "PASS", details)
        else:
            print_case(title, "FAIL", details)
    except Exception as e:
        print_case(title, "ERROR", str(e))

def test_no_missing_critical_fields():
    title = "No missing registration_date in dim_user"
    try:
        df = pd.read_csv(os.path.join(warehouse_dir, 'dim_user.csv'))
        missing = df['registration_date'].isnull().sum() if 'registration_date' in df.columns else 0
        details = f"Missing registration_date: {missing}"
        if missing == 0:
            print_case(title, "PASS", details)
        else:
            print_case(title, "FAIL", details)
    except Exception as e:
        print_case(title, "ERROR", str(e))

def test_valid_date_ranges():
    title = "All plan_start_date < plan_end_date in fact_user_plan"
    try:
        df = pd.read_csv(os.path.join(warehouse_dir, 'fact_user_plan.csv'))
        if 'plan_start_date' in df.columns and 'plan_end_date' in df.columns:
            invalid = (pd.to_datetime(df['plan_start_date']) > pd.to_datetime(df['plan_end_date'])).sum()
            details = f"Invalid plan date ranges: {invalid}"
            if invalid == 0:
                print_case(title, "PASS", details)
            else:
                print_case(title, "FAIL", details)
        else:
            print_case(title, "INFO", "plan_start_date or plan_end_date not found. Skipping.")
    except Exception as e:
        print_case(title, "ERROR", str(e))

def test_users_with_no_activity():
    title = "Users with no play sessions or payments"
    try:
        users = pd.read_csv(os.path.join(warehouse_dir, 'dim_user.csv'))
        sessions = pd.read_csv(os.path.join(warehouse_dir, 'fact_play_session.csv'))
        payments = pd.read_csv(os.path.join(warehouse_dir, 'fact_user_payment.csv'))
        session_users = set(sessions['user_id']) if 'user_id' in sessions.columns else set()
        payment_users = set(payments['user_id']) if 'user_id' in payments.columns else set()
        active_users = session_users.union(payment_users)
        inactive_users = set(users['user_id']) - active_users
        details = f"Users with no activity: {len(inactive_users)}"
        print_case(title, "INFO", details)
    except Exception as e:
        print_case(title, "ERROR", str(e))

def test_monthly_active_users():
    title = "Monthly active users (unique per month)"
    try:
        sessions = pd.read_csv(os.path.join(warehouse_dir, 'fact_play_session.csv'))
        if 'start_datetime' in sessions.columns:
            sessions['month'] = pd.to_datetime(sessions['start_datetime']).dt.to_period('M')
            monthly_active = sessions.groupby('month')['user_id'].nunique()
            # Format as a table for readability
            details = "\n" + monthly_active.reset_index().rename(columns={'user_id': 'active_users'}).to_string(index=False)
            print_case(title, "INFO", details)
        else:
            print_case(title, "INFO", "start_datetime not found. Skipping.")
    except Exception as e:
        print_case(title, "ERROR", str(e))

def test_unusually_long_or_short_sessions():
    title = "Sessions <1 min or >24 hours"
    try:
        sessions = pd.read_csv(os.path.join(warehouse_dir, 'fact_play_session.csv'))
        if 'start_datetime' in sessions.columns and 'end_datetime' in sessions.columns:
            sessions['start'] = pd.to_datetime(sessions['start_datetime'])
            sessions['end'] = pd.to_datetime(sessions['end_datetime'])
            sessions['duration_min'] = (sessions['end'] - sessions['start']).dt.total_seconds() / 60
            too_short = (sessions['duration_min'] < 1).sum()
            too_long = (sessions['duration_min'] > 24*60).sum()
            details = f"Sessions <1 min: {too_short}\nSessions >24 hours: {too_long}"
            print_case(title, "INFO", details)
        else:
            print_case(title, "INFO", "start_datetime or end_datetime not found. Skipping.")
    except Exception as e:
        print_case(title, "ERROR", str(e))

def main():
    print("\n" + "#"*60)
    print("#           ETL DATA QUALITY TESTS DASHBOARD           #")
    print("#" * 60)
    test_dim_user_unique_ids()
    test_fact_user_ids_exist_in_dim()
    test_no_missing_payments()
    test_no_negative_payments()
    test_fact_user_plan_ids_exist_in_dim()
    test_fact_play_session_platform_ids_exist_in_dim()
    test_no_duplicate_play_sessions()
    test_no_missing_critical_fields()
    test_valid_date_ranges()
    test_users_with_no_activity()
    test_monthly_active_users()
    test_unusually_long_or_short_sessions()
    print("#" * 60)
    print("#                END OF TESTS REPORT                   #")
    print("#" * 60 + "\n")

if __name__ == "__main__":
    main()