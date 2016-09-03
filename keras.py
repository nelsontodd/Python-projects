import numpy as np
np.random.seed(1337)
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.utils import np_utils

batch_size = 120
n_classes = 10
n_epochs = 20

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_test /= 255

y_train = np_utils.to_categorical(y_train, n_classes)
y_test = np_utils.to_categorical(y_test, n_classes)

model = Sequential()
model.add(Dense(512, input_shape=(784, )))
model.add(Activation('relu'))
model.add(Dropout(.2))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(.2))
model.add(Dense(10))
model.add(Activation('softmax'))

sgd = SGD(lr=.05)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

model.fit(x_train, y_train, batch_size=batch_size, nb_epoch=n_epochs, show_accuracy=True, verbose = 1, validation_data= (x_test, y_test))
score = model.evaluate(x_test, y_test, show_accuracy=True, verbose=0)
print("Test score: {}".format(score[0]))
print("Test accuracy: {}".format(score[1]))
