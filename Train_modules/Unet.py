# ________________________________________________________________________
# change working directory to: Home/Documents/model
from email.policy import default
import os
import sys

import pecan

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
# ________________________________________________________________________
try:
    from Train_modules.model import KerasClsBaseModel
except:
    from model import KerasClsBaseModel
import segmentation_models as sm


sm.set_framework("tf.keras")
sm.framework()


class unet(KerasClsBaseModel):
    """UNET model based on Unet architecture for Keras segmentation models

    Parameters
    ----------
    KerasClsBaseModel : _type_
        _description_
    """

    def __init__(
        self,
        backbone_name="efficientnetb2",
        input_shape=(None, None, 3),
        classes=1,
        activation="sigmoid",
        weights=None,
        encoder_weights="imagenet",
        encoder_freeze=True,
        decoder_use_batchnorm=False,
        encoder_features="default",
        # dropout_rate=None,
        decoder_block_type="upsampling",
        decoder_filters=(256, 128, 64, 32, 16),
        # pyramid_block_filters=256,
        # pyramid_use_batchnorm=True,
        # pyramid_aggregation="concat",
        # downsample_factor=8,
        # psp_conv_filters=512,
        # psp_pooling_type="avg",
    ):
        self.encoder_features = encoder_features
        self.decoder_block_type = decoder_block_type
        self.decoder_filters = decoder_filters
        super().__init__(
            backbone_name=backbone_name,
            input_shape=input_shape,
            classes=classes,
            activation=activation,
            weights=weights,
            encoder_weights=encoder_weights,
            encoder_freeze=encoder_freeze,
            decoder_use_batchnorm=decoder_use_batchnorm,
            # encoder_features,
            # dropout_rate,
            # decoder_block_type,
            # decoder_filters,
            # pyramid_block_filters,
            # pyramid_use_batchnorm,
            # pyramid_aggregation,
            # downsample_factor,
            # psp_conv_filters,
            # psp_pooling_type,
        )

    def build(
        self,
        backbone_name="efficientnetb2",
        input_shape=(None, None, 3),
        classes=1,
        activation="sigmoid",
        weights=None,
        encoder_weights="imagenet",
        encoder_freeze=True,
        decoder_use_batchnorm=False,
        # encoder_features="default",
        # dropout_rate=None,
        # decoder_block_type="upsampling",
        # decoder_filters=(256, 128, 64, 32, 16),
        # pyramid_block_filters=256,
        # pyramid_use_batchnorm=True,
        # pyramid_aggregation="concat",
        # downsample_factor=8,
        # psp_conv_filters=512,
        # psp_pooling_type="avg",
    ):
        # print("69" * 69)
        # print("in model", encoder_weights)
        # print("in model", decoder_use_batchnorm)
        # print("in model", encoder_freeze)
        # print("in model", backbone_name)
        # print("in model", activation)
        # print("69" * 69)
        model = sm.Unet(
            backbone_name=backbone_name,
            input_shape=input_shape,
            classes=classes,
            activation=activation,
            weights=weights,
            encoder_weights=encoder_weights,
            encoder_freeze=encoder_freeze,
            encoder_features=self.encoder_features,
            decoder_block_type=self.decoder_block_type,
            decoder_filters=self.decoder_filters,
            decoder_use_batchnorm=decoder_use_batchnorm,
        )
        return model
