import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from joblib import dump
import xgboost as xgb

def model_train(data):
    label_encoder = LabelEncoder()
    data['encode'] = label_encoder.fit_transform(data['food'])
    
    product_counts = data['encode'].value_counts()

    products_multi= product_counts[product_counts > 1].index
    products_single = product_counts[product_counts == 1].index

    data_multi= data[data['encode'].isin(products_multi)]
    data_single = data[data['encode'].isin(products_single)]

    X__multi = data_multi[['weekday', 'hour']]
    y__multi = data_multi['encode']

    X_single = data_single[['weekday', 'hour']]
    y_single = data_single['encode']

    X_train_tmp, X_test, y_train_tmp, y_test = train_test_split(
        X__multi, y__multi, test_size=0.3, random_state=42
    )

    X_train = pd.concat([X_train_tmp, X_single])
    y_train = pd.concat([y_train_tmp, y_single])

    y = data['encode']
    model = xgb.XGBClassifier(objective='multi:softmax', num_class=len(y.unique()))
    model.fit(X_train, y_train)
    return model, label_encoder
        
        
        
