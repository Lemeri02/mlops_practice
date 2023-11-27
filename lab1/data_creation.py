import numpy as np
import pandas as pd
import os


TRAIN_DATA_PATH='train'
TEST_DATA_PATH='test'
TRAIN_DATA_SIZE=1000
TEST_DATA_SIZE=600


# Создание папок train и test
if not os.path.exists(TRAIN_DATA_PATH):
    os.makedirs(TRAIN_DATA_PATH)
if not os.path.exists(TEST_DATA_PATH):
    os.makedirs(TEST_DATA_PATH)


def create_train_data():
  train_data = pd.DataFrame(generate_random_data(TRAIN_DATA_SIZE))
  train_data['label'] = np.where(train_data['temperature'] > 30, 1, 0)
  train_data.to_csv(f'{TRAIN_DATA_PATH}/train_data.csv', index=False)
  return train_data


def create_test_data():
  test_data = pd.DataFrame(generate_random_data(TEST_DATA_SIZE))
  test_data['label'] = np.where(test_data['temperature'] > 30, 1, 0)
  test_data.to_csv(f'{TEST_DATA_PATH}/test_data.csv', index=False)
  return test_data


def generate_random_data(size):
  data = {
   'temperature': np.random.normal(loc=25, scale=5, size=size),
   'humidity': np.random.normal(loc=50, scale=10, size=size),
   'pressure': np.random.normal(loc=1000, scale=50, size=size)
  }
  return data
   

create_train_data()
create_test_data()