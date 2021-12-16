from celery import shared_task
from .models import TestModel

@shared_task
def test_funk():
    
    for i in range(1,6):
        print(i)
    TestModel.objects.create(name='testname',value=f'testvalue{i}')
    for i in TestModel.objects.all():
        print(i.id)
    return 'Done'