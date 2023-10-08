from rest_framework.decorators import api_view
from rest_framework.response import  Response
from rest_framework import status

@api_view(['GET'])
def test_api_view(request):
    dict_ = {
        "key" : "value",
        'int' : 100,
        'float' : 34.3
    }
    return Response(data=dict_, status=status.HTTP_409_CONFLICT)
