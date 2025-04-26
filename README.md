# Steam Tests 

**Steam Tests**  — это набор автоматизированных тестов для веб-платформы Steam, разработанный с использованием `pytest` и `Selenium WebDriver`.​

## Структура проекта 

 
- `pages/` — реализация паттерна Page Object для различных страниц Steam.
 
- `tests/` — тестовые сценарии, написанные с использованием `pytest`.
 
- `utils/` — вспомогательные модули, включая конфигурации и инициализацию WebDriver.
 
- `conftest.py` — общие фикстуры для тестов.​


##  Установка и запуск 

 
2. Установите зависимости:​


```bash
pip install -r requirements.txt
```
 
4. Запустите тесты:​[GitHub](https://github.com/riscv-software-src/riscv-tests?utm_source=chatgpt.com) 


```bash
pytest
```


## Конфигурация 

Файл `utils/config.json` содержит настройки, такие как URL-адреса и параметры браузера.​

## Используемые технологии 

 
- Python
 
- pytest
 
- Selenium WebDriver
