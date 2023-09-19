#### AioStorageORM (CyberPhysics)
[![Upload pypi](https://github.com/CyberPhysics-Platform/aiostorage-orm/actions/workflows/pypi_deploy.yml/badge.svg)](https://github.com/CyberPhysics-Platform/aiostorage-orm/actions/workflows/pypi_deploy.yml)
[![Linting & Pytest](https://github.com/CyberPhysics-Platform/aiostorage-orm/actions/workflows/lint_and_test.yml/badge.svg)](https://github.com/CyberPhysics-Platform/aiostorage-orm/actions/workflows/lint_and_test.yml)
##### Установка
```bash
    pip install aiostorage-orm
```
##### Зависимости
- [redis-py](https://github.com/redis/redis-py)
- [nest-asyncio](https://github.com/erdewit/nest_asyncio)
##### Базовый пример использования ([все примеры](examples/), [базовый пример](examples/redis_1_single.py))
1. Импорт классов
    ```python
        import redis.asyncio as redis

        from aiostorage_orm import AIOStorageORM
        from aiostorage_orm import AIORedisORM
        from aiostorage_orm import AIORedisItem
        from aiostorage_orm import OperationResult
    ```
1. Определить модель
    ```python
        class ExampleItem(AIORedisItem):
            """
                Атрибуты объекта с указанием типа данных
                  (в процессе сбора данных из БД приводится тип)
            """
            date_time: int
            any_value: float

            class Meta:
                """
                    Системный префикс записи в Redis
                    Ключи указанные в префиксе обязательны для
                      передачи в момент создания экземпляра
                """
                table = "subsystem.{subsystem_id}.tag.{tag_id}"
    ```
1. Установить подключение ORM можно двумя способами
    1. Передать данные для подключения непосредственно в ORM
        ```python
            orm: AIOStorageORM = AIORedisORM(host="localhost", port=8379, db=1)
            await orm.init()
        ```
    1. Создать подключение redis.Redis и передать его в конструктор
        ```python
            redis: redis.Redis = redis.Redis(host="localhost", port=8379, db=1)
            orm: AIOStorageORM = AIORedisORM(client=redis)
            await orm.init()
        ```
1. Добавление/редактирование записи (ключами записи являются параметры, указанные в Meta.table модели)
    1. Создать объект на основе модели
        ```python
            example_item: ExampleItem = ExampleItem(
                subsystem_id=3,
                tag_id=15,
                date_time=100,
                any_value=17.
            )
        ```
    1. Выполнить вставку можно несколькими способами
        1. Использовать метод save() созданного экземпляра
            ```python
                operation_result: OperationResult = await example_item.save()
            ```
        1. Использовать метод save() AIOStorageOrm
            ```python
                operation_result: OperationResult = await orm.save(item=example_item)
            ```
        1. Использовать **групповую** вставку записей ([пример групповой вставки](examples/redis_2_bulk_multiple.py))
            ```python
                operation_result: OperationResult = await orm.bulk_create(
                    items=[example_item1, example_item2]
                )
            ```
1. Выборка данных из БД
    - для выборки необходимо передать аргументы для параметров, которые используются в Meta.table
        ```python
            table = "subsystem.{subsystem_id}.tag.{tag_id}"
                                     ^               ^
        ```
        , например
        ```python
            example_items: ExampleItem = await exampleitem.get(subsystem_id=3, tag_id=15)
        ```
1. Использование нескольких подключений ([пример](examples/redis_3_using_multiple_connections.py))
    - для использования нескольких подключений необходимо в метод AIOStorageItem.using(db_instance=...) передать
      подготовленное соединение с БД Redis, например
        ```python
            redis_another: redis.Redis = redis.Redis(host="localhost", port=8379, db=17)
            ...
            result_of_operation: OperationResult = await example_item.using(db_instance=redis_another).save()
        ```
1. Поиск по списку значений ([пример](examples/redis_4_values_in_list.py))
    - для поиска записей по параметру, находящемуся в списке значений, необходимо параметр дополнить суффиксом __in, в
      который необходимо передать список искомых значений
        ```python
            getted_items: list[ExampleItem] = await ExampleItem.filter(subsystem_id__in=[21, 23], tag_id=15)
        ```
1. Поиск по предварительно подготовленному объекту ([пример](examples/redis_5_find_by_object.py))
    - для поиска записи указанным образом, необходимо создать объект с параметрами, необходимыми для поиска и передать
      его в метод AIORedisORM.get
    ```python
        item: ExampleItem = ExampleItem(subsystem_id=1, tag_id=15)
        item_by_object: ExampleItem | None = await ExampleItem.get(_item=item)
    ```
1. Поиск по предварительно подготовленным объектам ([пример](examples/redis_5_find_by_object.py))
    - для поиска записи указанным образом, необходимо создать объекты с параметрами, необходимыми для поиска и передать
      их списком в метод AIORedisORM.filter
    ```python
        items: list[ExampleItem] = [
            ExampleItem(subsystem_id=1, tag_id=15),
            ExampleItem(subsystem_id=2, tag_id=16),
        ]
        item_by_objects: list[ExampleItem] = await ExampleItem.filter(_items=items)
    ```
1. Удаление одного объекта ([пример](examples/redis_6_delete_item.py))
    ```python
        example_item: ExampleItem = ExampleItem(subsystem_id=3, tag_id=15)
        result_of_operation: OperationResult = await example_item.delete()
    ```
1. Удаление нескольких объектов одновременно ([пример](examples/redis_6_delete_item.py))
    ```python
        result_of_operation: OperationResult = await orm.bulk_delete(items=example_items)
    ```
1. Добавление объектов с ограниченным временем жизни ([пример](examples/redis_7_ttl.py))
    ```python
        class ExampleItem(AIORedisItem):
            # Атрибуты объекта с указанием типа данных (в процессе сбора данных из БД приводится тип)
            date_time: int
            any_value: str

            class Meta:
                # Системный префикс записи в Redis
                # Ключи указанные в префиксе обязательны для передачи в момент создания экземпляра
                table = "subsystem.{subsystem_id}.tag.{tag_id}"
                # Время жизни объекта в базе данных
                ttl = 10
        ...
        example_item: ExampleItem = ExampleItem(subsystem_id=3, tag_id=15, date_time=100, any_value=17.)
        result_of_operation: OperationResult = await example_item.save()
        ...
        example_items: list[ExampleItem] = []
        for i in range(100):
            subsystem_id: int = i % 10
            example_item: ExampleItem = ExampleItem(
                subsystem_id=subsystem_id,
                another_key_value=i,
                tag_id=10 + (15 * random.randint(0, 1)),
                date_time=i*100,
                any_value=random.random() * 10,
            )
            example_items.append(example_item)
        result_of_operation: OperationResult = await orm.bulk_create(items=example_items)
    ```
1. Добавление одной записи во фрейм ([пример](examples/redis_8_frame.py))
    ```python
        class ExampleItem(AIORedisItem):
            # Атрибуты объекта с указанием типа данных (в процессе сбора данных из БД приводится тип)
            date_time: int
            any_value: str

            class Meta:
                # Системный префикс записи в Redis
                # Ключи указанные в префиксе обязательны для передачи в момент создания экземпляра
                table = "subsystem.{subsystem_id}.tag.{tag_id}"
                ttl = 10  # Время жизни объекта в базе данных
                frame_size = 3  # Размер frame'а
        ...
        result_of_operation: OperationResult = await orm.frame.add(item_or_items=example_item)
    ```
1. Групповое добавление записей во фрейм ([пример](examples/redis_8_frame.py))
    * записи могут быть разнородными (должны являться наследником AIORedisItem, но при этом они могут быть определены
      различными друг от друга классами)
    ```python
        ...
        result_of_operation: OperationResult = await orm.frame.add(item_or_items=[example_item, example_item_2])
    ```
1. Сбор данных из фрейма ([пример](examples/redis_8_frame.py))
    * данные из фрейма можно получить только списком (list[ExampleItem])
    * получение данных из фрейма ограничивается агрументами start_index и end_index (включительно, т.е. самый старый элемент
      get(ExampleItem(), 0, 0), самый последний добавленный get(ExampleItem(), -1, -1))
    ```python
        ...
        result_of_operation: OperationResult = await orm.frame.get(item=example_item)
    ```
##### Запуск примеров
```bash
    python -m venv venv
    source ./venv/bin/activate
    pip install redis

    # Базовый простой пример
    PYTHONPATH="${PYTHONPATH}:." python examples/redis_1_single.py

    # Пример групповой вставки (bulk)
    PYTHONPATH="${PYTHONPATH}:." python examples/redis_2_bulk_multiple.py

    # Пример использования нескольких подключений
    PYTHONPATH="${PYTHONPATH}:." python examples/redis_3_using_multiple_connections.py

    # Пример поиска по списку значений
    PYTHONPATH="${PYTHONPATH}:." python examples/redis_4_values_in_list.py

    # Пример поиска по переданному подготовленному экземпляру
    PYTHONPATH="${PYTHONPATH}:." python examples/redis_5_find_by_object.py

    # Пример удаления объектов  
    PYTHONPATH="${PYTHONPATH}:." python examples/redis_6_delete_item.py
    
    # Пример добавления объектов с ограниченным временем жизни
    PYTHONPATH="${PYTHONPATH}:." python examples/redis_7_ttl.py
    
    # Пример работы с frame'ами
    PYTHONPATH="${PYTHONPATH}:." python examples/redis_8_frame.py
```
