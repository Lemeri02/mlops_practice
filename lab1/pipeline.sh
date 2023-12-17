#!/bin/bash
# Добавляем bash-скрипту режим исполнения:
# sudo chmod +x pipeline.sh
# ls -la
# Создать виртуальное окружение:
# python -m venv myenv
# source myenv/bin/activate
# Установить зависимости:
# pip install -r requirements.txt

# Запускаем скрипт из текущего каталога:
# ./pipeline.sh

python ./data_creation.py
python ./data_preprocessing.py
python ./model_preparation.py
python ./model_testing.py
