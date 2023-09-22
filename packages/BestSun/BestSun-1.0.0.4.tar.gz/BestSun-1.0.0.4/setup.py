from setuptools import setup, find_packages



setup(name='BestSun', 

version='1.0.0.4',

description='Test Package',

author='Hyeonseo',

author_email='whgustj0222@korea.ac.kr',
packages=['test'],


license='MIT', 

py_modules=['Forecast_API','Weather_API','get_battery_percentage'], 

python_requires='>=3.10',

install_requires=['pandas','scikit-learn','requests'], 
package_data={'BestSun': ['*.csv']},

)