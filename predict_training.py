import pandas as pd
from joblib import load
ridge_model = load('ridge_model.joblib')


def name_of_training ():
    file_path = 'megaGymDataset.csv'
    df = pd.read_csv(file_path)
    trainid_trainingname = {}
    for i in range (len(df)):
        trainid_trainingname[df['Unnamed: 0'][i]]=df['Title'][i]
    return trainid_trainingname


def predict_training(completed_training, segmentation, goal, healthlimit, tire, time, quant, type, bodypart, equipment, level, top_k = 3):
    if completed_training:
        trainid = completed_training[-1]
        X = [[trainid, segmentation, goal, healthlimit, tire, time, quant, type, bodypart, equipment, level]]
        prediction_rating = ridge_model.predict(X)
    else:
        prediction_rating = 5
    trainingnames = name_of_training()
    file_path = 'mydataset.csv'
    df = pd.read_csv(file_path)
    training = []
    trainingnametop = []
    print(type, bodypart, equipment, level)
    for i in range (len(df)):
        if df['Type'][i] == type and df['BodyPart'][i]==bodypart and df['Level'][i]==level and df['Equipment'][i]==equipment:
            training.append([df['TrainID'][i], abs(prediction_rating - df['Rating'][i])])
    training.sort(key=lambda x: x[1])

    for j in range (len(training)):
        if training[j][0] not in completed_training and training[j][0] not in [x[0] for x in trainingnametop]:
            trainingnametop.append([training[j][0], trainingnames[training[j][0]]])
            if len(trainingnametop) == top_k:
                return trainingnametop



