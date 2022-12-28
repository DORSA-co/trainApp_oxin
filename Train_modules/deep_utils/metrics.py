## Initializing Metrics.py
import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.metrics as metrics
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


class BIN_Metrics():
    """This is a class that computes some metrics for our deep learning models.

    :param threshold: Threshold by witch convert predicted label to zero or one. Defaults to 0.5, defaults to 0.5.
    :type threshold: float, optional
    """
    def __init__(self, threshold=0.5): 
        """Constructor method.
        """ 
        # Set threshold
        self.__threshold = threshold

    def True_Pos(self, y_true, y_pred):
        """Compute True Positive.

        :param y_true: True label of samples.
        :type y_true: array
        :param y_pred: Predicted label of samples.
        :type y_pred: array
        :return: Computed True Positive.
        :rtype: int
        """
        # Convert y_pred to zero or one using given threshold
        y_pred = tf.math.floor(
            (tf.math.sign(y_pred - self.__threshold) + 1) / 2
        )
        return tf.reduce_sum(y_pred, axis=[-1, -2, -3])
        metered = tf.multiply(y_true, y_pred)
        true_pos_count = tf.reduce_sum(metered, axis=[-1, -2, -3])
        return true_pos_count
        all_ = tf.reduce_sum(y_true)
        return tf.math.divide_no_nan(true_pos_count, all_)

    def True_Neg(self, y_true, y_pred):
        """Compute True Negative.

        :param y_true: True label of samples.
        :type y_true: array
        :param y_pred: Predicted label of samples.
        :type y_pred: array
        :return: Computed True Negative.
        :rtype: int
        """
        # Convert y_pred to zero or one using given threshold
        y_pred = tf.math.floor(
            (tf.math.sign(y_pred - self.__threshold) + 1) / 2
        )

        y_true = 1 - y_true
        y_pred = 1 - y_pred

        metered = tf.multiply(y_true, y_pred)
        true_neg_count = tf.reduce_sum(metered, axis=[-1, -2, -3])
        return true_neg_count
        all_ = tf.reduce_sum(y_true)
        return tf.math.divide_no_nan(true_neg_count, all_)

    def False_Pos(self, y_true, y_pred):
        """Compute False Positive.

        :param y_true: True label of samples.
        :type y_true: array
        :param y_pred: Predicted label of samples.
        :type y_pred: array
        :return: Computed False Positive.
        :rtype: int
        """
        # Convert y_pred to zero or one using given threshold
        y_pred = tf.math.floor(
            (tf.math.sign(y_pred - self.__threshold) + 1) / 2
        )

        metered = (1 - y_true) * y_pred
        false_pos_count = tf.reduce_sum(metered, axis=[-1, -2, -3])

        return false_pos_count
        all_ = tf.reduce_sum(y_true)
        return tf.math.divide_no_nan(false_pos_count, all_)

    def False_Neg(self, y_true, y_pred):
        """Compute False Negative.
        :param y_true: True label of samples.
        :type y_true: array
        :param y_pred: Predicted label of samples.
        :type y_pred: array
        :return: Computed False Negative.
        :rtype: int
        """
        # Convert y_pred to zero or one using given threshold
        y_pred = tf.math.floor(
            (tf.math.sign(y_pred - self.__threshold) + 1) / 2
        )

        metered = y_pred * (1 - y_pred)
        false_neg_count = tf.reduce_sum(metered, axis=[-1, -2, -3])

        return false_neg_count
        return tf.math.divide_no_nan(false_neg_count, all_)

    def recall(self, y_true, y_pred):
        """Compute Recall metric using TP and FN.
        :param y_true: True label of samples.
        :type y_true: array
        :param y_pred: Predicted label of samples.
        :type y_pred: array
        :return: Computed Recall.
        :rtype: int
        """
        tp = self.True_Pos(y_true, y_pred)
        fn = self.False_Neg(y_true, y_pred)
        return tf.reduce_mean(tf.math.divide_no_nan(tp, (tp + fn)))

    def precision(self, y_true, y_pred):
        """Compute Precision metric using TP and FP.
        :param y_true: True label of samples.
        :type y_true: array
        :param y_pred: Predicted label of samples.
        :type y_pred: array
        :return: Computed Precision.
        :rtype: int
        """
        tp = self.True_Pos(y_true, y_pred)
        fp = self.False_Pos(y_true, y_pred)
        return tf.math.divide_no_nan(tp, (tp + fp))

    def specificity(self, y_true, y_pred):
        """Compute Specificity metric using TN and FP.
        :param y_true: True label of samples.
        :type y_true: array
        :param y_pred: Predicted label of samples.
        :type y_pred: array
        :return: Computed Specificity.
        :rtype: int
        """
        tn = self.True_Neg(y_true, y_pred)
        fp = self.False_Pos(y_true, y_pred)
        return tf.reduce_mean(tf.math.divide_no_nan(tn, tn + fp))

    def acc(self, y_true, y_pred):
        """Compute Accuracy metric using TP, TN, FP and FN.
        :param y_true: True label of samples.
        :type y_true: array
        :param y_pred: Predicted label of samples.
        :type y_pred: array
        :return: Computed Accuracy.
        :rtype: int
        """
        tn = self.True_Neg(y_true, y_pred)
        fn = self.False_Neg(y_true, y_pred)
        tp = self.True_Pos(y_true, y_pred)
        fp = self.False_Pos(y_true, y_pred)
        return tf.reduce_mean(tf.math.divide_no_nan(tn + tp, tn + tp + fp + fn))


