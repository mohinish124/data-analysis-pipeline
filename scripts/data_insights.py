import pandas as pd

def load_warehouse_tables():
    fact_play_session = pd.read_csv('warehouse/fact_play_session.csv')
    dim_platform = pd.read_csv('warehouse/dim_platform.csv')
    fact_user_plan = pd.read_csv('warehouse/fact_user_plan.csv')
    dim_plan = pd.read_csv('warehouse/dim_plan.csv')
    fact_user_payment = pd.read_csv('warehouse/fact_user_payment.csv')
    return fact_play_session, dim_platform, fact_user_plan, dim_plan, fact_user_payment

def play_sessions_by_platform(fact_play_session, dim_platform):
    print("\n" + "="*50)
    print("INSIGHT 1: Play Sessions by Platform/Channel")
    print("="*50)
    platform_sessions = fact_play_session['platform_id'].value_counts().rename_axis('platform_id').reset_index(name='session_count')
    platform_sessions = platform_sessions.merge(dim_platform, on='platform_id', how='left')
    # Print as a nice table
    col_name = platform_sessions.columns[-1]
    print(f"\n{'Platform/Channel':<25} {'Session Count':>15}")
    print("-"*45)
    for _, row in platform_sessions.iterrows():
        print(f"{str(row[col_name]):<25} {row['session_count']:>15}")
    print()

def registered_users_by_plan(fact_user_plan, dim_plan):
    print("\n" + "="*50)
    print("INSIGHT 2: Registered Users by Plan/Payment Frequency")
    print("="*50)
    plan_counts = fact_user_plan['plan_id'].value_counts().rename_axis('plan_id').reset_index(name='user_count')
    plan_counts = plan_counts.merge(dim_plan[['plan_id', 'payment_frequency_code']], on='plan_id', how='left')
    print(f"\n{'Payment Frequency':<25} {'User Count':>15}")
    print("-"*45)
    for _, row in plan_counts.iterrows():
        print(f"{str(row['payment_frequency_code']):<25} {row['user_count']:>15}")
    print()

def gross_revenue(fact_user_payment):
    print("\n" + "="*50)
    print("INSIGHT 3: Gross Revenue Generated from the App")
    print("="*50)
    if 'cost_amount' in fact_user_payment.columns:
        gross_revenue = fact_user_payment['cost_amount'].sum()
        print(f"\nTotal Gross Revenue: ${gross_revenue:,.2f}\n")
    else:
        print("\nGross revenue: 'cost_amount' column not found in fact_user_payment.\n")

def main():
    print("\n" + "#"*60)
    print("#           GAME APP DATA INSIGHTS DASHBOARD           #")
    print("#" * 60)
    fact_play_session, dim_platform, fact_user_plan, dim_plan, fact_user_payment = load_warehouse_tables()
    play_sessions_by_platform(fact_play_session, dim_platform)
    registered_users_by_plan(fact_user_plan, dim_plan)
    gross_revenue(fact_user_payment)
    print("#" * 60)
    print("#                END OF INSIGHTS REPORT                #")
    print("#" * 60 + "\n")

if __name__ == "__main__":
    main()