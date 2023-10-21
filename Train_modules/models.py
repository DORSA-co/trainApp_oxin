import numpy as np
import os
import numpy as np
import tensorflow as tf

# tf.compat.v1.enable_eager_execution()
from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.callbacks import ModelCheckpoint, LearningRateScheduler
from tensorflow.keras.models import load_model


# from tensorflow.keras import backend as keras
try:
    from Train_modules.deep_utils import metrics
except:
    from deep_utils import metrics

from tensorflow.keras import layers

import segmentation_models as sm

sm.set_framework("tf.keras")
sm.framework()

try:
    from Train_modules import Unet
except:
    import Unet
# sm.set_framework("tf.keras")
# sm.framework()
from yolov5.models.common import DetectMultiBackend


BINARY = "binary"
CATEGORICAL = "categorical"
LOSS = {"DIFO": sm.losses.DiceLoss() + sm.losses.BinaryFocalLoss()}

__loss__ = {CATEGORICAL: "categorical_crossentropy", BINARY: "binary_crossentropy"}
# __activation__ = {CATEGORICAL: "softmax", BINARY: "sigmoid"}
__activation__ = {CATEGORICAL: "sigmoid", BINARY: "sigmoid"}


def unet_model(
    input_size, learning_rate=1e-4, num_class=1, mode=BINARY, weights_path=None
):
    activation = "sigmoid" if num_class == 1 else "softmax"
    if weights_path is not None:
        model = Unet.unet(
            backbone_name="efficientnetb2",
            input_shape=input_size,
            classes=num_class,
            activation=activation,
            weights=weights_path,
            encoder_freeze=False,
            decoder_use_batchnorm=True,
        )
    else:
        model = Unet.unet(
            backbone_name="efficientnetb2",
            input_shape=input_size,
            classes=num_class,
            activation=activation,
            encoder_freeze=False,
            decoder_use_batchnorm=True,
        )

    optimizer = tf.keras.optimizers.Adam(learning_rate)
    metrics = [
        "accuracy",
        sm.metrics.IOUScore(threshold=0.5),
        sm.metrics.FScore(threshold=0.5),
    ]
    loss = LOSS["DIFO"]
    model.compile(loss=loss, metrics=metrics, optimizer=optimizer)
    return model


def base_unet(
    input_size,
    num_class=1,
    learning_rate=1e-3,
    mode=BINARY,
    pretained="imagenet",
    base_model="resnet34",
):
    """Create base Unet model using segmentation_models library.

    :param input_size:  Shape of input image (H, W, C), in general case you do not need to set H and W shapes,
    just pass (None, None, C) to make your model be able to process images af any size,
    but H and W of input images should be divisible by factor 32.
    :type input_size: tuple
    :param num_class: A number of classes for output, defaults to 1
    :type num_class: int, optional
    :param learning_rate: Learning rate of model, defaults to 1e-3
    :type learning_rate: float, optional
    :param mode: Defined BINARY or CATEGORICAL, defaults to BINARY
    :type mode: str, optional
    :param pretained: One of None (random initialization), imagenet (pre-training on ImageNet), defaults to 'imagenet'
    :type pretained: str, optional
    :param base_model: Name of classification model (without last dense layers) used as feature extractor
    to build segmentation model, defaults to 'resnet34'
    :type base_model: str, optional
    :return: Base Unet model.
    :rtype: keras.models.Model
    """
    if input_size[-1] != 3:
        pretained = None
    model = sm.Unet(
        base_model,
        input_shape=input_size,
        classes=num_class,
        activation=__activation__[mode],
        encoder_weights=pretained,
    )

    iou = metrics.iou()
    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss=__loss__[mode],
        metrics=[
            "accuracy",
            tf.keras.metrics.Precision(name="Precision"),
            tf.keras.metrics.Recall(name="Recall"),
            iou,
        ],
    )

    model.summary()
    return model


