from preprocessing import extract_features_from_folder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression 
import pandas as pd
import json 
import joblib 

folder_path = 'cropped/train'
X_raw, y_encoded, le = extract_features_from_folder(folder_path)

X_train, X_test, y_train, y_test = train_test_split(X_raw, y_encoded, test_size=0.2,random_state=0)

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(kernel='rbf',C=5,probability=True))])
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)


model_params = {
    'svm':{
        'model':SVC(probability=True),
        'params':{
            'svc__C': [1, 10, 100],
            'svc__kernel': ['linear', 'rbf'],
        }
    },
    'logistic':{
        'model':LogisticRegression(),
        'params':{
            'logisticregression__C': [1, 5, 10],
        }
    }
}



scores = []
best_estimators = {}

for algo, mp in model_params.items():
    pipe = make_pipeline(StandardScaler(),mp['model'])
    clf = GridSearchCV(pipe, mp['params'], cv=5, return_train_score=False, n_jobs=-1)

    clf.fit(X_train, y_train)
    scores.append({
        'model': algo,
        'best_score': clf.best_score_,
        'best_params': clf.best_params_
    })
    best_estimators[algo] = clf.best_estimator_
df = pd.DataFrame(scores,columns=['model','best_score','best_params'])

y_pred = best_estimators['svm'].predict(X_test)




joblib.dump(best_estimators['svm'], 'model.pkl')

classes = le.classes_.tolist()
classes_dict = {classes[i]:i for i in range(len(classes))}
with open('classes.json','w') as f:
    f.write(json.dumps(classes_dict))
    
