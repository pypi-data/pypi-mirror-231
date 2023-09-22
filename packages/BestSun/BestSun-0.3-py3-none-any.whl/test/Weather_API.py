
# -*- coding: cp949 -*-

import requests
import datetime
import pandas as pd
import os


print("스크립트 시작")

def download_file(file_url, save_path): #API 받아와서 파일 다운로드 하는 함수
    with open(save_path, 'wb') as f: #API 받아와서 파일 다운로드 하는 함수
        response = requests.get(file_url) #API 받아와서 파일 다운로드 하는 함수
        f.write(response.content) #API 받아와서 파일 다운로드 하는 함수
        


def download_file(file_url, save_path):
    try:
        # 디렉토리 생성
        if not os.path.exists(os.path.dirname(save_path)): # os.path.dirname메서드로 디렉토리 부분을 추출한 후 os.path.exists()메서드로 디렉토리 유무를 확인
            os.makedirs(os.path.dirname(save_path)) # os.makedirs 메서드로 디렉토리 생성
        
        # 파일 다운로드
        with open(save_path, 'wb') as f:
            response = requests.get(file_url)
            if response.status_code == 200:
                f.write(response.content)
            else:
                print(f"다운로드 실패. HTTP 상태 코드: {response.status_code}")
    except Exception as e:
        print(f"오류 발생: {e}")





# 현재 날짜와 시간 가져오기
current_datetime = datetime.datetime.now() # datetime 모듈로 현재시간 가져오기
current_date_str = current_datetime.strftime('%Y%m%d') # 현재시간을 연-월-일 형식으로 변환해 current_date_str에 저장
previous_date_str = (current_datetime - datetime.timedelta(days=1)).strftime('%Y%m%d') # 현재시간을 활용해 하루 전 날짜 값 지정. 

# URL과 저장 경로 동적으로 생성하기
base_url = "https://apihub.kma.go.kr/api/typ01/url/kma_sfctm3.php" # url의 불변 포맷
auth_key = "ghBQh0IXRimQUIdCFzYp4w" # url의 가변 포맷- 인증키 부분


stn_value = "146" # url의 가변 포맷 - 관측소 id 부분

# RL의 tm1과 tm2 값을 설정
tm1_value = current_date_str + "0700" # url의 가변 포맷 - 관측 시간 지정
tm2_value = current_date_str + "2000" # url의 가변 포맷 - 관측 시간 지정

# 완성된 URL
url = f"{base_url}?tm1={tm1_value}&tm2={tm2_value}&stn={stn_value}&help=1&authKey={auth_key}" # url 조합


# 저장 경로

save_file_path = f"D:\hyeonseo\태양광배터리충전량조절\Battery_Charge_V3\Battery_Charge_V3\test\API_Dataset\Weather_{current_date_str}_file.csv" # output_오늘날짜.csv 형식으로 저장


try:
   # 파일 다운로드 함수 호출
    download_file(url, save_file_path)
except Exception as e:
    print(f"파일 다운로드 중 오류 발생: {e}")



response = requests.get(url)

# 응답 상태 코드 확인
print(response.status_code)

# 응답 내용 출력
print(response.text)


print("스크립트 종료")




# 파일 다운로드 함수 호출
download_file(url, save_file_path) # 조합된 url과 지정된 파일경로를 활용해 download_file 함수 돌려서 종관데이터 api 파일을 로컬에 저장



def preprocess_weather_data(input_path, output_path): # 전처리하는 함수 정의, save_file_path를 통해 불러와서 전처리한 후 ouput_path로 내보낼 계획
    output_file = pd.read_csv(input_path, sep='\s+', comment='#', encoding='cp949') # input_path를 활용해 파일을 불러오되, 공백은 구분자로 인식하고 #부분을 주석처리된 것으로 간주함
    
    with open(input_path, "r", encoding="cp949") as file: # 읽기모드로 열기
        lines = file.readlines() # 파일 내 요소들을 리스트 내 요소로 반환. 인덱싱 등 요소에 접근하여 전처리하기 쉽게 바꿔주는 readlines()메서드 활용

    column_index = [i for i, line in enumerate(lines) if line.startswith("# YYMMDDHHMI")][0] # 위에서 만든 list 내 line들을 순회하면서 # YYMMDDHHMI로 시작하는 부분의 행과 인덱스를 반환하는 enumerate에서, 행만 반환(0)
    column_names = lines[column_index].split() # 공백 기준으로 split해서 컬럼명으로 반환한 후 column_names에 저장
    column_names.remove('#') # 처음에 만들어진 컬럼 길이와 사용자 정의한 컬럼 길이가 맞지 않음. 이에 사용자 정의 측 컬럼 길이를 임의적으로 줄여서 길이 맞춰주기
    output_file.columns = column_names # 사용자 정의 메서드로 컬럼명 설정

    df_weather_API = output_file[['YYMMDDHHMI', 'STN', 'WS', 'HM', 'CA', 'SS', 'SI', 'TS']] # 사용할 컬럼만 추려서 종관데이터 파일 만들기
    df_weather_API['YYMMDDHHMI'] = df_weather_API['YYMMDDHHMI'].astype(str) # 날짜 및 시간정보를 가지는 YYMMDDHHM 열을 기준으로 필터링하기 위해, 먼저 문자열로 바꿔줌
    df_weather_API['datetime'] = pd.to_datetime(df_weather_API['YYMMDDHHMI']).dt.strftime('%Y-%m-%d %H:00') # datetime64ns 형식으로 형변환 해준 후, strftime메서드로 연-월-일- 시:00 형식으로 포맷팅해줌.
    df_weather_API['datetime'] = pd.to_datetime(df_weather_API['datetime']) # strftime 메서드를 활용하면 문자열로 다시 바뀌므로, datetime으로 재변환
    df_weather_API = df_weather_API[(df_weather_API['datetime'].dt.hour >= 7) & (df_weather_API['datetime'].dt.hour <= 20)] # dt.hour으로 연-월-일-시:00 에서 '시' 부분만 뽑아낸 후, 이를 기준으로 7시와 20시 사이만 필터링
    df_weather_API.to_csv(output_path, index=False) # 전처리 완료. output_path로 파일 내보내기



output_path = f"D:\hyeonseo\태양광배터리충전량조절\Battery_Charge_V3\Battery_Charge_V3\test\API_Dataset\Weather_{current_date_str}_file.csv" # 내보내는 파일 경로 지정
# 전처리 함수 호출
preprocess_weather_data(save_file_path, output_path) 




