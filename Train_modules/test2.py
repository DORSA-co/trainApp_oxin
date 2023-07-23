import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import ResNet50

def create_grayscale_model():
    # Load the pre-trained RGB model without top (classification) layers
    rgb_model = ResNet50(weights='imagenet', include_top=False, input_shape=(None, None, 3))

    # Create a new model with single-channel (grayscale) input
    grayscale_input = tf.keras.layers.Input(shape=(None, None, 1))
    
    # Replicate the single channel to create three identical channels (RGB)
    rgb_input = tf.keras.layers.Concatenate()([grayscale_input]*3)
    
    # Connect the replicated input to the RGB model
    grayscale_model = tf.keras.models.Model(inputs=grayscale_input, outputs=rgb_model(rgb_input))

    return grayscale_model

if __name__ == "__main__":
    # Create the grayscale model
    model = create_grayscale_model()

    # Load and preprocess a grayscale image
    grayscale_image = np.random.random((512, 512))  # Replace with your actual grayscale image
    grayscale_image = np.expand_dims(grayscale_image, axis=0)  # Add batch dimension
    grayscale_image = grayscale_image.astype('float32') / 255.0  # Normalize the image (if required)

    # Predict using the grayscale model
    predictions = model.predict(grayscale_image)

    print(predictions.shape)  # The output shape will be (batch_size, height, width, num_features)
