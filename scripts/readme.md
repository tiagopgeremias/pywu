# django-extensions

## Example

```python
# scripts/delete_all_questions.py

from polls.models import Question

def run():
    # Fetch all questions
    questions = Question.objects.all()
    # Delete questions
    questions.delete()
```

## Execute

```sh
python manage.py runscript delete_all_questions
```