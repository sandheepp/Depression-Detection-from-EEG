from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D

seq_length = 600

model = Sequential()
model.add(Conv1D(filters=8, kernel_size=1, activation='relu', input_shape=(24000,600)))
model.add(MaxPooling1D(3))
model.add(Conv1D(4, 1, activation='relu'))
model.add(Conv1D(2, 1, activation='relu'))
model.add(GlobalAveragePooling1D())
model.add(Dropout(0.1))
#model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
#model.add(Flatten())
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)
score = model.evaluate(x_test, y_test)