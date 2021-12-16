from celery import shared_task
from .models import testmodel

@shared_task
def test_funk():
    
    for i in range(1,6):
        print(i)
    testmodel.objects.create(name='testname',value=f'testvalue{i}')
    for i in testmodel.objects.all():
        print(i.id)
    return 'Done'