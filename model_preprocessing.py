# -*- coding: utf-8 -*-
"""model_preprocessing

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1md93J01GOj8wrq4iMBZ6sKx-TuAMzGp7
"""

from sklearn.preprocessing import StandardScaler
import numpy as np

# Загрузка данных
train_data = np.load("train/train_data.npy")

# Пример предобработки данных с использованием StandardScaler
scaler = StandardScaler()
train_data_scaled = scaler.fit_transform(train_data)

# Сохранение предобработанных данных
np.save("train/train_data_scaled.npy", train_data_scaled)