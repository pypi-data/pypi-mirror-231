


#     with open("D:\hyeonseo\태양광배터리충전량조절\API_Renewal.py\get_battery_percentage.py", 'r', encoding='utf-8') as f:
#         content = f.read()
#     print("파일 읽기 성공!")
# except UnicodeDecodeError as e:
#     print(f"오류 발생: {e}")


# #인코딩 방식 추정하기
# import chardet

# #파일 이름 및 경로를 지정합니다.
# file_path = "D:\hyeonseo\태양광배터리충전량조절\API_Renewal.py\get_battery_percentage.py"

# try:
#     #파일을 바이너리 모드로 열고 데이터를 읽어 변수에 저장합니다.
#     with open(file_path, 'rb') as file:
#         file_content = file.read()

#     #파일 내용의 인코딩을 감지합니다.
#     result = chardet.detect(file_content)
#     encoding = result['encoding']
#     confidence = result['confidence']

#     print(f"파일의 인코딩: {encoding}, 신뢰도: {confidence}")
# except FileNotFoundError:
#     print(f"파일 '{file_path}'를 찾을 수 없습니다.")
# except Exception as e:
#     print(f"파일을 읽는 동안 오류가 발생했습니다: {e}")

import io
import pandas as pd
import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 현재 날짜와 시간 가져오기
current_datetime = datetime.datetime.now() # datetime 모듈로 현재시간 가져오기
current_date_str = current_datetime.strftime('%Y%m%d') # 현재시간을 연-월-일 형식으로 변환해 current_date_str에 저장
previous_date_str = (current_datetime - datetime.timedelta(days=1)).strftime('%Y%m%d') # 현재시간을 활용해 9일 전 날짜 값 지정. 이는 과거예보(9일 전~2일 전) 활용하기 위함
later_date_str = (current_datetime + datetime.timedelta(days=1)).strftime('%Y%m%d') # 현재시간을 활용해 9일 전 날짜 값 지정. 이는 과거예보(9일 전~2일 전) 활용하기 위함


# Commented out IPython magic to ensure Python compatibility.
# %%writefile battery_charge_module.py


# 현재 날짜와 시간 가져오기
current_datetime = datetime.datetime.now() # datetime 모듈로 현재시간 가져오기
current_date_str = current_datetime.strftime('%Y%m%d') # 현재시간을 연-월-일 형식으로 변환해 current_date_str에 저장
previous_date_str = (current_datetime - datetime.timedelta(days=1)).strftime('%Y%m%d') # 현재시간을 활용해 9일 전 날짜 값 지정. 이는 과거예보(9일 전~2일 전) 활용하기 위함
later_date_str = (current_datetime + datetime.timedelta(days=1)).strftime('%Y%m%d') # 현재시간을 활용해 9일 전 날짜 값 지정. 이는 과거예보(9일 전~2일 전) 활용하기 위함




# 변수 불러오기

observation_data_path = f"D:\hyeonseo\태양광배터리충전량조절\API_Dataset\output_Weather_{current_date_str}.csv"

forecast_data_path = f"D:\hyeonseo\태양광배터리충전량조절\API_Dataset\output_forecast_{current_date_str}.csv"

training_data_path = "D:\hyeonseo\태양광배터리충전량조절\API_Renewal.py\df_sky_weather_sunenergy_V7.csv"


try:
 df_Weather_API = pd.read_csv(observation_data_path, encoding='cp949')
 print("종관데이터 읽기 성공!")
except Exception as e:
 print(f"종관데이터에서 오류 발생: {e}")

try:
 df_forecast_API = pd.read_csv(forecast_data_path, encoding='utf-8')
 print("예보데이터 읽기 성공!")
except Exception as e:
 print(f"예보데이터에서 오류 발생: {e}")

try:
 training_data_df = pd.read_csv(training_data_path, encoding='utf-8')
 print("학습데이터 읽기 성공!")
except Exception as e:
 print(f"학습데이터에서 오류 발생: {e}")

 print(df_Weather_API.head())




