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
Preparing/Cleaning the data: 
   like removing duplicates

import pandas as pd
music_data = pd.read_csv('ML_music.csv')
x = music_data.drop(columns = ['Genre']) #x is i/p data set
y = music_data['Genre'] # y is o/p data set
y

-------------------- 
  
