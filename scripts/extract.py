import pandas as pd
import os

def extract_data(data_dir):
    data = {}
    data['user'] = pd.read_csv(os.path.join(data_dir, 'user.csv'))
    data['channel_code'] = pd.read_csv(os.path.join(data_dir, 'channel_code.csv'))
    data['plan_payment_frequency'] = pd.read_csv(os.path.join(data_dir, 'plan_payment_frequency.csv'))
    data['plan'] = pd.read_csv(os.path.join(data_dir, 'plan.csv'))
    data['status_code'] = pd.read_csv(os.path.join(data_dir, 'status_code.csv'))
    data['user_registration'] = pd.read_csv(os.path.join(data_dir, 'user_registration.csv'))
    data['user_plan'] = pd.read_csv(os.path.join(data_dir, 'user_plan.csv'))
    data['user_payment_detail'] = pd.read_csv(os.path.join(data_dir, 'user_payment_detail.csv'))
    data['user_play_session'] = pd.read_csv(os.path.join(data_dir, 'user_play_session.csv'))
    return data