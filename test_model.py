from Train_modules.models import resnet_cnn,BINARY,CATEGORICAL
import cv2
import numpy as np
import os
from tensorflow import one_hot
import matplotlib.pyplot as plt
from tensorflow.keras.metrics import Accuracy 
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score




perfect_path=r'default_dataset\binary\perfect'
defect_path=r'default_dataset\binary\defect'

perfect_paths=os.listdir(perfect_path)
defect_paths=os.listdir(defect_path)


#train________________________________
train_input_list=[]
for file in perfect_paths[0:4]:
    path=os.path.join(perfect_path,file)
    img=cv2.imread(path)
    img=cv2.resize(img,(1600,256))
    train_input_list.append(img)

for file in defect_paths[0:4]:
    path=os.path.join(defect_path,file)
    img=cv2.imread(path)
    img=cv2.resize(img,(1600,256))
    train_input_list.append(img)


train_input_img=np.array(train_input_list)
train_output_list = [0,1,2,2]
depth =3
out=one_hot(train_output_list, depth)
perfect_out=np.zeros((4,3),dtype=np.uint8)
train_output_label=np.concatenate((out,perfect_out),axis=0)


#validtion________________________________
val_input_list=[]
for file in perfect_paths[4:6]:
    path=os.path.join(perfect_path,file)
    img=cv2.imread(path)
    img=cv2.resize(img,(1600,256))
    val_input_list.append(img)

for file in defect_paths[4:6]:
    path=os.path.join(defect_path,file)
    img=cv2.imread(path)
    img=cv2.resize(img,(1600,256))
    val_input_list.append(img)


val_input_img=np.array(val_input_list)
val_output_list = [2,1,]
depth =3
out=one_hot(val_output_list, depth)
perfect_out=np.zeros((2,3),dtype=np.uint8)
val_output_label=np.concatenate((out,perfect_out),axis=0)





# #print(train_input_img.shape)
# #print(train_output_label.shape)


# #print(val_input_img.shape)
# #print(val_output_label.shape)




classifing_model=resnet_cnn(input_size=(256,1600,3), learning_rate=1e-3, num_class=3, mode=CATEGORICAL)
# #print(classifing_model.layers[-1].output.shape[1])
# classifing_model.fit(x=train_input_img,y=train_output_label, epochs=2,validation_data=(val_input_img,val_output_label),)
l=[100, 104, 122, 123, 124, 128]
# #print((4 in l))
# #print(l)
# thresh=0.2
# pred=classifing_model.predict(val_input_img)
# pred=(pred > thresh).astype('int32')


# acc_=accuracy_score(val_output_label, pred)
# precision_=precision_score(y_true=val_output_label, y_pred=pred,average='micro')
# recall_=recall_score(y_true=val_output_label, y_pred=pred,average='micro')
# f1_=f1_score(y_true=val_output_label, y_pred=pred,average='micro')


# #print(acc_)
# #print(precision_)
# #print(recall_)
# #print(f1_)

x=[]
x.extend([[1]]*3)
# #print(x)
x.extend([[1]]*3)
# #print(x)
x.append([0])
# #print(x)


# #print(val_output_label)
# #print('----------------------------------------------')
# #print(pred)


