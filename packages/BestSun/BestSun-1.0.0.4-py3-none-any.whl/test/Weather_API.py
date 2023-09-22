
# -*- coding: cp949 -*-

import requests
import datetime
import pandas as pd
import os


print("��ũ��Ʈ ����")

def download_file(file_url, save_path): #API �޾ƿͼ� ���� �ٿ�ε� �ϴ� �Լ�
    with open(save_path, 'wb') as f: #API �޾ƿͼ� ���� �ٿ�ε� �ϴ� �Լ�
        response = requests.get(file_url) #API �޾ƿͼ� ���� �ٿ�ε� �ϴ� �Լ�
        f.write(response.content) #API �޾ƿͼ� ���� �ٿ�ε� �ϴ� �Լ�
        


def download_file(file_url, save_path):
    try:
        # ���丮 ����
        if not os.path.exists(os.path.dirname(save_path)): # os.path.dirname�޼���� ���丮 �κ��� ������ �� os.path.exists()�޼���� ���丮 ������ Ȯ��
            os.makedirs(os.path.dirname(save_path)) # os.makedirs �޼���� ���丮 ����
        
        # ���� �ٿ�ε�
        with open(save_path, 'wb') as f:
            response = requests.get(file_url)
            if response.status_code == 200:
                f.write(response.content)
            else:
                print(f"�ٿ�ε� ����. HTTP ���� �ڵ�: {response.status_code}")
    except Exception as e:
        print(f"���� �߻�: {e}")





# ���� ��¥�� �ð� ��������
current_datetime = datetime.datetime.now() # datetime ���� ����ð� ��������
current_date_str = current_datetime.strftime('%Y%m%d') # ����ð��� ��-��-�� �������� ��ȯ�� current_date_str�� ����
previous_date_str = (current_datetime - datetime.timedelta(days=1)).strftime('%Y%m%d') # ����ð��� Ȱ���� �Ϸ� �� ��¥ �� ����. 

# URL�� ���� ��� �������� �����ϱ�
base_url = "https://apihub.kma.go.kr/api/typ01/url/kma_sfctm3.php" # url�� �Һ� ����
auth_key = "ghBQh0IXRimQUIdCFzYp4w" # url�� ���� ����- ����Ű �κ�


stn_value = "146" # url�� ���� ���� - ������ id �κ�

# RL�� tm1�� tm2 ���� ����
tm1_value = current_date_str + "0700" # url�� ���� ���� - ���� �ð� ����
tm2_value = current_date_str + "2000" # url�� ���� ���� - ���� �ð� ����

# �ϼ��� URL
url = f"{base_url}?tm1={tm1_value}&tm2={tm2_value}&stn={stn_value}&help=1&authKey={auth_key}" # url ����


# ���� ���

save_file_path = f"D:\hyeonseo\�¾籤���͸�����������\Battery_Charge_V3\Battery_Charge_V3\test\API_Dataset\Weather_{current_date_str}_file.csv" # output_���ó�¥.csv �������� ����


try:
   # ���� �ٿ�ε� �Լ� ȣ��
    download_file(url, save_file_path)
except Exception as e:
    print(f"���� �ٿ�ε� �� ���� �߻�: {e}")



response = requests.get(url)

# ���� ���� �ڵ� Ȯ��
print(response.status_code)

# ���� ���� ���
print(response.text)


print("��ũ��Ʈ ����")




# ���� �ٿ�ε� �Լ� ȣ��
download_file(url, save_file_path) # ���յ� url�� ������ ���ϰ�θ� Ȱ���� download_file �Լ� ������ ���������� api ������ ���ÿ� ����



def preprocess_weather_data(input_path, output_path): # ��ó���ϴ� �Լ� ����, save_file_path�� ���� �ҷ��ͼ� ��ó���� �� ouput_path�� ������ ��ȹ
    output_file = pd.read_csv(input_path, sep='\s+', comment='#', encoding='cp949') # input_path�� Ȱ���� ������ �ҷ�����, ������ �����ڷ� �ν��ϰ� #�κ��� �ּ�ó���� ������ ������
    
    with open(input_path, "r", encoding="cp949") as file: # �б���� ����
        lines = file.readlines() # ���� �� ��ҵ��� ����Ʈ �� ��ҷ� ��ȯ. �ε��� �� ��ҿ� �����Ͽ� ��ó���ϱ� ���� �ٲ��ִ� readlines()�޼��� Ȱ��

    column_index = [i for i, line in enumerate(lines) if line.startswith("# YYMMDDHHMI")][0] # ������ ���� list �� line���� ��ȸ�ϸ鼭 # YYMMDDHHMI�� �����ϴ� �κ��� ��� �ε����� ��ȯ�ϴ� enumerate����, �ุ ��ȯ(0)
    column_names = lines[column_index].split() # ���� �������� split�ؼ� �÷������� ��ȯ�� �� column_names�� ����
    column_names.remove('#') # ó���� ������� �÷� ���̿� ����� ������ �÷� ���̰� ���� ����. �̿� ����� ���� �� �÷� ���̸� ���������� �ٿ��� ���� �����ֱ�
    output_file.columns = column_names # ����� ���� �޼���� �÷��� ����

    df_weather_API = output_file[['YYMMDDHHMI', 'STN', 'WS', 'HM', 'CA', 'SS', 'SI', 'TS']] # ����� �÷��� �߷��� ���������� ���� �����
    df_weather_API['YYMMDDHHMI'] = df_weather_API['YYMMDDHHMI'].astype(str) # ��¥ �� �ð������� ������ YYMMDDHHM ���� �������� ���͸��ϱ� ����, ���� ���ڿ��� �ٲ���
    df_weather_API['datetime'] = pd.to_datetime(df_weather_API['YYMMDDHHMI']).dt.strftime('%Y-%m-%d %H:00') # datetime64ns �������� ����ȯ ���� ��, strftime�޼���� ��-��-��- ��:00 �������� ����������.
    df_weather_API['datetime'] = pd.to_datetime(df_weather_API['datetime']) # strftime �޼��带 Ȱ���ϸ� ���ڿ��� �ٽ� �ٲ�Ƿ�, datetime���� �纯ȯ
    df_weather_API = df_weather_API[(df_weather_API['datetime'].dt.hour >= 7) & (df_weather_API['datetime'].dt.hour <= 20)] # dt.hour���� ��-��-��-��:00 ���� '��' �κи� �̾Ƴ� ��, �̸� �������� 7�ÿ� 20�� ���̸� ���͸�
    df_weather_API.to_csv(output_path, index=False) # ��ó�� �Ϸ�. output_path�� ���� ��������



output_path = f"D:\hyeonseo\�¾籤���͸�����������\Battery_Charge_V3\Battery_Charge_V3\test\API_Dataset\Weather_{current_date_str}_file.csv" # �������� ���� ��� ����
# ��ó�� �Լ� ȣ��
preprocess_weather_data(save_file_path, output_path) 




