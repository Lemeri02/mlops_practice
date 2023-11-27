#!/bin/bash
python3 data_creation.py
python3 data_preprocessing.py
python3 model_preparation.py
python3 model_testing.py


# Добавляем bash-скрипту режим исполнения:
# sudo chmod +x pipeline.sh
# ls -la

# Запускаем скрипт из текущего каталога:
# ./pipeline.sh