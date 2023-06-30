# 기계학습을 이용한 IoT Sensor 트래픽 플로우 분류
해당 리포지토리는 2023년도 봄학기 기계학습개론 최종 프로젝트로 진행한 **기계학습을 이용한 IoT Sensor 트래픽 플로우 분류**에 대한 전처리된 데이터셋, 소스코드와 결과를 담고 있습니다.

## 데이터셋에 대한 정보
본 프로젝트에서 사용한 데이터셋은 2022년도 IEEE Access Volume: 10에 게시된 *Edge-IIoTset: A New Comprehensive Realistic Cyber Security Dataset of IoT and IIoT Applications for Centralized and Federated Learning* 논문에서 제공하는 **Edge-IIoTset-dataset.zip**을 이용하였으며, 해당 데이터셋은 [IEEE-Dataport](http://ieee-dataport.org/8939 "Edge-IIoTset-dataset.zip")에서 접근 가능합니다.

전처리된 데이터셋은 리포지토리에 포함된 [dataset](https://github.com/t0ck/aics305-23s/tree/master/dataset "dataset")폴더에서 확인하실 수 있습니다.

## 파일 정보
파일의 정보는 다음과 같습니다.

파일 이름|파일 설명
---|---
test_case_01.py|해당 소스코드는 Temperature_and_Humidity.csv와 Water_Level.csv를 읽어와서 전처리 과정을 거친 후 dataset 폴더에 dataset_test_case_01.csv를 생성하고 DecisionTree 학습을 한 후 정확도를 출력합니다.
test_case_02.py|해당 소스코드는 Temperature_and_Humidity.csv와 Flame_Sensor.csv를 읽어와서 Digital_Output으로 묶고, Heart_Level.csv, Soil_Moisture.csv, Water_Level.csv, phValue.csv, Sound_Sensor.csv를 읽어와서 Analog_Output으로 묶는 전처리 과정을 거친 후 dataset 폴더에 dataset_test_case_02.csv를 생성하고 DecisionTree 학습을 한 후 정확도를 출력합니다.
test_case_03.py|해당 소스코드는 Temperature_and_Humidity.csv와 Flame_Sensor.csv를 읽어와서 Digital_Output으로 묶고, Heart_Level.csv, Soil_Moisture.csv, Water_Level.csv, phValue.csv, Sound_Sensor.csv를 읽어와서 Analog_Output으로 묶는 전처리 과정을 거친 후 dataset 폴더에 dataset_test_case_03-Digital.csv, dataset_test_case_03-Analog.csv를 생성하고 DecisionTree 학습을 한 후 정확도를 출력합니다.
test_case_04.py|해당 소스코드는 Temperature_and_Humidity.csv, Flame_Sensor.csv, Heart_Level.csv, Soil_Moisture.csv, Water_Level.csv, phValue.csv, Sound_Sensor.csv를 읽어와서 전처리 과정을 거친 후 dataset 폴더에 dataset_test_case_04.csv를 생성하고 DecisionTree 학습을 한 후 정확도를 출력합니다.
DecisionTree.ipynb|해당 주피터 노트북은 dataset에 존재하는 test_case_01.csv, test_case_02.csv, test_case_03-Digital.csv, test_case_03-Analog.csv, test_case_04.csv를 읽어와서 각각의 DecisionTree 학습을 진행하고 학습된 결과를 출력해줍니다.
RandomForest.ipynb|해당 주피터 노트북은 dataset에 존재하는 test_case_01.csv, test_case_02.csv, test_case_03-Digital.csv, test_case_03-Analog.csv, test_case_04.csv를 읽어와서 각각의 RandomForest 학습을 진행하고 학습된 결과를 출력해줍니다.
SVM.ipynb|해당 주피터 노트북은 dataset에 존재하는 test_case_01.csv, test_case_02.csv, test_case_03-Digital.csv, test_case_03-Analog.csv, test_case_04.csv를 읽어와서 각각의 SVM 학습을 진행하고 학습된 결과를 출력해줍니다.
XGBoost.ipynb|해당 주피터 노트북은 dataset에 존재하는 test_case_01.csv, test_case_02.csv, test_case_03-Digital.csv, test_case_03-Analog.csv, test_case_04.csv를 읽어와서 각각의 XGBoost 학습을 진행하고 학습된 결과를 출력해줍니다.
