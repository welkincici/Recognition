import keras.preprocessing.image as kpi

train_data = kpi.ImageDataGenerator(
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    rotation_range=180,
    fill_mode='nearest'
)

i = 0
for batch in train_data.flow_from_directory('dataset/raw', save_format='jpg', save_to_dir='dataset/train'):
    i += 1
    if i > 20:
        break
