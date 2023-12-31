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