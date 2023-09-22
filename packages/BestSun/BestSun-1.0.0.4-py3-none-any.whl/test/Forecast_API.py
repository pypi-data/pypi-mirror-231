
# -*- coding: cp949 -*-


from tkinter.font import names
import requests
import datetime
import pandas as pd

print("스크립트시작")

def download_file(file_url, save_path): #API 받아와서 파일 다운로드 하는 함수
    with open(save_path, 'wb') as f: #API 받아와서 파일 다운로드 하는 함수
        response = requests.get(file_url) #API 받아와서 파일 다운로드 하는 함수
        f.write(response.content) #API 받아와서 파일 다운로드 하는 함수

# 현재 날짜와 시간 가져오기
current_datetime = datetime.datetime.now() # datetime 모듈로 현재시간 가져오기
current_date_str = current_datetime.strftime('%Y%m%d') # 현재시간을 연-월-일 형식으로 변환해 current_date_str에 저장
previous9_date_str = (current_datetime - datetime.timedelta(days=9)).strftime('%Y%m%d') # 현재시간을 활용해 9일 전 날짜 값 지정. 이는 과거예보(9일 전~2일 전) 활용하기 위함
previous2_date_str = (current_datetime - datetime.timedelta(days=2)).strftime('%Y%m%d') # 현재시간을 활용해 2일 전 날짜 값 지정. 이는 과거예보(9일 전~2일 전) 활용하기 위함
later_date_str = (current_datetime + datetime.timedelta(days=1)).strftime('%Y%m%d') #  현재시간을 활용해 하루 뒤 날짜 값 지정. 이는 미래예보(1일 후~2일 후) 활용하기 위함
later2_date_str = (current_datetime + datetime.timedelta(days=2)).strftime('%Y%m%d') #  현재시간을 활용해 하루 뒤 날짜 값 지정. 이는 미래예보(1일 후~2일 후) 활용하기 위함




# URL과 저장 경로 동적으로 생성하기




base_url = "https://apihub.kma.go.kr/api/typ01/url/fct_afs_wl.php" # url의 불변 포맷
auth_key = "ghBQh0IXRimQUIdCFzYp4w" # url의 가변 포맷, 인증키 부분
stn_value = "146" # url의 가변 포맷 - 관측소 id 부분

# URL의 tm1과 tm2 값을 설정
tm1_value = previous9_date_str + "00" # url의 가변 포맷 - 관측 시간 지정
tm2_value = previous2_date_str + "00" # url의 가변 포맷 - 관측 시간 지정

# 완성된 URL
url = f"{base_url}?reg=&stn={stn_value}&tmfc1={tm1_value}&tmfc2={tm2_value}&mode=0&disp=0&help=1&authKey={auth_key}"  # 호출 URL 조합 

# 저장 경로
save_file_path = f"D:\hyeonseo\태양광배터리충전량조절\Battery_Charge_V3\Battery_Charge_V3\test\API_Dataset\API_Dataset\forecast_{current_date_str}.csv" # output_오늘날짜.csv 형식으로 저장

# 파일 다운로드 함수 호출
download_file(url, save_file_path)  # 조합된 url과 지정된 파일경로를 활용해 download_file 함수 돌려서 예보데이터 api 파일 구글 드라이브에 저장



response = requests.get(url)

# 응답 상태 코드 확인
print(response.status_code)

# 응답 내용 출력
print(response.text)


print("스크립트 종료")


def preprocess_forecast_data(input_path, output_path): # 파일 전처리 하는 함수 정의. 불러올 때 파일경로, 내보낼 때 파일경로를 인자로 사용함
 
    output_file = pd.read_csv(input_path, sep='\s+', comment='#', encoding='cp949') # 불러올 떄 파일, 공백을 구분자로 인식, #를 주석처리하고, cp949 인코딩 방식 사용



# 컬럼명을 추출
    with open(input_path, "r", encoding="cp949") as file: # 먼저 파일을 읽기 전용모드로 열기
     lines = file.readlines() # 파일 내 요소들을 리스트 내 요소로 반환. 인덱싱 등 요소에 접근하여 전처리하기 쉽게 바꿔주는 readlines()메서드 활용


    # "reg_id"로 시작하는 라인을 찾아 컬럼명으로 사용
    column_index = [i for i, line in enumerate(lines) if line.startswith("# REG_ID")][0] # 위에서 만든 list 내 line들을 순회하면서 #reg_id로 시작하는 부분의 행과 인덱스를 반환하는 enumerate에서, 행만 반환(0)
    column_names = lines[column_index].split() # 공백 기준으로 split해서 컬럼명으로 반환한 후 column_names에 저장


    # '#' 컬럼 제거
    column_names.remove('#') # 처음에 만들어진 컬럼 길이와 사용자 정의한 컬럼 길이가 맞지 않음. 이에 사용자 정의 측 컬럼 길이를 임의적으로 줄여서 길이 맞춰주기
    
   


    # 데이터 프레임의 컬럼명을 설정
    output_file.columns = column_names # 사용자 정의 메서드로 컬럼명 설정

    output_file = output_file[output_file['STN'] == 146] # stn 컬럼의 값이 146인 행만 남기기



    output_file['TM_EF'] = output_file['TM_EF'].astype(str) # TM_EF 컬럼을 문자열로 변환. 이는 TM_EF (예보발효시간)의 값으로 필터링을 하기 위함.

    output_file['datetime'] = pd.to_datetime(output_file['TM_EF']) #  TM_EF 컬럼을 datetime형식으로 변환


    # t+1시점과 t+2시점이 남도록 필터링해야 함.
    filtered_output_file = output_file[
        (output_file['datetime'].dt.date == pd.to_datetime(later_date_str).date()) | # T+1시점 00시, T+1시점 12시의 예보상태가 포함된 later_date_str 값 필터링
        (output_file['datetime'].dt.date == pd.to_datetime(later2_date_str).date()) # T+2시점 00시의 예보상태가 포함된 later2_date_str 값 필터링. 이는 T+1시점 12시~ T+2시점 00시 사이의 예보상태를 보기 위함임
    ]



    def season_searching(month): # 계절정보 정의하는 함수.

      if 3<= month <=5:
        return 'spring'
      elif 6<= month <= 8:
        return 'summer'
      elif 9<= month <=11:
        return 'fall'
      else:
        return 'winter'

    filtered_output_file['season'] = filtered_output_file['datetime'].dt.month.apply(season_searching) # apply 메서드를 통해 season_searching 함수 적용




    filtered_output_file.to_csv(output_path, index = False) # 전처리 완료. 파일 내보내기.



 
output_path = f"D:\hyeonseo\태양광배터리충전량조절\Battery_Charge_V3\Battery_Charge_V3\test\API_Dataset\API_Dataset\forecast_{current_date_str}.csv"
# preprocess_forecast_data 함수 사용
preprocess_forecast_data(save_file_path, output_path)

print("스크립트종료")
