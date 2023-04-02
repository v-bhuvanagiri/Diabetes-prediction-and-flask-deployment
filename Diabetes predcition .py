import pandas as pd


df = pd.read_csv(r"C:\Users\Vaishnavi\Downloads\diabetes.csv")

x = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.30,random_state =6)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)



import pickle

pickle.dump(dt,open("model1.pkl","wb"))











