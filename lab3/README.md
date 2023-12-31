## MLOps. Практическое задание №3

Запуск проекта 

Склонировать репозиторий
```commandline
git clone https://github.com/Lemeri02/mlops_practice.git
```

Перейти в директорию практического задания №3
```commandline
cd mlops_practice/lab3
```

Запустить сборку docker-compose
```commandline
docker-compose build
```

Запустить проект 
```commandline
docker-compose up -d
```

Остановить проект
```commandline
docker-compose stop
```

Модель классификации текста 
https://huggingface.co/cointegrated/rubert-tiny-toxicity

Эта модель является дообученной версией модели cointegrated/rubert-tiny, настроенной для классификации токсичности и неприемлемости коротких неформальных текстов на русском языке, таких как комментарии в социальных сетях.

Проблема формулируется как многоклассовая классификация со следующими классами:

- non-toxic - нетоксичный: текст НЕ содержит оскорблений, нецензурной брани и угроз в смысле соревнования OK ML Cup.
- insult - оскорбление
- obscenity - нецензурная брань
- threat - угроза
- dangerous - опасный: текст неприемлем согласно [Babakov и др.](https://arxiv.org/abs/2103.05345), то есть он может нанести вред репутации говорящего.

Текст считается безопасным, если он одновременно и нетоксичен, и не представляет опасности.

Пример работы с программой:

После запуска контейнера отправляем POST запрос через curl или другим инструментом:

Пример с косвенной угрозой:

```commandline
curl -X POST http://localhost/predict -H "Content-Type: application/json" -d '{"text": "Жду с нетерпением твоего следующего гениального шага, умник"}'
```

Пример ответа:

```commandline
{"prediction":{"non-toxic":0.98748,"insult":0.01479,"obscenity":0.00017,"threat":0.00066,"dangerous":0.70522}}
```