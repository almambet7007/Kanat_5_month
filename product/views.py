from rest_framework.decorators import api_view
from rest_framework.response import  Response
from rest_framework import status

from product.models import Category

@api_view(['GET'])
def test_api_view(request):
    dict_ = {
        "key" : "value",
        'int' : 100,
        'float' : 34.3
    }
    return Response(data=dict_, status=status.HTTP_409_CONFLICT)

@api_view(['GET'])
def category_api_view(request):
    category = Category.objects.all()
    return Response(data=category, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def category_detail_api_view(request, id):
    category = Category.objects.get(id=id)
    return Response(data=category, status=status.HTTP_409_CONFLICT)
