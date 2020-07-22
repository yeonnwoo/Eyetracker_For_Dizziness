import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Activation, Dense
from tensorflow.keras import optimizers
import tensorflow as tf
import numpy as np
import os
from keras.callbacks import ModelCheckpoint, EarlyStopping
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.utils import to_categorical
from keras.layers.core import Activation, Dense, Dropout


from keras.models import load_model
model = load_model('eye_mlp_model.h5')

data = pd.read_csv('real_test.csv')
data=data.values
X_test = data[:,1:-1]

results=model.predict(X_test)

if np.argmax(results[0])>=0.5:
    ans= "안구운동에 이상이 있습니다 :("
else:
    ans="이상이 없습니다 :)"

print('검진결과,',ans)

f = open('result.txt', mode='wt', encoding = 'utf-8')
f.write(str(np.argmax(results[0])))
f.close()
os.system('watchDog')
