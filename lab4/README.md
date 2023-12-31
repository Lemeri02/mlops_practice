## MLOps. Практическое задание №4




1. Настройка git и dvc

Установил git и dvc

```
sudo apt install git
```

```
pip install dvc
pip install "dvc[gdrive]
```

```
git init
dvc init
```

```
python3 create_dataset.py
```

```
dvc add titanic.csv
git add titanic.csv.dvc .gitignore
git commit -m "Add initial Titanic dataset"
dvc push
```

### Модификация датасета 1: заполнение пропущенных значений

Заполним пропущенные значения в поле "Age" средним значением:
```bash
python modify_dataset.py
```
Снова делаем коммит в git и dvc:
```bash
dvc add titanic.csv
git add titanic.csv.dvc
git commit -m "Fill missing age"
dvc push
```

### Модификация датасета 2: cоздание нового признака с использованием one-hot-encoding

```bash
python modify2_dataset.py
```

Коммитим изменения:
```bash
dvc add titanic.csv
git add titanic.csv.dvc
git commit -m "one-hot encoding to sex column"
dvc push
```
