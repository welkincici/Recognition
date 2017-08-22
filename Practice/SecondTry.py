from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras import models, layers


# Data Input

train_data = image.ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    rotation_range=180,
)

train_generator = train_data.flow_from_directory(
    'dataset/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary'
)

validation_data = image.ImageDataGenerator(
    rescale=1./255
)

validation_generator = validation_data.flow_from_directory(
    'dataset/validation',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary'
)

# CNN based on VGG16

# load VGG16 and freeze it
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

for layer in base_model.layers:
    layer.trainable = False

# add top layers
x = base_model.output
x = layers.Flatten()(x)
x = layers.Dense(256, activation='relu')(x)
x = layers.Dropout(0.5)(x)
predictions = layers.Dense(1, activation='sigmoid')(x)

model = models.Model(inputs=base_model.input, outputs=predictions)

model.compile(loss='binary_crossentropy', optimizer='rmsprop',
              metrics=['accuracy'])

model.fit_generator(
    train_generator,
    samples_per_epoch=2048,
    nb_epoch=1,
    validation_data=validation_generator,
    nb_val_samples=800
)

model.save('second_try.h5')
