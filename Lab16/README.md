 
# Лабораторна робота №16: Розширений список TODO

## Мета роботи

Метою даної лабораторної роботи є створення класів `Task` і `Schedule` для управління завданнями та їх розкладом, а також реалізація методів для додавання, видалення, оновлення завдань та інших операцій з ними.

## Опис завдання

В рамках лабораторної роботи необхідно реалізувати наступні класи та методи:

1. Клас `Task` для опису завдання.
2. Клас `Schedule` для управління списком завдань.
3. Методи для додавання, видалення, оновлення завдань, а також для виконання різних операцій над ними (наприклад, сортування, фільтрація, пошук, тощо).

## Виконання роботи

### Структура проекту

- **labY/**
  - `main.py` - Основний код програми
  - `README.md` - Документація проекту

### Опис основних файлів

#### main.py

Містить реалізації наступних класів та методів:

```python
from datetime import date, datetime, timedelta

class Task:
    def __init__(self, title: str, description: str, due_date: date, priority: str = "Medium", notes: str = "",
                 duration: int = 0, recurrence: str = "", status: str = "Pending", dependencies: list = []):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence
        self.status = status
        self.dependencies = dependencies

    def is_due_today(self) -> bool:
        return self.due_date == date.today()


class Schedule:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task_title: str):
        for task in self.tasks:
            if task.title == task_title:
                self.tasks.remove(task)
                break

    def get_task(self, task_title: str) -> Task:
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None

    def list_overdue_tasks(self) -> list:
        return [task for task in self.tasks if task.due_date < date.today()]

    def list_tasks_due_today(self) -> list:
        return [task for task in self.tasks if task.is_due_today()]

    def sort_tasks_by_due_date(self) -> list:
        return sorted(self.tasks, key=lambda task: task.due_date)

    def update_task(self, task_title: str, **kwargs):
        task = self.get_task(task_title)
        if task:
            for key, value in kwargs.items():
                setattr(task, key, value)

    def weekly_schedule(self, start_date: date) -> list:
        end_date = start_date + timedelta(days=7)
        return [task for task in self.tasks if start_date <= task.due_date < end_date]

    def monthly_schedule(self, year: int, month: int) -> list:
        first_day = date(year, month, 1)
        last_day = date(year, month + 1, 1) - timedelta(days=1)
        return [task for task in self.tasks if first_day <= task.due_date <= last_day]

    def list_tasks_by_priority(self, priority: str) -> list:
        return [task for task in self.tasks if task.priority == priority]

    def save_to_file(self, filename: str):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(
                    f"{task.title},{task.description},{task.due_date},{task.priority},{task.notes},{task.duration},{task.recurrence},{task.status},{';'.join([dep.title for dep in task.dependencies])}\n")

    def load_from_file(self, filename: str):
        self.tasks = []
        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                title = task_data[0]
                description = task_data[1]
                due_date = datetime.strptime(task_data[2], "%Y-%m-%d").date()
                priority = task_data[3]
                notes = task_data[4]
                duration = int(task_data[5])
                recurrence = task_data[6]
                status = task_data[7]
                dependencies = [self.get_task(dep_title) for dep_title in task_data[8].split(";") if dep_title]
                task = Task(title, description, due_date, priority, notes, duration, recurrence, status, dependencies)
                self.add_task(task)

    def list_tasks_with_notes(self) -> list:
        return [task for task in self.tasks if task.notes]

    def mark_as_completed(self, task_title: str):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"

    def list_completed_tasks(self) -> list:
        return [task for task in self.tasks if task.status == "Completed"]

    def find_task_by_keyword(self, keyword: str) -> list:
        return [task for task in self.tasks if
                keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]

    def check_deadlines(self) -> list:
        return [task for task in self.tasks if task.due_date == date.today() + timedelta(days=1)]

    def list_all_tasks(self) -> list:
        return self.tasks

    def list_tasks_by_duration(self, min_duration: int, max_duration: int) -> list:
        return [task for task in self.tasks if min_duration <= task.duration <= max_duration]

    def task_history(self) -> list:
        history = []
        for task in self.tasks:
            if task.status == "Completed":
                history.append(("completed", task))
            elif task.status == "Pending":
                history.append(("added", task))
            else:
                history.append(("updated", task))
        return history

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]

    def list_recurring_tasks(self) -> list:
        return [task for task in self.tasks if task.recurrence]

    def set_reminder(self, task_title: str, reminder_date: date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date

    def completion_percentage(self) -> float:
        if not self.tasks:
            return 0.0
        completed_tasks = len(self.list_completed_tasks())
        total_tasks = len(self.tasks)
        return (completed_tasks / total_tasks) * 100
```

### Опис основних класів та методів 

- `clear_completed_tasks`: Видаляє всі завдання зі статусом "Completed".
- `list_recurring_tasks`: Повертає список завдань, що повторюються.
- `set_reminder`: Встановлює дату нагадування для завдання.
- `completion_percentage`: Обчислює відсоток виконаних завдань.

## Інструкція з використання

1. **Імпорт необхідних модулів**:
   ```python
   from datetime import date, datetime, timedelta
   ```

2. **Створення екземпляру класу `Task`**:
   ```python
   task1 = Task(
       title="Task 1",
       description="Description for Task 1",
       due_date=date(2024, 6, 25),
       priority="High",
       notes="This is an important task.",
       duration=60,
       recurrence="weekly",
       status="Pending",
       dependencies=[]
   )
   ```

3. **Створення екземпляру класу `Schedule` та додавання завдань**:
   ```python
   schedule = Schedule()
   schedule.add_task(task1)
   
   task2 = Task(
       title="Task 2",
       description="Description for Task 2",
       due_date=date(2024, 6, 20),
       priority="Medium",
       notes="This is a less important task.",
       duration=30,
       recurrence="",
       status="Pending",
       dependencies=[task1]
   )
   schedule.add_task(task2)
   ```

4. **Операції з розкладом завдань**:
   - **Видалення завдання**:
     ```python
     schedule.remove_task("Task 2")
     ```
   - **Отримання завдання за заголовком**:
     ```python
     task = schedule.get_task("Task 1")
     ```
   - **Список прострочених завдань**:
     ```python
     overdue_tasks = schedule.list_overdue_tasks()
     ```
   - **Список завдань, які мають бути виконані сьогодні**:
     ```python
     today_tasks = schedule.list_tasks_due_today()
     ```
   - **Сортування завдань за датою виконання**:
     ```python
     sorted_tasks = schedule.sort_tasks_by_due_date()
     ```
   - **Оновлення завдання**:
     ```python
     schedule.update_task("Task 1", description="Updated description for Task 1")
     ```
   - **Тижневий розклад**:
     ```python
     weekly_tasks = schedule.weekly_schedule(date.today())
     ```
   - **Місячний розклад**:
     ```python
     monthly_tasks = schedule.monthly_schedule(2024, 6)
     ```
   - **Список завдань за пріоритетом**:
     ```python
     high_priority_tasks = schedule.list_tasks_by_priority("High")
     ```

5. **Збереження та завантаження списку завдань з файлу**:
   - **Збереження**:
     ```python
     schedule.save_to_file("tasks.txt")
     ```
   - **Завантаження**:
     ```python
     schedule.load_from_file("tasks.txt")
     ```

6. **Інші корисні методи**:
   - **Список завдань з нотатками**:
     ```python
     tasks_with_notes = schedule.list_tasks_with_notes()
     ```
   - **Позначення завдання як виконаного**:
     ```python
     schedule.mark_as_completed("Task 1")
     ```
   - **Список виконаних завдань**:
     ```python
     completed_tasks = schedule.list_completed_tasks()
     ```
   - **Пошук завдання за ключовим словом**:
     ```python
     keyword_tasks = schedule.find_task_by_keyword("important")
     ```
   - **Перевірка дедлайнів**:
     ```python
     deadline_tasks = schedule.check_deadlines()
     ```
   - **Список всіх завдань**:
     ```python
     all_tasks = schedule.list_all_tasks()
     ```
   - **Список завдань за тривалістю**:
     ```python
     duration_tasks = schedule.list_tasks_by_duration(30, 60)
     ```
   - **Історія завдань**:
     ```python
     task_history = schedule.task_history()
     ```
   - **Очищення виконаних завдань**:
     ```python
     schedule.clear_completed_tasks()
     ```
   - **Список повторюваних завдань**:
     ```python
     recurring_tasks = schedule.list_recurring_tasks()
     ```
   - **Встановлення нагадування для завдання**:
     ```python
     schedule.set_reminder("Task 1", date(2024, 6, 24))
     ```
   - **Відсоток виконаних завдань**:
     ```python
     completion_percentage = schedule.completion_percentage()
     ```

## Висновки

Ця лабораторна робота допомагає зрозуміти та реалізувати базові операції управління завданнями та розкладом, включаючи додавання, видалення, оновлення завдань, фільтрацію, сортування та інші корисні функції. Реалізований проект може бути розширений для підтримки більш складних сценаріїв, включаючи інтеграцію з календарями, нагадуваннями та іншими системами управління часом.

## Інструкції з запуску

Для запуску програми необхідно мати встановлену версію Python 3.6 або вище. Щоб виконати програму, використовуйте наступну команду:

```sh
python main.py
```

Необхідні бібліотеки:
- datetime
