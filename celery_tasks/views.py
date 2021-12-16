from django.http.response import HttpResponse

from .tasks import test_funk

# Create your views here.
def test(request):
    test_funk.delay()
    return HttpResponse("Done")
