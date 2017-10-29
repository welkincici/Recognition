import keras.applications.mobilenet as mbn
import keras.preprocessing.image as kpi
import keras.callbacks as kcb
import keras.models as kmd
import numpy as np

model = mbn.MobileNet(weights=None, classes=10, alpha=0.5, input_shape=(224, 224, 3), dropout=0.75)
model.load_weights('mobile_net16.h5', by_name=True)


def identify(file_name):
    img = kpi.load_img(file_name, target_size=(224, 224))
    x = kpi.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = mbn.preprocess_input(x)
    preds = model.predict(x)

    return str(decode(preds[0]))


def decode(preds, top=1):
    label = ['bag', 'cap', 'cup', 'jacket', 'key', 'medicine_bottle',
             'slipper', 'spoon', 'umbrella', 'wallet']
    res = {}
    for i in range(0, len(label)):
        res[label[i]] = preds[i]

    res = sorted(res.items(), key=lambda a: a[1], reverse=True)
    return res[:top]


def train():

    adam = kmd.optimizers.adam(lr=0.000001)

    model.compile(loss='categorical_crossentropy',
                  optimizer=adam,
                  metrics=['accuracy'])

    train_data = kpi.ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        rotation_range=180
    )

    train_generator = train_data.flow_from_directory(
        'dataset/train',
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical'
    )

    validation_data = kpi.ImageDataGenerator(
        rescale=1. / 255
    )

    validation_generator = validation_data.flow_from_directory(
        'dataset/validation',
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical'
    )

    early_stopping = kcb.EarlyStopping(monitor='val_loss', patience=3, mode='min', min_delta=0.001)

    model.fit_generator(
        train_generator,

        samples_per_epoch=2048,
        nb_epoch=50,
        validation_data=validation_generator,
        nb_val_samples=50,
        callbacks=[early_stopping]
    )

    model.save_weights('mobile_net17.h5')

train()
