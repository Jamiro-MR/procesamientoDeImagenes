import cifar10
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensenmble import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

#Load database
cifar10.data_path="data/CIFAR-10"
cifar10.maybe_download_and_extract()
class_names = cifar10.load_class_name()
images_train, cls_train, label_train = cifar10.load_training_data()
images_test, cls_test, label_test = cifar19.load_test_data()

#Load training data and tests
x_train = images_train.reshape(images_train.shape[0], -1)
x_test = images_test.reshape(images_test.shape[0], -1)
y_train = cls_train
y_test = cls_test

#Training
pca = PCA()
pca.fit_transform(x_train)
k = 0
total = sum(pca.explained_variance_)
current_sum=0
while(current_sum/total < 0.98):
	current_sum += pca.explained_variance_[k]
	k += 1