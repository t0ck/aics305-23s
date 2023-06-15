# <-- import library -->
import pandas as pd
import numpy as np
import datetime
from tqdm import tqdm
import os

# <-- Machine-learning library -->
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# <-- config -->
_TODAY = datetime.datetime.today().date()
dataset_dic = './dataset/'
pre_dataset = './dataset_test_case_02'
IoT_list = ['Heart_Rate', 'Soil_Moisture', 'Sound_Sensor', 'Temperature_and_Humidity', 'Water_Level', 'phValue']
test_list = ['Digital_Output', 'Analog_Output']
features = ['src.port', 'flow_duration', 'mqtt_duration', 'mqtt_connection_duration', 'mqtt_connection_ack_duration', 'mqtt_disconnection_duration', 'IoT_label', 'test_label']

# <-- data pre-processing -->
if os.path.isfile(dataset_dic + pre_dataset + '.csv'):
    df = pd.read_csv(dataset_dic + pre_dataset + '.csv')
else:
    new_list = [] #Using it for making DataFrame
    for IoT in tqdm(IoT_list, desc='Data Pre-Processing', position=0): #Progress bar - 1
        csv_df = pd.read_csv(dataset_dic + IoT + '.csv', low_memory=False)
        #Initializing variables
        session_dict = {}
        for index, row in tqdm(csv_df.iterrows(), total=len(csv_df), desc=('IoT : ' + IoT), position=1, leave=False): #Progress bar - 2
            if row['tcp.connection.syn'] == 1: #Flow start point
                #Record start
                session_dict = { int(row['tcp.srcport']) : [ int(pd.to_timedelta(row['frame.time']).total_seconds() * 10**6), ] }
            if row['mqtt.msgtype'] == 1: #MQTT Connection
                #Record time
                if int(row['tcp.srcport']) in session_dict:
                    session_dict[int(row['tcp.srcport'])].append(int(pd.to_timedelta(row['frame.time']).total_seconds() * 10**6), )
            if row['mqtt.msgtype'] == 2: #MQTT Connection Ack
                #Record time
                if int(row['tcp.dstport']) in session_dict:
                    session_dict[int(row['tcp.dstport'])].append(int(pd.to_timedelta(row['frame.time']).total_seconds() * 10**6), )
            if row['mqtt.msgtype'] == 14: #MQTT Disconnection
                #Record time
                if int(row['tcp.srcport']) in session_dict:
                    session_dict[int(row['tcp.srcport'])].append(int(pd.to_timedelta(row['frame.time']).total_seconds() * 10**6), )
            if row['tcp.connection.fin'] == 1 and row['mqtt.msgtype'] != 14:
                #Record end
                if int(int(row['tcp.dstport'])) in session_dict:
                    if len(session_dict[int(row['tcp.dstport'])]) == 4:
                        session_dict[int(row['tcp.dstport'])].append(int(pd.to_timedelta(row['frame.time']).total_seconds() * 10**6), )
                        flow_duration = session_dict[int(row['tcp.dstport'])][4] - session_dict[int(row['tcp.dstport'])][0]
                        mqtt_duration = session_dict[int(row['tcp.dstport'])][3] - session_dict[int(row['tcp.dstport'])][1]
                        mqtt_connection_duration = session_dict[int(row['tcp.dstport'])][1] - session_dict[int(row['tcp.dstport'])][0]
                        mqtt_connection_ack_duration = session_dict[int(row['tcp.dstport'])][2] - session_dict[int(row['tcp.dstport'])][1]
                        mqtt_disconnection_duration = session_dict[int(row['tcp.dstport'])][3] - session_dict[int(row['tcp.dstport'])][2]
                        if IoT in ['Temperature_and_Humidity', 'Flame_Sensor']:
                            test_label = test_list[0]
                        else:
                            test_label = test_list[1]
                        new_list.append([int(row['tcp.dstport']), flow_duration, mqtt_duration, mqtt_connection_duration, mqtt_connection_ack_duration, mqtt_disconnection_duration, IoT, test_label])
    df = pd.DataFrame(new_list, columns=features)
    df.to_csv(dataset_dic + pre_dataset + '-' + str(_TODAY) + '.csv')
    os.system("ln --symbolic --relative " + dataset_dic + pre_dataset + '-' + str(_TODAY) + '.csv ' + dataset_dic + pre_dataset + '.csv')
        
# <-- train set split -->
train_features = features[1:-2] #Excepting src.port & label
target = features[-1] #label

X = df[train_features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=43)

# <-- test train : DecisionTree -->
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

y_pred = dtc.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)