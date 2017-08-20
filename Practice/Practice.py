import keras.preprocessing.image as kpi
import keras.models as kmd
import keras.layers as kly


# Data Input

train_data = kpi.ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    rotation_range=180,
)

train_generator = train_data.flow_from_directory(
    'dataset/train',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

validation_data = kpi.ImageDataGenerator(
    rescale=1./255
)

validation_generator = validation_data.flow_from_directory(
    'dataset/validation',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

# CNN

model = kmd.Sequential()

model.add(kly.Convolution2D(32, 3, 3, input_shape=(150, 150, 3)))
model.add(kly.Activation('relu'))
model.add(kly.MaxPooling2D(pool_size=(2, 2)))

model.add(kly.Convolution2D(32, 3, 3))
model.add(kly.Activation('relu'))
model.add(kly.MaxPooling2D(pool_size=(2, 2)))

model.add(kly.Convolution2D(64, 3, 3))
model.add(kly.Activation('relu'))
model.add(kly.MaxPooling2D(pool_size=(2, 2)))

model.add(kly.Flatten())
model.add(kly.Dense(64))
model.add(kly.Activation('relu'))
model.add(kly.Dropout(0.5))
model.add(kly.Dense(1))
model.add(kly.Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit_generator(
    train_generator,
    samples_per_epoch=2048,
    nb_epoch=1,
    validation_data=validation_generator,
    nb_val_samples=800
)

# Save weights

model.save_weights('first_try.h5')

