import pandas as pd
df = pd.read_csv('vgsales.csv')
df

df.shape

df.values
--------------------
ML Steps:
  Import the data
  Clean the data
  Split the data into training/test sets
  Create a model
  Train the model
  Make prediction
  Evaluate and improve
---------------------
1. Import the data:
  
import pandas as pd
music_data = pd.read_csv('ML_music.csv')
music_data
  
-------------------
2.Preparing/Cleaning the data: 
   like removing duplicates

import pandas as pd
music_data = pd.read_csv('ML_music.csv')
x = music_data.drop(columns = ['Genre']) #x is i/p data set
y = music_data['Genre'] # y is o/p data set
y

-------------------- 
  3. Learning and predicting
  
  (Algorthim - Decesion Tree)

  import pandas as pd
from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_csv('ML_music.csv')
x = music_data.drop(columns = ['Genre']) #x is i/p data set
y = music_data['Genre'] # y is o/p data set

model = DecisionTreeClassifier()
model.fit(x, y)
predictions = model.predict([[24,1], [22,0]])
predictions

----------------------------------------------------
4. Accuracy test

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_data = pd.read_csv('ML_music.csv')
x = music_data.drop(columns = ['Genre']) #x is i/p data set
y = music_data['Genre'] # y is o/p data set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)
predictions = model.predict(x_test)

score = accuracy_score(y_test, predictions)
score

------------------------------------------------
5. Persisting Model:
  
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib            #Joblib object has methods for saving and loading modules 

music_data = pd.read_csv('ML_music.csv')
x = music_data.drop(columns = ['Genre']) #x is i/p data set
y = music_data['Genre'] # y is o/p data set


model = DecisionTreeClassifier()
model.fit(x, y)

joblib.dump(model, 'music-recommender.joblib')


#predictions = model.predict([[21, 1]])



#Persisting Models

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib            #Joblib object has methods for saving and loading modules 

# music_data = pd.read_csv('ML_music.csv')
# x = music_data.drop(columns = ['Genre']) #x is i/p data set
# y = music_data['Genre'] # y is o/p data set


# model = DecisionTreeClassifier()
# model.fit(x, y)

model = joblib.load('music-recommender.joblib')


predictions = model.predict([[21, 1]])
predictions
---------------------------------------------------
#Visualizing a Decision Tree

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

music_data = pd.read_csv('ML_music.csv')
x = music_data.drop(columns = ['Genre']) #x is i/p data set
y = music_data['Genre'] # y is o/p data set


model = DecisionTreeClassifier()
model.fit(x, y)

tree.export_graphviz(model, out_file='music-recommender.dot',         #upload the dot file in VSCODE to visualise the Decision Tree.
                    feature_names=['age', 'gender'],
                    class_names=sorted(y.unique()),
                     label='all',
                     rounded=True,
                     filled=True)

--------------------------------------------------------------------

