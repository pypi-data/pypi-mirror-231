
# -*- coding: cp949 -*-


from tkinter.font import names
import requests
import datetime
import pandas as pd

print("��ũ��Ʈ����")

def download_file(file_url, save_path): #API �޾ƿͼ� ���� �ٿ�ε� �ϴ� �Լ�
    with open(save_path, 'wb') as f: #API �޾ƿͼ� ���� �ٿ�ε� �ϴ� �Լ�
        response = requests.get(file_url) #API �޾ƿͼ� ���� �ٿ�ε� �ϴ� �Լ�
        f.write(response.content) #API �޾ƿͼ� ���� �ٿ�ε� �ϴ� �Լ�

# ���� ��¥�� �ð� ��������
current_datetime = datetime.datetime.now() # datetime ���� ����ð� ��������
current_date_str = current_datetime.strftime('%Y%m%d') # ����ð��� ��-��-�� �������� ��ȯ�� current_date_str�� ����
previous9_date_str = (current_datetime - datetime.timedelta(days=9)).strftime('%Y%m%d') # ����ð��� Ȱ���� 9�� �� ��¥ �� ����. �̴� ���ſ���(9�� ��~2�� ��) Ȱ���ϱ� ����
previous2_date_str = (current_datetime - datetime.timedelta(days=2)).strftime('%Y%m%d') # ����ð��� Ȱ���� 2�� �� ��¥ �� ����. �̴� ���ſ���(9�� ��~2�� ��) Ȱ���ϱ� ����
later_date_str = (current_datetime + datetime.timedelta(days=1)).strftime('%Y%m%d') #  ����ð��� Ȱ���� �Ϸ� �� ��¥ �� ����. �̴� �̷�����(1�� ��~2�� ��) Ȱ���ϱ� ����
later2_date_str = (current_datetime + datetime.timedelta(days=2)).strftime('%Y%m%d') #  ����ð��� Ȱ���� �Ϸ� �� ��¥ �� ����. �̴� �̷�����(1�� ��~2�� ��) Ȱ���ϱ� ����




# URL�� ���� ��� �������� �����ϱ�




base_url = "https://apihub.kma.go.kr/api/typ01/url/fct_afs_wl.php" # url�� �Һ� ����
auth_key = "ghBQh0IXRimQUIdCFzYp4w" # url�� ���� ����, ����Ű �κ�
stn_value = "146" # url�� ���� ���� - ������ id �κ�

# URL�� tm1�� tm2 ���� ����
tm1_value = previous9_date_str + "00" # url�� ���� ���� - ���� �ð� ����
tm2_value = previous2_date_str + "00" # url�� ���� ���� - ���� �ð� ����

# �ϼ��� URL
url = f"{base_url}?reg=&stn={stn_value}&tmfc1={tm1_value}&tmfc2={tm2_value}&mode=0&disp=0&help=1&authKey={auth_key}"  # ȣ�� URL ���� 

# ���� ���
save_file_path = f"D:\hyeonseo\�¾籤���͸�����������\Battery_Charge_V3\Battery_Charge_V3\test\API_Dataset\API_Dataset\forecast_{current_date_str}.csv" # output_���ó�¥.csv �������� ����

# ���� �ٿ�ε� �Լ� ȣ��
download_file(url, save_file_path)  # ���յ� url�� ������ ���ϰ�θ� Ȱ���� download_file �Լ� ������ ���������� api ���� ���� ����̺꿡 ����



response = requests.get(url)

# ���� ���� �ڵ� Ȯ��
print(response.status_code)

# ���� ���� ���
print(response.text)


print("��ũ��Ʈ ����")


def preprocess_forecast_data(input_path, output_path): # ���� ��ó�� �ϴ� �Լ� ����. �ҷ��� �� ���ϰ��, ������ �� ���ϰ�θ� ���ڷ� �����
 
    output_file = pd.read_csv(input_path, sep='\s+', comment='#', encoding='cp949') # �ҷ��� �� ����, ������ �����ڷ� �ν�, #�� �ּ�ó���ϰ�, cp949 ���ڵ� ��� ���



# �÷����� ����
    with open(input_path, "r", encoding="cp949") as file: # ���� ������ �б� ������� ����
     lines = file.readlines() # ���� �� ��ҵ��� ����Ʈ �� ��ҷ� ��ȯ. �ε��� �� ��ҿ� �����Ͽ� ��ó���ϱ� ���� �ٲ��ִ� readlines()�޼��� Ȱ��


    # "reg_id"�� �����ϴ� ������ ã�� �÷������� ���
    column_index = [i for i, line in enumerate(lines) if line.startswith("# REG_ID")][0] # ������ ���� list �� line���� ��ȸ�ϸ鼭 #reg_id�� �����ϴ� �κ��� ��� �ε����� ��ȯ�ϴ� enumerate����, �ุ ��ȯ(0)
    column_names = lines[column_index].split() # ���� �������� split�ؼ� �÷������� ��ȯ�� �� column_names�� ����


    # '#' �÷� ����
    column_names.remove('#') # ó���� ������� �÷� ���̿� ����� ������ �÷� ���̰� ���� ����. �̿� ����� ���� �� �÷� ���̸� ���������� �ٿ��� ���� �����ֱ�
    
   


    # ������ �������� �÷����� ����
    output_file.columns = column_names # ����� ���� �޼���� �÷��� ����

    output_file = output_file[output_file['STN'] == 146] # stn �÷��� ���� 146�� �ุ �����



    output_file['TM_EF'] = output_file['TM_EF'].astype(str) # TM_EF �÷��� ���ڿ��� ��ȯ. �̴� TM_EF (������ȿ�ð�)�� ������ ���͸��� �ϱ� ����.

    output_file['datetime'] = pd.to_datetime(output_file['TM_EF']) #  TM_EF �÷��� datetime�������� ��ȯ


    # t+1������ t+2������ ������ ���͸��ؾ� ��.
    filtered_output_file = output_file[
        (output_file['datetime'].dt.date == pd.to_datetime(later_date_str).date()) | # T+1���� 00��, T+1���� 12���� �������°� ���Ե� later_date_str �� ���͸�
        (output_file['datetime'].dt.date == pd.to_datetime(later2_date_str).date()) # T+2���� 00���� �������°� ���Ե� later2_date_str �� ���͸�. �̴� T+1���� 12��~ T+2���� 00�� ������ �������¸� ���� ������
    ]



    def season_searching(month): # �������� �����ϴ� �Լ�.

      if 3<= month <=5:
        return 'spring'
      elif 6<= month <= 8:
        return 'summer'
      elif 9<= month <=11:
        return 'fall'
      else:
        return 'winter'

    filtered_output_file['season'] = filtered_output_file['datetime'].dt.month.apply(season_searching) # apply �޼��带 ���� season_searching �Լ� ����




    filtered_output_file.to_csv(output_path, index = False) # ��ó�� �Ϸ�. ���� ��������.



 
output_path = f"D:\hyeonseo\�¾籤���͸�����������\Battery_Charge_V3\Battery_Charge_V3\test\API_Dataset\API_Dataset\forecast_{current_date_str}.csv"
# preprocess_forecast_data �Լ� ���
preprocess_forecast_data(save_file_path, output_path)

print("��ũ��Ʈ����")
