# MLP for Pima Indians Dataset with 10-fold cross validation
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
from sklearn.model_selection import StratifiedKFold
import numpy
# fix random seed for reproducibility

""" 
model.metrics_names[0] :  'loss'
model.metrics_names[1] : 'acc'
"""
seed = 7
numpy.random.seed(seed)
# define 10-fold cross validation test harness
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
cvscores = []
for train, test in kfold.split(dataset, labels):
    model = Sequential()
    model.add(Conv1D(32, 5, activation='relu', input_shape=(600,1)))
    model.add(Conv1D(64, 1, activation='relu'))
    model.add(MaxPooling1D(1))
    model.add(Conv1D(128, 1, activation='relu'))
    model.add(Conv1D(128, 1, activation='relu'))
    model.add(GlobalAveragePooling1D())
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
    model.fit(dataset[train], labels[train], batch_size=20, epochs=1)
    #evaluate
    scores = model.evaluate(dataset[test], labels[test], batch_size=15, verbose=0)
    #print(score)
	# evaluate the model
	#scores = model.evaluate(X[test], Y[test], verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1] * 100)
print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))
with open('scores_10fold.txt', 'w') as f:
    for item in cvscores:
        f.write("%s\n" % item)