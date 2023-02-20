from abc import ABC
from tensorflow.keras.optimizers import Adam


class BaseModel(ABC):
    def __init__(self):
        pass

    def build(self):
        raise NotImplementedError()

    def load_imagenet_weights(self):
        raise NotImplementedError()

    def train(
        self,
        metrics,
        callbacks,
        epochs,
        loss,
        optimizer,
        train_data_loader=None,
        validation_data_loader=None,
        X=None,
        Y=None,
        X_val=None,
        Y_val=None,
        batch_size=32,
        **kwargs,
    ):
        raise NotImplementedError()

    def evaluate(
        self,
        loss,
        metrics,
        test_data_loader=None,
        X=None,
        Y=None,
        **kwargs,
    ):
        raise NotImplementedError()

    def predict(self, img, **kwargs):
        raise NotImplementedError()

    def save(self, path, **kwargs):
        # raise NotImplementedError()
        self.model.save(path)

    def load_weights(self, path, **kwargs):
        raise NotImplementedError()

    def summary(self):
        raise NotImplementedError()


class KerasClsBaseModel(BaseModel):
    """A Base Model for Keras segmentation models.

    Parameters
    ----------
    BaseModel : BaseModel OBJ
        base model!!!!!!!!!!!!!!!
    """

    def __init__(
        self,
        # common param for all architectures
        backbone_name="vgg16",
        input_shape=(None, None, 3),
        classes=1,
        activation="sigmoid",
        weights=None,
        encoder_weights="imagenet",
        encoder_freeze=True,
        decoder_use_batchnorm=False,
        # Unet and Linknet and FPN
        # encoder_features="default",
        # FPN and PSPnet:
        # dropout_rate=None,
        # unet and linknet:
        # decoder_block_type="upsampling",
        # decoder_filters=(256, 128, 64, 32, 16),
        # FPN
        # pyramid_block_filters=256,
        # pyramid_use_batchnorm=True,
        # pyramid_aggregation="concat",
        # PSP
        # downsample_factor=8,
        # psp_conv_filters=512,
        # psp_pooling_type="avg",
    ):
        """init function

        Parameters
        ----------
        backbone_name : str, optional
             name of classification model (without last dense layers) used as feature extractor to build segmentation model, by default "vgg16",is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        input_shape : tuple, optional
             shape of input data/image (H, W, C), by default (None, None, 3),is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        classes : int, optional
             a number of classes for output (output shape - (h, w, classes)), by default 1,is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        activation : str, optional
            name of one of keras.activations for last model layer (e.g. sigmoid, softmax, linear)., by default "sigmoid",is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        weights : str, optional
            path to model weights, by default None,is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        encoder_weights : str, optional
            one of None (random initialization), imagenet (pre-training on ImageNet), by default "imagenet",is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        encoder_freeze : bool, optional
             if True set all layers of encoder (backbone model) as non-trainable, by default True,is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        decoder_use_batchnorm : bool, optional
            if True, BatchNormalisation layer between Conv2D and Activation layers is used, by default False,is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        encoder_features : str, optional
           a list of layer numbers or names starting from top of the model. Each of these layers will be concatenated with corresponding decoder block. If default is used layer names are taken from DEFAULT_SKIP_CONNECTIONS, by default "default",is common features between 3 architectures(unet,linknet,FPN)
        dropout_rate :float, optional
            dropout rate between 0 and 1, by default None,is common features between 2 architectures(FPN,PSPnet)
        decoder_block_type : str, optional
            one of blocks with following layers structure:
            upsampling: UpSampling2D -> Conv2D -> Conv2D
            transpose: Transpose2D -> Conv2D, by default "upsampling"
            ,is common features between 3 architectures(unet,linknet)
        decoder_filters : tuple, optional
            list of numbers of Conv2D layer filters in decoder blocks, by default (256, 128, 64, 32, 16),is common features between 2 architectures(unet,linknet)
        pyramid_block_filters : int, optional
            a number of filters in Feature Pyramid Block of FPN., by default 256,is specific for FPN
        pyramid_use_batchnorm : bool, optional
            if True, BatchNormalisation layer between Conv2D and Activation layers is used, by default True,is specific for FPN
        pyramid_aggregation : str, optional
            one of ‘sum’ or ‘concat’. The way to aggregate pyramid blocks, by default 'concat',is specific for FPN
        downsample_factor : int, optional
            one of 4, 8 and 16. Downsampling rate or in other words backbone depth to construct PSP module on it, by default 8,is specific for PSPnet
        psp_conv_filters : int, optional
             number of filters in Conv2D layer in each PSP block., by default 512,is specific for PSPnet
        psp_pooling_type : str, optional
            one of ‘avg’, ‘max’. PSP block pooling type (maximum or average)., by default 'avg',is specific for PSPnet
        """
        # common param for all architectures
        self.backbone_name = backbone_name
        self.input_shape = input_shape
        self.classes = classes
        self.activation = activation
        self.weights = weights
        self.encoder_weights = encoder_weights
        self.encoder_freeze = encoder_freeze
        self.decoder_use_batchnorm = decoder_use_batchnorm
        # Unet and Linknet and FPN
        # self.encoder_features = encoder_features
        # # FPN and PSPnet
        # self.dropout_rate = dropout_rate
        # # unet and linknet
        # self.decoder_block_type = decoder_block_type
        # self.decoder_filters = decoder_filters
        # # FPN
        # self.pyramid_block_filters = pyramid_block_filters
        # self.pyramid_use_batchnorm = pyramid_use_batchnorm
        # self.pyramid_aggregation = pyramid_aggregation
        # # PSP
        # self.downsample_factor = downsample_factor
        # self.psp_conv_filters = psp_conv_filters
        # self.psp_pooling_type = psp_pooling_type

        self.model = self.build(
            # common param for all architectures
            self.backbone_name,
            self.input_shape,
            self.classes,
            self.activation,
            self.weights,
            self.encoder_weights,
            self.encoder_freeze,
            # unet and linknet
            # self.encoder_features,
            # self.decoder_block_type,
            # self.decoder_filters,
            self.decoder_use_batchnorm,
            # # FPN
            # self.pyramid_block_filters,
            # self.pyramid_use_batchnorm,
            # self.pyramid_aggregation,
            # # PSP
            # self.downsample_factor,
            # self.psp_conv_filters,
            # self.psp_pooling_type,
        )

    def build(
        self,
        # common param for all architectures
        backbone_name="vgg16",
        input_shape=(None, None, 3),
        classes=1,
        activation="sigmoid",
        weights=None,
        encoder_weights="imagenet",
        encoder_freeze=True,
        decoder_use_batchnorm=False,
        # Unet and Linknet and FPN
        # encoder_features="default",
        # FPN and PSPnet:
        # dropout_rate=None,
        # unet and linknet:
        # decoder_block_type="upsampling",
        # decoder_filters=(256, 128, 64, 32, 16),
        # # FPN
        # pyramid_block_filters=256,
        # pyramid_use_batchnorm=True,
        # pyramid_aggregation="concat",
        # # PSP
        # downsample_factor=8,
        # psp_conv_filters=512,
        # psp_pooling_type="avg",
    ):
        """init function

        Parameters
        ----------
        backbone_name : str, optional
             name of classification model (without last dense layers) used as feature extractor to build segmentation model, by default "vgg16",is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        input_shape : tuple, optional
             shape of input data/image (H, W, C), by default (None, None, 3),is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        classes : int, optional
             a number of classes for output (output shape - (h, w, classes)), by default 1,is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        activation : str, optional
            name of one of keras.activations for last model layer (e.g. sigmoid, softmax, linear)., by default "sigmoid",is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        weights : str, optional
            path to model weights, by default None,is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        encoder_weights : str, optional
            one of None (random initialization), imagenet (pre-training on ImageNet), by default "imagenet",is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        encoder_freeze : bool, optional
             if True set all layers of encoder (backbone model) as non-trainable, by default True,is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        decoder_use_batchnorm : bool, optional
            if True, BatchNormalisation layer between Conv2D and Activation layers is used, by default False,is common features between 4 architectures(unet,linknet,FPN,PSPnet)
        encoder_features : str, optional
           a list of layer numbers or names starting from top of the model. Each of these layers will be concatenated with corresponding decoder block. If default is used layer names are taken from DEFAULT_SKIP_CONNECTIONS, by default "default",is common features between 3 architectures(unet,linknet,FPN)
        dropout_rate :float, optional
            dropout rate between 0 and 1, by default None,is common features between 2 architectures(FPN,PSPnet)
        decoder_block_type : str, optional
            one of blocks with following layers structure:
            upsampling: UpSampling2D -> Conv2D -> Conv2D
            transpose: Transpose2D -> Conv2D, by default "upsampling"
            ,is common features between 3 architectures(unet,linknet)
        decoder_filters : tuple, optional
            list of numbers of Conv2D layer filters in decoder blocks, by default (256, 128, 64, 32, 16),is common features between 2 architectures(unet,linknet)
        pyramid_block_filters : int, optional
            a number of filters in Feature Pyramid Block of FPN., by default 256,is specific for FPN
        pyramid_use_batchnorm : bool, optional
            if True, BatchNormalisation layer between Conv2D and Activation layers is used, by default True,is specific for FPN
        pyramid_aggregation : str, optional
            one of ‘sum’ or ‘concat’. The way to aggregate pyramid blocks, by default 'concat',is specific for FPN
        downsample_factor : int, optional
            one of 4, 8 and 16. Downsampling rate or in other words backbone depth to construct PSP module on it, by default 8,is specific for PSPnet
        psp_conv_filters : int, optional
             number of filters in Conv2D layer in each PSP block., by default 512,is specific for PSPnet
        psp_pooling_type : str, optional
            one of ‘avg’, ‘max’. PSP block pooling type (maximum or average)., by default 'avg',is specific for PSPnet
        """

        raise NotImplementedError()

    def compile(self, loss, metrics, optimizer=Adam()):
        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def train(
        self,
        epochs,
        callbacks=[],
        train_data_loader=None,
        validation_data_loader=None,
        X=None,
        Y=None,
        X_val=None,
        Y_val=None,
        batch_size=32,
        **kwargs,
    ):
        """train : trains the model by input data

        Parameters
        ----------
        epochs : int
            number of epochs that training process will repeat
        loss : str or keras.loss
            loss function to calculate gradients
        metrics : list
            list of keras.metrics
        callbacks : list, optional
            functions that will execute after each eochs, by default []
        optimizer : keras.optimizer, optional
            optimizer method to optimize learning process, by default Adam()
        train_data_loader : keras data generator, optional
            data loader to give training data sectional, by default None
        validation_data_loader : [type], optional
             data loader to give validation data sectional, by default None
        X : tensor, optional
            input data as a tensor, by default None
        Y : tensor, optional
            labels as a tensor, by default None
        X_val : tensor, optional
            validation input as a tensor, by default None
        Y_val : tensor, optional
            validation labels as a tensor, by default None
        batch_size : int, optional
            number of inputs per each calculation, by default 32

        Returns
        -------
        keras history OBJ
            history of training
        """

        if train_data_loader == None:
            history = self.model.fit(
                x=X,
                y=Y,
                callbacks=callbacks,
                batch_size=batch_size,
                epochs=epochs,
                validation_data=(X_val, Y_val),
                **kwargs,
            )
        else:
            history = self.model.fit(
                x=train_data_loader,
                batch_size=batch_size,
                epochs=epochs,
                validation_data=validation_data_loader,
                callbacks=callbacks,
                **kwargs,
            )

        return history