def iou(threshold=0.5):
    """Return a function that compute iou metrics.

    :param threshold: Threshold by witch convert predicted label to zero or one, defaults to 0.5.
    :type threshold: float, optional
    :return: A function that compute iou metrics.
    :rtype: function
    """
    def __iou__(y_true, y_pred):
        """Compute the Intersection over Union (IoU) metrics.

        :param y_true: True label of samples.
        :type y_true: array
        :param y_pred: Predicted label of samples.
        :type y_pred: array
        :return: Computed IoU.
        :rtype: int
        """
        # Convert y_pred to zero or one using given threshold
        y_pred = tf.math.floor(
            (tf.math.sign(y_pred - threshold) + 1) / 2
        )

        # Compute intersection
        unity = y_pred * y_true
        # Compute union
        union = tf.maximum(y_pred, y_true)

        unity_area = tf.reduce_sum(unity, axis=[-1, -2, -3])
        union_area = tf.reduce_sum(union, axis=[-1, -2, -3])

        iou = tf.math.divide_no_nan(unity_area, union_area)
        return tf.reduce_mean(iou)

    return __iou__


if __name__ == '__main__':
    metric = BIN_Metrics()
    yt = np.array([[0, 0, 1],
                   [0, 1, 0],
                   [1, 1, 0]])
    yt = np.reshape(yt, (1, 3, 3, 1))

    yp = np.array([[0, 0.7, 0.6],
                   [0, 0.4, 0.1],
                   [0.9, 0.8, 0]])

    yp = np.reshape(yp, (1, 3, 3, 1))
    # yt = np.random.randint(0,2, 128*800)
    # yt = np.reshape(yt, (1,10,10,1))
    # yp = np.random.randint(1.128,800,1)
    print(metric.True_Pos(yt, yp))

'''
data_ = np.random.rand( 100, 8 )
print(data_)
label_ = np.sum(data_ , axis= 1)
print(label_)
model = Sequential()
model.add(Dense(20 , input_dim=8 , activation='relu'))
model.add(Dense(20 , activation='relu'))
model.add(Dense(20 , activation='relu'))
model.add(Dense(1 , activation='sigmoid'))

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=[
        'accuracy' ,
        BIN_Metrics(0.7).False_Neg ,
        BIN_Metrics(0.7).False_Pos ,
        BIN_Metrics(0.7).True_Neg ,
        BIN_Metrics(0.7).True_Pos ,
        ])

model.fit(data_, label_, epochs=10, batch_size=1)
'''

# yt = [[0, 0, 0, 0],[1,1,0,0],[0,  0,0,  0],[1,   0,0,1]]
# yp = [[1, 1, 0, 1],[0,1,0,0],[0.9,0,0.2,0],[0.88,0,0,0]]
# yt = tf.constant(yt)
# yp = tf.constant(yp)

# binm = BIN_Metrics()
# print(binm.False_Neg( yt , yp))
# print(binm.False_Pos(yt , yp))
# print(binm.True_Neg(yt , yp))
# print(binm.True_Pos(yt , yp))


# class BIN_TruePos(Metric):

#     def __init__(self, name = 'Binary_true_positives' ,  **kwargs):

#         super(BIN_TruePos , self).__init__(name = name , **kwargs)
