from django.http.response import HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import TestSerializer
from .models import TestModel
from .tasks import test_funk

# Create your views here.
def test(request):
    test_funk.delay()
    return HttpResponse("Done")

class TestListView(APIView):
    def get(self, request,*args,**kwargs):
        objects = TestModel.objects.all()
        serializer = TestSerializer(objects,many=True)
        response = Response(serializer.data)
        return response