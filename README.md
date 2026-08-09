# QA Engineering Lab

Практический проект по автоматизации тестирования REST API на Python. Репозиторий показывает базовую архитектуру тестового фреймворка: отдельный API client, конфигурацию через environment variables, pytest fixtures, позитивные и негативные проверки и запуск в GitHub Actions.

## Что реализовано

- REST API testing с `pytest` и `requests`;
- переиспользуемый `ApiClient` с timeout и обработкой URL;
- конфигурация через environment variables без credentials в коде;
- параметризованные smoke-проверки;
- позитивные и негативные сценарии для ресурса `/posts`;
- автоматический запуск тестов и Ruff в GitHub Actions.

Тестовым объектом по умолчанию служит публичный сервис [JSONPlaceholder](https://jsonplaceholder.typicode.com/). Он предназначен для учебных запросов: операции изменения данных эмулируются и не сохраняются на сервере.

## Структура

```text
qa-engineering-lab/
├── .github/workflows/quality.yml
├── framework/
│   ├── clients/api_client.py
│   └── config/settings.py
├── tests/
│   ├── api/test_posts.py
│   └── conftest.py
├── .env.example
├── pyproject.toml
├── pytest.ini
└── requirements.txt
```

## Быстрый запуск

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest
```

Проверка стиля:

```bash
ruff check .
```

## Конфигурация

Значения по умолчанию подходят для запуска без секретов. При необходимости можно изменить endpoint:

```bash
export API_BASE_URL="https://jsonplaceholder.typicode.com"
export API_TIMEOUT_SECONDS="10"
pytest
```

Пример переменных находится в `.env.example`. Файл `.env` не должен попадать в Git.

## Roadmap

- schema validation;
- Allure reporting;
- PostgreSQL integration tests;
- Kafka consumer/producer tests;
- Docker Compose test environment.
