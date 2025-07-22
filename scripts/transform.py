import pandas as pd

def transform_data(data):
    # Dimensions
    dim_user = data['user'].drop_duplicates()
    dim_channel = data['channel_code'].drop_duplicates()
    # Find merge key for plan and plan_payment_frequency
    merge_key = next((col for col in data['plan'].columns if col in data['plan_payment_frequency'].columns), None)
    if not merge_key:
        raise KeyError("No common column found to merge plan and plan_payment_frequency.")
    dim_plan = data['plan'].merge(data['plan_payment_frequency'], on=merge_key, how='left').drop_duplicates()
    dim_status = data['status_code'].drop_duplicates()
    platform_col = 'channel_code'
    dim_platform = data['user_play_session'][[platform_col]].drop_duplicates().reset_index(drop=True)
    dim_platform['platform_id'] = dim_platform.index + 1

    # Facts
    fact_user_registration = data['user_registration'].drop_duplicates()
    fact_user_plan = data['user_plan'].drop_duplicates()
    fact_user_payment = data['user_payment_detail'].merge(
        data['user_plan'][['payment_detail_id', 'plan_id']],
        on='payment_detail_id', how='left'
    ).merge(
        data['plan'][['plan_id', 'cost_amount']],
        on='plan_id', how='left'
    )
    fact_play_session = data['user_play_session'].merge(dim_platform, on=platform_col, how='left')

    return {
        'dim_user': dim_user,
        'dim_channel': dim_channel,
        'dim_plan': dim_plan,
        'dim_status': dim_status,
        'dim_platform': dim_platform,
        'fact_user_registration': fact_user_registration,
        'fact_user_plan': fact_user_plan,
        'fact_user_payment': fact_user_payment,
        'fact_play_session': fact_play_session
    }