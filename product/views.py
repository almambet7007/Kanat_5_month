from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from product.models import Category


@api_view(['GET'])
def category_api_view(request):
    category = Category.objects.all()
    return Response(data=category, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category).data
    return Response(data=serializer, status=status.HTTP_409_CONFLICT)


@api_view(['GET'])
def product_api_view(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True).data
    return Response(data=serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product).data
    return Response(data=serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_api_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True).data
    return Response(data=serializer, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review).data
    return Response(data=serializer, status=status.HTTP_200_OK)


def product_review_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductReviewSerializer(product, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
