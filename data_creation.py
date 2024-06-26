# -*- coding: utf-8 -*-
"""data_creation

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1md93J01GOj8wrq4iMBZ6sKx-TuAMzGp7
"""

import numpy as np
import os

# Создание папок "train" и "test"
os.makedirs("train", exist_ok=True)
os.makedirs("test", exist_ok=True)

# Создание и сохранение наборов данных в папки "train" и "test"
# Например, генерация случайных данных
train_data = np.random.rand(100, 2)
test_data = np.random.rand(50, 2)

np.save("train/train_data.npy", train_data)
np.save("test/test_data.npy", test_data)