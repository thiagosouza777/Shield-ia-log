
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier

def treinar_modelo_supervisionado(X, y):
    modelo = RandomForestClassifier()
    modelo.fit(X, y)
    return modelo

def detectar_anomalias(X):
    detector = IsolationForest(contamination=0.05)
    anomalias = detector.fit_predict(X)
    return anomalias
