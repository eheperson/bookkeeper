# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from booktracker.models import(
    Book
)
from booktracker.serializers import(
    BookSerializer,
)
# Create your views here.


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def bookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bookDetailed(request,pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def bookRecord(request):
    # books = Book.objects.all()
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def bookUpdate(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data, partial=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def bookDelete(request, pk):
    book = Book.objects.all(id=pk)
    book.delete()
    return Response('Deleted')
