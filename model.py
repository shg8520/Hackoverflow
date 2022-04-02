import numpy as np
import pandas as pd
import joblib

dataset= pd.read_csv("Sur - Form Responses 1.csv")

dataset["Gender"]=dataset["Gender"].astype('category')
dataset["Age"]=dataset["Age"].astype('category')
dataset["How-active-is-your-work?"]=dataset["How-active-is-your-work?"].astype('category')
dataset["How-is-your-fitness-level"]=dataset["How-is-your-fitness-level"].astype('category')
dataset["Working-Hour-Per-Day"]=dataset["Working-Hour-Per-Day"].astype('category')
dataset["Do-you-exercise-daily?"]=dataset["Do-you-exercise-daily?"].astype('category')
dataset["How-many-hours-in-a-day-you-do-any-physical-activities?"]=dataset["How-many-hours-in-a-day-you-do-any-physical-activities?"].astype('category')
dataset["Do-you-follow-any-diet-plans?"]=dataset["Do-you-follow-any-diet-plans?"].astype('category')
dataset["How-many-hours-a-day-do-you-sleep?"]=dataset["How-many-hours-a-day-do-you-sleep?"].astype('category')
dataset["How-often-do-you-spend-with-fam-and-friends?"]=dataset["How-often-do-you-spend-with-fam-and-friends?"].astype('category')
dataset["How-many-hours-do-you-spend-for-entertainment?"]=dataset["How-many-hours-do-you-spend-for-entertainment?"].astype('category')
dataset["Does-using-social-media-affect-your-mental-health"]=dataset["Does-using-social-media-affect-your-mental-health"].astype('category')
dataset["How-often-are-you-stressed?"]=dataset["How-often-are-you-stressed?"].astype('category')
dataset["How-much-your-mental-health-has-been-affected-in-pandemic?"]=dataset["How-much-your-mental-health-has-been-affected-in-pandemic?"].astype('category')
dataset["Target"]=dataset["Target"].astype('category')


dataset["Gender"]=dataset["Gender"].cat.codes
dataset["Age"]=dataset["Age"].cat.codes
dataset["How-active-is-your-work?"]=dataset["How-active-is-your-work?"].cat.codes
dataset["How-is-your-fitness-level"]=dataset["How-is-your-fitness-level"].cat.codes
dataset["Working-Hour-Per-Day"]=dataset["Working-Hour-Per-Day"].cat.codes
dataset["Do-you-exercise-daily?"]=dataset["Do-you-exercise-daily?"].cat.codes
dataset["How-many-hours-in-a-day-you-do-any-physical-activities?"]=dataset["How-many-hours-in-a-day-you-do-any-physical-activities?"].cat.codes
dataset["Do-you-follow-any-diet-plans?"]=dataset["Do-you-follow-any-diet-plans?"].cat.codes
dataset["How-many-hours-a-day-do-you-sleep?"]=dataset["How-many-hours-a-day-do-you-sleep?"].cat.codes
dataset["How-often-do-you-spend-with-fam-and-friends?"]=dataset["How-often-do-you-spend-with-fam-and-friends?"].cat.codes
dataset["How-many-hours-do-you-spend-for-entertainment?"]=dataset["How-many-hours-do-you-spend-for-entertainment?"].cat.codes
dataset["Does-using-social-media-affect-your-mental-health"]=dataset["Does-using-social-media-affect-your-mental-health"].cat.codes
dataset["How-often-are-you-stressed?"]=dataset["How-often-are-you-stressed?"].cat.codes
dataset["How-much-your-mental-health-has-been-affected-in-pandemic?"]=dataset["How-much-your-mental-health-has-been-affected-in-pandemic?"].cat.codes
dataset["Target"]=dataset["Target"].cat.codes

X=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

from sklearn.ensemble import RandomForestClassifier
cls = RandomForestClassifier(criterion = 'entropy', n_estimators= 300, random_state=42)
cls.fit(X_train,y_train)

print('Accuracy is', cls.score(X_test,y_test)*100,'%')

filename="model.sav"
joblib.dump(cls,filename)
