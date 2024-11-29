import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

DATA_DIR = "data/processed/"

def build_model():
    """Build a simple CNN model."""
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')  # Adjust based on your task
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model():
    """Train the model using preprocessed data."""
    datagen = ImageDataGenerator(validation_split=0.2)

    train_gen = datagen.flow_from_directory(DATA_DIR, target_size=(224, 224), subset='training')
    val_gen = datagen.flow_from_directory(DATA_DIR, target_size=(224, 224), subset='validation')

    model = build_model()
    model.fit(train_gen, epochs=10, validation_data=val_gen)
    model.save("models/deepfashion_model.h5")

if __name__ == "__main__":
    train_model()
