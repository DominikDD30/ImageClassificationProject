#1
# model = Sequential([
#     Conv2D(16, (3, 3), activation="relu", input_shape=(150, 150, 3)),
#     MaxPooling2D((2, 2)),
#
#     Conv2D(32, (3, 3), activation="relu"),
#     MaxPooling2D((2, 2)),
#
#     Conv2D(64, (3, 3), activation="relu"),
#     MaxPooling2D((2, 2)),
#
#     Flatten(),
#
#     Dense(64, activation="relu"),
#     Dense(num_classes, activation="softmax")
# ])

#2 the same but more filters 32, 64 ,128
#3 the same but more epochos 7


#4 change model and generators type to binary ,last dense layer change astivation to sigmoid ||2epochs
# model = Sequential()
# model.add(Conv2D(16, (3,3), 1, activation='relu', input_shape=(150,150,3)))
# model.add(MaxPooling2D())
#
# model.add(Conv2D(32, (3,3), 1, activation='relu'))
# model.add(MaxPooling2D())
#
# model.add(Conv2D(16, (3,3), 1, activation='relu'))
# model.add(MaxPooling2D())
#
# model.add(Flatten())
# model.add(Dense(64, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))
#
# model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])

#5 the same as 4 but 7 epochs

#6 binary 2 epoch but without validation

#7  more filters and and Dropout
# model = Sequential()
# model.add(Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)))
# model.add(MaxPooling2D())
#
# model.add(Conv2D(64, (3,3),  activation='relu'))
# model.add(MaxPooling2D())
#
# model.add(Conv2D(128, (3,3), activation='relu'))
# model.add(MaxPooling2D())
#
# model.add(Flatten())
# model.add(Dropout(0.2)),
# model.add(Dense(512, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))
#
# model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])


#binaryV3   new Dense ,more dropout,change batch size from 32 to 256
# model = Sequential()
# model.add(Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)))
# model.add(MaxPooling2D())
#
# model.add(Conv2D(64, (3,3),  activation='relu'))
# model.add(MaxPooling2D())
#
# model.add(Conv2D(128, (3,3), activation='relu'))
# model.add(MaxPooling2D())
#
# model.add(Flatten())
# model.add(Dense(256,activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(64,activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(1,activation='sigmoid')) # output
#
# model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])


#binary128 bigger images

# model = Sequential()
# model.add(Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)))
# model.add(MaxPooling2D())
#
# model.add(Conv2D(64, (3,3),  activation='relu'))
# model.add(MaxPooling2D())
#
# model.add(Conv2D(128, (3,3), activation='relu'))
# model.add(MaxPooling2D())
#
# model.add(Flatten())
# model.add(Dense(256))
# model.add(Activation("relu"))
# model.add(Dropout(0.5))
# model.add(Dense(64))
# model.add(Activation("relu"))
# model.add(Dropout(0.5))
# model.add(Dense(2)) # output
# model.add(Activation("sigmoid"))
#
# model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])