def unet(input_size, learning_rate=1e-4, num_class=1, mode=BINARY, nfilter=64):
    """Create Unet model.

    :param input_size: Shape of input image
    :type input_size: tuple
    :param learning_rate: Learning rate of model. Defaults to 1e-4., defaults to 1e-4
    :type learning_rate: float, optional
    :param num_class: A number of classes for output, defaults to 1
    :type num_class: int, optional
    :param mode: Defined BINARY or CATEGORICAL, defaults to BINARY
    :type mode: str, optional
    :param nfilter: The number of output filters in the first convolution. Increase each time by a factor of two, defaults to 64
    :type nfilter: int, optional
    :return: Unet model.
    :rtype: keras.models.Model
    """
    assert num_class > 0, "num class could not be 0"
    if mode == CATEGORICAL:
        assert (
            num_class > 1
        ), "for categorical out_mode, num_class should be greater than 2"

    inputs = Input(input_size)
    conv1 = Conv2D(
        nfilter, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(inputs)
    conv1 = Conv2D(
        nfilter, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
    conv2 = Conv2D(
        nfilter * 2,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(pool1)
    conv2 = Conv2D(
        nfilter * 2,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
    conv3 = Conv2D(
        nfilter * 4,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(pool2)
    conv3 = Conv2D(
        nfilter * 4,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
    conv4 = Conv2D(
        nfilter * 8,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(pool3)
    conv4 = Conv2D(
        nfilter * 8,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(conv4)
    drop4 = Dropout(0.5)(conv4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(drop4)

    conv5 = Conv2D(
        nfilter * 16,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(pool4)
    conv5 = Conv2D(
        nfilter * 16,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(conv5)
    drop5 = Dropout(0.5)(conv5)

    up6 = Conv2D(
        nfilter * 8,
        2,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(UpSampling2D(size=(2, 2))(drop5))
    merge6 = concatenate([drop4, up6], axis=3)
    conv6 = Conv2D(
        nfilter * 8,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(merge6)
    conv6 = Conv2D(
        nfilter * 8,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(conv6)

    up7 = Conv2D(
        nfilter * 4,
        2,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(UpSampling2D(size=(2, 2))(conv6))
    merge7 = concatenate([conv3, up7], axis=3)
    conv7 = Conv2D(
        nfilter * 4,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(merge7)
    conv7 = Conv2D(
        nfilter * 4,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(conv7)

    up8 = Conv2D(
        nfilter * 2,
        2,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(UpSampling2D(size=(2, 2))(conv7))
    merge8 = concatenate([conv2, up8], axis=3)
    conv8 = Conv2D(
        nfilter * 2,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(merge8)
    conv8 = Conv2D(
        nfilter * 2,
        3,
        activation="relu",
        padding="same",
        kernel_initializer="he_normal",
    )(conv8)

    up9 = Conv2D(
        nfilter, 2, activation="relu", padding="same", kernel_initializer="he_normal"
    )(UpSampling2D(size=(2, 2))(conv8))
    merge9 = concatenate([conv1, up9], axis=3)
    conv9 = Conv2D(
        nfilter, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(merge9)
    conv9 = Conv2D(
        nfilter, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv9)
    conv9 = Conv2D(
        2, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv9)
    conv10 = Conv2D(num_class, 1, activation=__activation__[mode])(conv9)

    model = Model(inputs=inputs, outputs=conv10)
    iou = metrics.iou()
    """
    initial_learning_rate = 0.001
    learning_rate_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
                                                                initial_learning_rate,
                                                                decay_steps=1000,
                                                                decay_rate=0.95,
                                                                staircase=True
                                                                )
    """
    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss=__loss__[mode],
        metrics=[
            "accuracy",
            tf.keras.metrics.Precision(name="Precision"),
            tf.keras.metrics.Recall(name="Recall"),
            iou,
        ],
    )

    model.summary()

    return model


def low_unet(input_size, learning_rate=1e-4, num_class=1, mode=BINARY):
    """Create Low Unet model using SeparableConv2D.

    :param input_size: Shape of input image
    :type input_size: tuple
    :param learning_rate: Learning rate of model, defaults to 1e-4
    :type learning_rate: float, optional
    :param num_class: A number of classes for output, defaults to 1
    :type num_class: int, optional
    :param mode: Defined BINARY or CATEGORICAL, defaults to BINARY
    :type mode: str, optional
    :return: Low Unet model
    :rtype: keras.models.Model
    """
    assert num_class > 0, "num class could not be 0"
    if mode == CATEGORICAL:
        assert (
            num_class > 1
        ), "for categorical out_mode, num_class should be greater than 2"

    inputs = Input(input_size)
    conv1 = SeparableConv2D(
        32, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(inputs)
    conv1 = SeparableConv2D(
        32, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
    conv2 = SeparableConv2D(
        64, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(pool1)
    conv2 = SeparableConv2D(
        64, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
    conv3 = SeparableConv2D(
        128, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(pool2)
    conv3 = SeparableConv2D(
        128, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
    conv4 = SeparableConv2D(
        256, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(pool3)
    conv4 = SeparableConv2D(
        256, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv4)
    drop4 = Dropout(0.5)(conv4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(drop4)

    conv5 = SeparableConv2D(
        512, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(pool4)
    conv5 = SeparableConv2D(
        512, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv5)
    drop5 = Dropout(0.5)(conv5)

    up6 = SeparableConv2D(
        256, 2, activation="relu", padding="same", kernel_initializer="he_normal"
    )(UpSampling2D(size=(2, 2))(drop5))
    merge6 = concatenate([drop4, up6], axis=3)
    conv6 = SeparableConv2D(
        256, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(merge6)
    conv6 = SeparableConv2D(
        256, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv6)

    up7 = SeparableConv2D(
        128, 2, activation="relu", padding="same", kernel_initializer="he_normal"
    )(UpSampling2D(size=(2, 2))(conv6))
    merge7 = concatenate([conv3, up7], axis=3)
    conv7 = SeparableConv2D(
        128, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(merge7)
    conv7 = SeparableConv2D(
        128, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv7)

    up8 = SeparableConv2D(
        64, 2, activation="relu", padding="same", kernel_initializer="he_normal"
    )(UpSampling2D(size=(2, 2))(conv7))
    merge8 = concatenate([conv2, up8], axis=3)
    conv8 = SeparableConv2D(
        64, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(merge8)
    conv8 = SeparableConv2D(
        64, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv8)

    up9 = SeparableConv2D(
        32, 2, activation="relu", padding="same", kernel_initializer="he_normal"
    )(UpSampling2D(size=(2, 2))(conv8))
    merge9 = concatenate([conv1, up9], axis=3)
    conv9 = SeparableConv2D(
        32, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(merge9)
    conv9 = SeparableConv2D(
        32, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv9)
    conv9 = SeparableConv2D(
        16, 3, activation="relu", padding="same", kernel_initializer="he_normal"
    )(conv9)
    conv10 = SeparableConv2D(num_class, 1, activation=__activation__[mode])(conv9)

    model = Model(inputs=inputs, outputs=conv10)
    iou = metrics.iou()

    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss=__loss__[mode],
        metrics=[
            "accuracy",
            tf.keras.metrics.Precision(name="Precision"),
            tf.keras.metrics.Recall(name="Recall"),
            iou,
        ],
    )
    model.summary()

    return model


def resnet_unet(input_size, learning_rate=1e-3, num_class=1, mode=BINARY):
    """Create Resnet Unet model using residual blocks.

    :param input_size: Shape of input image
    :type input_size: tuple
    :param learning_rate: Learning rate of model, defaults to 1e-3
    :type learning_rate: float, optional
    :param num_class: A number of classes for output, defaults to 1
    :type num_class: int, optional
    :param mode: Defined BINARY or CATEGORICAL, defaults to BINARY
    :type mode: str, optional
    :return: Resnet Unet model
    :rtype: keras.models.Model
    """
    assert num_class > 0, "num class could not be 0"
    if mode == CATEGORICAL:
        assert (
            num_class > 1
        ), "for categorical out_mode, num_class should be greater than 2"

    inputs = Input(shape=input_size)
    ### [First half of the network: downsampling inputs] ###
    # Entry block
    x = Conv2D(32, 3, strides=2, padding="same")(inputs)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    previous_block_activation = x  # Set aside residual

    # Blocks 1, 2, 3 are identical apart from the feature depth.
    for filters in [64, 128, 256]:
        x = Activation("relu")(x)
        x = SeparableConv2D(filters, 3, padding="same")(x)
        x = BatchNormalization()(x)

        x = Activation("relu")(x)
        x = SeparableConv2D(filters, 3, padding="same")(x)
        x = BatchNormalization()(x)

        x = MaxPooling2D(3, strides=2, padding="same")(x)

        # Project residual
        residual = Conv2D(filters, 1, strides=2, padding="same")(
            previous_block_activation
        )
        x = add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    ### [Second half of the network: upsampling inputs] ###

    for filters in [256, 128, 64, 32]:
        x = Activation("relu")(x)
        x = Conv2DTranspose(filters, 3, padding="same")(x)
        x = BatchNormalization()(x)

        x = Activation("relu")(x)
        x = Conv2DTranspose(filters, 3, padding="same")(x)
        x = BatchNormalization()(x)

        x = UpSampling2D(2)(x)

        # Project residual
        residual = UpSampling2D(2)(previous_block_activation)
        residual = Conv2D(filters, 1, padding="same")(residual)
        x = add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    # Add a per-pixel classification layer
    outputs = Conv2D(num_class, 3, activation=__activation__[mode], padding="same")(x)

    # Define the model
    model = Model(inputs, outputs)

    iou = metrics.iou()
    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss=__loss__[mode],
        metrics=[
            "accuracy",
            tf.keras.metrics.Precision(name="Precision"),
            tf.keras.metrics.Recall(name="Recall"),
            iou,
        ],
    )

    model.summary()

    return model


def resnet_cnn(
        
    input_size,
    learning_rate=1e-3,
    num_class=1,
    mode=BINARY,
    fine_tune_layer=-1,
    weights=None,
    
):
    """Create Resnet model.

    :param input_size: Shape of input image
    :type input_size: tuple
    :param learning_rate: Learning rate of model, defaults to 1e-3
    :type learning_rate: float, optional
    :param num_class: A number of classes for output, defaults to 1
    :type num_class: int, optional
    :param mode: Defined BINARY or CATEGORICAL, defaults to BINARY, defaults to BINARY
    :type mode: str, optional
    :param fine_tune_layer: Layer number for fine tunning, defaults to -1
    :type fine_tune_layer: int, optional
    :param weights: Pretraind weights path, defaults to None
    :type weights: str, optional
    :return: Resnet CNN model
    :rtype: keras.models.Model
    """




    preprocess_input = tf.keras.applications.resnet_v2.preprocess_input

    try:
        base_model = tf.keras.applications.ResNet50V2(
            include_top=False, weights="imagenet", input_shape=input_size
        )
    except Exception as e:
        print(e)
        base_model = tf.keras.applications.ResNet50V2(
            include_top=False, weights=None, input_shape=input_size
        )

    base_model.trainable = False

    inpt = tf.keras.Input(shape=(input_size[0],input_size[1],1))

    inpt2 = tf.keras.layers.Concatenate()([inpt]*3)

    inpt_pre = preprocess_input(inpt2)

    # --------------------------------------------
    out_base = base_model(inpt_pre)
    # --------------------------------------------

    x = tf.keras.layers.GlobalAveragePooling2D()(out_base)
    x = tf.keras.layers.Dropout(0.2)(x)
    x = tf.keras.layers.Dense(512, activation="relu")(x)
    # x = keras.layers.Dense(256, activation='relu')(x)
    out = x = tf.keras.layers.Dense(num_class, activation=__activation__[mode])(x)
    model = tf.keras.Model(inpt, out)
    # --------------------------------------------
    if weights is not None:
        pretrain_model = load_model(weights)
        weights = pretrain_model.get_weights()
        model.set_weights(weights)
    # --------------------------------------------
    if fine_tune_layer > 0:
        base_model = model.layers[4]
        base_model.trainable = True
        for i in range(fine_tune_layer):
            base_model.layers[i].trainable = False
    # --------------------------------------------

    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss=__loss__[mode],
        metrics=[
            "accuracy",
            tf.keras.metrics.Precision(name="Precision"),
            tf.keras.metrics.Recall(name="Recall"),
        ],
    )

    model.summary()
    return model


def xception_cnn(
    input_size,
    learning_rate=1e-3,
    num_class=1,
    mode=BINARY,
    fine_tune_layer=-1,
    weights=None,
):
    """Create Xception model.

    :param input_size: Shape of input image
    :type input_size: tuple
    :param learning_rate: Learning rate of model, defaults to 1e-3
    :type learning_rate: float, optional
    :param num_class: Number of classes for output, defaults to 1
    :type num_class: int, optional
    :param mode: Defined BINARY or CATEGORICAL, defaults to BINARY
    :type mode: str, optional
    :param fine_tune_layer: Layer number for fine tunning, defaults to -1
    :type fine_tune_layer: int, optional
    :param weights: Pretraind weights path, defaults to None
    :type weights: str, optional
    :return: Xception CNN model
    :rtype: keras.models.Model
    """
    preprocess_input = tf.keras.applications.xception.preprocess_input

    try:
        base_model = tf.keras.applications.Xception(
            include_top=False, weights="imagenet", input_shape=input_size
        )
    except Exception as e:
        print(e)
        base_model = tf.keras.applications.Xception(
            include_top=False, weights=None, input_shape=input_size
        )

    base_model.trainable = False

    inpt = tf.keras.Input(shape=(input_size[0],input_size[1],1))
    print(input_size)

    inpt2 = tf.keras.layers.Concatenate()([inpt]*3)

    inpt_pre = preprocess_input(inpt2)

    # inpt = tf.keras.Input(shape=input_size)
    # inpt_pre = preprocess_input(inpt)
    # --------------------------------------------
    out_base = base_model(inpt_pre)
    # --------------------------------------------
    x = tf.keras.layers.GlobalAveragePooling2D()(out_base)
    x = tf.keras.layers.Dropout(0.2)(x)
    x = tf.keras.layers.Dense(512, activation="relu")(x)
    x = tf.keras.layers.Dropout(0.2)(x)
    x = tf.keras.layers.Dense(256, activation="relu")(x)
    out = tf.keras.layers.Dense(num_class, activation=__activation__[mode])(x)
    model = tf.keras.Model(inpt, out)

    # --------------------------------------------
    if weights is not None:
        # pretrain_model = load_model(weights)
        # weights = pretrain_model.get_weights()
        # model.set_weights(weights)
        model.load_weights(weights)


    fine_tune_layer=-4
    # --------------------------------------------
    if fine_tune_layer > 0:
        base_model = model.layers[4]
        base_model.trainable = True
        for i in range(fine_tune_layer):
            base_model.layers[i].trainable = False


    elif fine_tune_layer<0:
        fine_tune_layer = abs(fine_tune_layer) 
        len_model = len(model.layers)

        for i in range(4,len_model-fine_tune_layer):

            model.layers[i].trainable = False





    # --------------------------------------------

    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss=__loss__[mode],
        metrics=[
            "accuracy",
            tf.keras.metrics.Precision(name="Precision"),
            tf.keras.metrics.Recall(name="Recall"),
        ],
    )
    return model


def efficientnetb4_cnn(
    input_size,
    learning_rate=1e-3,
    num_class=1,
    mode=BINARY,
    fine_tune_layer=-1,
    weights=None,
):
    """Create EfficientNetB4 model.

    :param input_size: Shape of input image
    :type input_size: tuple
    :param learning_rate: Learning rate of model, defaults to 1e-3
    :type learning_rate: float, optional
    :param num_class: A number of classes for output, defaults to 1
    :type num_class: int, optional
    :param mode: Defined BINARY or CATEGORICAL, defaults to BINARY, defaults to BINARY
    :type mode: str, optional
    :param fine_tune_layer: Layer number for fine tunning, defaults to -1
    :type fine_tune_layer: int, optional
    :param weights: Pretraind weights path, defaults to None
    :type weights: str, optional
    :return: EfficientNetB4 CNN model
    :rtype: keras.models.Model
    """
    preprocess_input = tf.keras.applications.efficientnet.preprocess_input
    base_model = tf.keras.applications.EfficientNetB4(
        include_top=False, weights="imagenet", input_shape=input_size
    )
    base_model.trainable = False

    inpt = tf.keras.Input(shape=input_size)
    inpt_pre = preprocess_input(inpt)
    # --------------------------------------------
    out_base = base_model(inpt_pre)
    # --------------------------------------------
    x = tf.keras.layers.GlobalAveragePooling2D()(out_base)
    x = tf.keras.layers.Dropout(0.2)(x)
    x = tf.keras.layers.Dense(512, activation="relu")(x)
    x = tf.keras.layers.Dense(256, activation="relu")(x)
    out = tf.keras.layers.Dense(num_class, activation=__activation__[mode])(x)
    model = tf.keras.Model(inpt, out)

    # --------------------------------------------
    if weights is not None:
        model.load_weights(weights)
    # --------------------------------------------
    # if fine_tune_layer>0:
    #     base_model = model.layers[3]
    #     base_model.trainable = True
    #     for i in range(fine_tune_layer):
    #         base_model.layers[i].trainable = False
    # --------------------------------------------

    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss=__loss__[mode],
        metrics=[
            "accuracy",
            tf.keras.metrics.Precision(name="Precision"),
            tf.keras.metrics.Recall(name="Recall"),
        ],
    )
    return model


def efficientnetb2_cnn(
    input_size,
    learning_rate=1e-3,
    num_class=1,
    mode=BINARY,
    fine_tune_layer=-1,
    weights=None,
):
    """Create EfficientNetB2 model.

    :param input_size: Shape of input image
    :type input_size: tuple
    :param learning_rate: Learning rate of model, defaults to 1e-3
    :type learning_rate: float, optional
    :param num_class: A number of classes for output, defaults to 1
    :type num_class: int, optional
    :param mode: Defined BINARY or CATEGORICAL, defaults to BINARY, defaults to BINARY
    :type mode: str, optional
    :param fine_tune_layer: Layer number for fine tunning, defaults to -1
    :type fine_tune_layer: int, optional
    :param weights: Pretraind weights path, defaults to None
    :type weights: str, optional
    :return: EfficientNetB2 CNN model
    :rtype: keras.models.Model
    """
    preprocess_input = tf.keras.applications.efficientnet.preprocess_input
    base_model = tf.keras.applications.EfficientNetB2(
        include_top=False, weights="imagenet", input_shape=input_size
    )
    base_model.trainable = False

    inpt = tf.keras.Input(shape=input_size)
    inpt_pre = preprocess_input(inpt)
    # --------------------------------------------
    out_base = base_model(inpt_pre)
    # --------------------------------------------
    x = tf.keras.layers.GlobalAveragePooling2D()(out_base)
    x = tf.keras.layers.Dropout(0.1)(x)
    x = tf.keras.layers.Dense(512, activation="tanh")(x)
    x = tf.keras.layers.Dropout(0.1)(x)
    x = tf.keras.layers.Dense(256, activation="tanh")(x)
    x = tf.keras.layers.Dropout(0.1)(x)
    x = tf.keras.layers.Dense(256, activation="tanh")(x)
    out = tf.keras.layers.Dense(num_class, activation=__activation__[mode])(x)
    model = tf.keras.Model(inpt, out)

    # --------------------------------------------
    if weights is not None:
        model.load_weights(weights)
    # --------------------------------------------
    # if fine_tune_layer>0:
    #     base_model = model.layers[3]
    #     base_model.trainable = True
    #     for i in range(fine_tune_layer):
    #         base_model.layers[i].trainable = False
    # --------------------------------------------

    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss=__loss__[mode],
        metrics=[
            "accuracy",
            tf.keras.metrics.Precision(name="Precision"),
            tf.keras.metrics.Recall(name="Recall"),
        ],
    )
    return model


def efficientnetb2_base_cnn(
    input_size,
    learning_rate=1e-3,
    num_class=1,
    mode=BINARY,
    fine_tune_layer=-1,
    weights=None,
):
    """Create EfficientNetB2 base model.

    :param input_size: Shape of input image
    :type input_size: tuple
    :param learning_rate: Learning rate of model, defaults to 1e-3
    :type learning_rate: float, optional
    :param num_class: A number of classes for output, defaults to 1
    :type num_class: int, optional
    :param mode: Defined BINARY or CATEGORICAL, defaults to BINARY, defaults to BINARY
    :type mode: str, optional
    :param fine_tune_layer: Layer number for fine tunning, defaults to -1
    :type fine_tune_layer: int, optional
    :param weights: Pretraind weights path, defaults to None
    :type weights: str, optional
    :return: EfficientNetB4 CNN model
    :rtype: keras.models.Model
    """
    preprocess_input = tf.keras.applications.efficientnet.preprocess_input
    base_model = tf.keras.applications.EfficientNetB2(
        include_top=False, weights=None, input_shape=input_size
    )
    base_model.trainable = True

    inpt = tf.keras.Input(shape=input_size)
    inpt_pre = preprocess_input(inpt)
    # --------------------------------------------
    out_base = base_model(inpt_pre)
    # --------------------------------------------
    x = tf.keras.layers.GlobalAveragePooling2D()(out_base)
    # x = tf.keras.layers.Dropout(0.1)(x)
    # x = tf.keras.layers.Dense(512, activation='tanh')(x)
    # x = tf.keras.layers.Dropout(0.1)(x)
    # x = tf.keras.layers.Dense(256, activation='tanh')(x)
    # x = tf.keras.layers.Dropout(0.1)(x)
    # x = tf.keras.layers.Dense(256, activation='tanh')(x)
    out = tf.keras.layers.Dense(num_class, activation=__activation__[mode])(x)
    model = tf.keras.Model(inpt, out)

    # --------------------------------------------
    if weights is not None:
        model.load_weights(weights)
    # --------------------------------------------
    if fine_tune_layer > 0:
        base_model = model.layers[3]
        base_model.trainable = True
        for i in range(fine_tune_layer):
            base_model.layers[i].trainable = False
    # --------------------------------------------

    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss=__loss__[mode],
        metrics=[
            "accuracy",
            tf.keras.metrics.Precision(name="Precision"),
            tf.keras.metrics.Recall(name="Recall"),
        ],
    )
    model.summary()
    return model


if __name__ == "__main__":
    # model = resnet_cnn( (255,255,3), num_class=5, mode=BINARY, fine_tune_layer=100 )
    # model = efficientnetb2_base_cnn((128, 800, 3), num_class=1, mode=BINARY)
    model = xception_cnn((256,256,3),fine_tune_layer=1)
    end = True
