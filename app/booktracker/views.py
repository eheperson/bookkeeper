# from django.shortcuts import render
from rest_framework import status    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from booktracker.serializers import BookSerializer
from booktracker.models import Book


@api_view(['GET'])
def bookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books,many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK   
    )


@api_view(['GET'])
def bookDetailed(request,pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book,many=False)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK   
    )


@api_view(['POST'])
def bookRecord(request):
    # books = Book.objects.all()
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )


@api_view(['PUT'])
def bookUpdate(request, pk):
    try:
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(
            instance=book, 
            data=request.data, 
            partial=False
        )
        if serializer.is_valid():
            serializer.save()
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK
        )
    except Book.DoesNotExist:
        return Response(
            data='object do you want to ubdate does not exists. check the id you requested', 
            status=status.HTTP_404_NOT_FOUND
        )
        

@api_view(['DELETE'])
def bookDelete(request, pk):
    try:
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(
            data='DELETED', 
            status=status.HTTP_200_OK
        )

    except Book.DoesNotExist:
        return Response(
            data='object do you want to delete does not exists. check the id you requested', 
            status=status.HTTP_404_NOT_FOUND
        )
