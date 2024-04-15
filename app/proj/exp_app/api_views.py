from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.response import Response

from .models import StreamingVariable
from .serializers import StreamingVariableSerializer
import json

@api_view(['GET'])
def example(request):
    return Response("Hello World")