def get_final_battery_charge(training_data_path, forecast_data_path, observation_data_path, prediction_date):
 

   # # 2. 데이터 전처리 및 모델 학습을 위한 함수들 정의
   # def predict_sunenergy_for_date(date_str, model, data, features):
       
   #     print(type(data))

   #     data['datetime'] = pd.to_datetime(data['datetime'])
   #     input_data = data[data['datetime'].dt.date == pd.to_datetime(date_str).date()]

   #     if input_data.empty:
   #         raise ValueError(f"no data available for the date: {date_str}")
   #     input_features = input_data[features]
   #     predicted_values = model.predict(input_features)
   #     return predicted_values.tolist()



   # 2. 데이터 전처리 및 모델 학습을 위한 함수들 정의
   def predict_sunenergy_for_date(date_str, model, data, features):
       
       print(type(data))

       if data.empty:
           raise ValueError(f"no data available for the date: {date_str}")
       input_features = data[features]
       predicted_values = model.predict(input_features)
       return predicted_values.tolist()




 
   # def get_mode_of_sky(filename):
   #     df = pd.read_csv(filename)
   #     return int(df['SKY'].mode()[0][-2:])
   

 
   def get_mode_of_sky(data):
       
       return int(data['SKY'].mode()[0][-2:])
 
   # def get_season_final(date_str, filename):
   #     df = pd.read_csv(filename)
 
   #     # 해당 날짜에 대한 'season' 컬럼의 값 반환
   #     season_data = df[df['datetime'].str.contains(date_str)]
   #     if not season_data.empty:
   #         return season_data['season'].iloc[0]
   #     else:
   #         raise ValueError(f"no season data available for the date: {date_str}")
       


   # def get_season_final(date_str, data):
       
   #     # 해당 날짜에 대한 'season' 컬럼의 값 반환
   #     season_data = data[data['datetime'].str.contains(date_str)]
   #     if not season_data.empty:
   #         return season_data['season'].iloc[0]
   #     else:
   #         raise ValueError(f"no season data available for the date: {date_str}")

 
   def get_season_final(data):
       
       # 해당 날짜에 대한 'season' 컬럼의 값 반환
     
       if not data.empty:
           return data['season'].iloc[0]
       else:
           raise ValueError(f"no season data available for the date")




 
   def decide_base_charge(sunenergy):
       if 0 <= sunenergy < 500:
           return 95
       elif 500 <= sunenergy < 1000:
           return 90
       elif 1000 <= sunenergy < 1500:
           return 85
       elif 1500 <= sunenergy < 2000:
           return 80
       elif 2000 <= sunenergy < 3000:
           return 70
       elif 3000 <= sunenergy < 4000:
           return 60
       elif 4000 <= sunenergy:
           return 50
 
   def decide_final_charge(sunenergy, sky_value, season):
       base_charge = decide_base_charge(sunenergy)
       additional_charge = 0
       if season in ['spring', 'summer', 'fall']:
           if sky_value <= 2:
               additional_charge = 0
           elif sky_value >= 3:
               additional_charge = 5
       elif season == 'winter':
           if sky_value <= 2:
               additional_charge = 5
           elif sky_value >= 3:
               additional_charge = 10
       final_charge = base_charge + additional_charge
       return min(100, max(50, final_charge))
 
 
 
   # 일별 기준으로 하루 전의 독립변수를 shift
   columns_to_shift = ['습도(%)', '전운량(10분위)', '일조(hr)', '일사(MJ/m2)', '지면온도(°C)', '풍속(m/s)']
 
   for col in columns_to_shift:
       shifted_col_name = col + "_shifted"
       training_data_df[shifted_col_name] = training_data_df[col].shift(14)
 
   x = training_data_df[['습도(%)_shifted', '전운량(10분위)_shifted','일조(hr)_shifted', '일사(MJ/m2)_shifted', '지면온도(°C)_shifted', '풍속(m/s)_shifted' ]]
 
 
   # 3. 태양광 발전량 예측 모델 학습
   features_mapping = {'풍속(m/s)_shifted': 'WS', '습도(%)_shifted': 'HM', '일조(hr)_shifted': 'SS', '일사(MJ/m2)_shifted': 'SI', '전운량(10분위)_shifted': 'CA', '지면온도(°C)_shifted': 'TS'}
   target = ' 태양광 발전량(MWh) '
 
 
 
   training_data_df_cleaned = training_data_df.dropna(subset=list(features_mapping.keys()) + [target])
   x = training_data_df_cleaned[list(features_mapping.keys())]
   y = training_data_df_cleaned[target]
   x = x.rename(columns=features_mapping)
   x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
   model = RandomForestRegressor(n_estimators=100, random_state=42)
   model.fit(x_train, y_train)


   # training_data_df_cleaned = training_data_df.dropna(subset=list(features_mapping.values()) + [target])
   # x = training_data_df_cleaned[list(features_mapping.values())]
   # y = training_data_df_cleaned[target]
   # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
   # model = RandomForestRegressor(n_estimators=100, random_state=42)
   # model.fit(x_train, y_train)


 
   # 4. "later_date_str"의 태양광 발전량 예측
   predicted_values_later_date_str = predict_sunenergy_for_date(current_date_str, model, df_Weather_API, list(features_mapping.values()))
   daily_predicted_value_later_date_str= sum(predicted_values_later_date_str)
   print(predicted_values_later_date_str)
   print(daily_predicted_value_later_date_str)
 
   # 5. "later_date_str"의 하늘 상태 가져오기
   sky_value_for_later_date_str = get_mode_of_sky(df_forecast_API)
   print(sky_value_for_later_date_str)
   # 6. "later_date_str"의 계절 정보  가져오기
   season_for_later_date_str= get_season_final(df_forecast_API)
   season_for_later_date_str
   print(season_for_later_date_str)
 
   # 7. 최종 배터리 충전량 계산
   battery_charge = decide_final_charge(daily_predicted_value_later_date_str, sky_value_for_later_date_str, season_for_later_date_str)
   print(battery_charge)
 
 
 
final_charge = get_final_battery_charge("D:\hyeonseo\태양광배터리충전량조절\Battery_Charge_V3\Battery_Charge_V3\df_sky_weather_sunenergy_V7.csv", f"D:\hyeonseo\태양광배터리충전량조절\Battery_Charge_V3\Battery_Charge_V3\API_Dataset\forecast_{current_date_str}.csv" , f"D:\hyeonseo\태양광배터리충전량조절\Battery_Charge_V3\Battery_Charge_V3\API_Dataset\Weather_{current_date_str}_file.csv", 'later_date_str')
print(final_charge)

