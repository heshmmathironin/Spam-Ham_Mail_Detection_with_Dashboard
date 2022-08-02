'''
Created on 25-May-2022

@author: A.P.SRITHARAN
'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import uuid
filename = 'finalized_model.pkl'
transformer = 'transformer.pkl'
#feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase='True')
def train(file):
    # loading the data from csv file to a pandas Dataframe
    raw_mail_data = pd.read_csv(file)
    print(raw_mail_data)
    # replace the null values with a null string
    mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)),'')
    mail_data.head()
    mail_data.shape
    # label spam mail as 0;  ham mail as 1;

    mail_data.loc[mail_data['Category'] == 'spam', 'Category',] = 0
    mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1
# separating the data as texts and label

    X = mail_data['Message']

    Y = mail_data['Category']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)
# transform the text data to feature vectors that can be used as input to the Logistic regression

    feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase='True')
    

    X_train_features = feature_extraction.fit_transform(X_train)
    X_test_features = feature_extraction.transform(X_test)
    pickle.dump(feature_extraction, open(transformer, 'wb'))
# convert Y_train and Y_test values as integers

    Y_train = Y_train.astype('int')
    Y_test = Y_test.astype('int')
    model = LogisticRegression()
# training the Logistic Regression model with the training data
    model.fit(X_train_features, Y_train)
    score = model.score(X_test_features, Y_test)

    print("Accuracy:", score)
    res = {'total_records_trained':mail_data.shape[0],'score':score}
    #filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))
    return res

def predict(input_mail):
    #input_mail = ["I've been searching for the right words to thank you for this breather. I promise i wont take your help for granted and will fulfil my promise. You have been wonderful and a blessing at all times"]
    #df = pd.DataFrame()
    #df['mail']=[input_mail]
    loaded_model = pickle.load(open(filename, 'rb'))
    #result = loaded_model.score(X_test, Y_test)
    #print(result)
    #feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase='True')
    feature_extraction = pickle.load(open(transformer, 'rb'))
    #feature_extraction.fit(df)
# convert text to feature vectors
    input_data_features = feature_extraction.transform([input_mail])

# making prediction

    prediction = loaded_model.predict(input_data_features)
    print(prediction)
    if prediction[0]==1:
        print('Ham mail')
        return 'Ham mail'
    else:
        print('Spam mail')
        return 'Spam mail'
    
def predict_file(file):
        # loading the data from csv file to a pandas Dataframe
    raw_mail_data = pd.read_csv(file)
    print(raw_mail_data)
    # replace the null values with a null string
    mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)),'')
    mail_data.head()
    mail_data.shape
    loaded_model = pickle.load(open(filename, 'rb'))
    feature_extraction = pickle.load(open(transformer, 'rb'))
    
# convert text to feature vectors
    input_data_features = feature_extraction.transform(mail_data['Message'])

# making prediction

    prediction = loaded_model.predict(input_data_features)
    print(prediction.shape)
 
    mail_data['Predicted_Category'] = prediction
    mail_data.loc[mail_data['Predicted_Category'] == 0, 'Predicted_Category',] = 'spam'
    mail_data.loc[mail_data['Predicted_Category'] == 1, 'Predicted_Category',] = 'ham'
    
    res_filename = str(uuid.uuid4())+'.csv'
    mail_data.to_csv(res_filename, sep='|',index=False, encoding='utf-8')
    #print("Accuracy:", score)
    
    
    return res_filename