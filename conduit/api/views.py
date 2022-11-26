from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from base.models import Item
# from .serializers import ItemSerializer

from base.models import User
from .serializers import UserSerializer

# @api_view(['GET'])
# def getData(request):
#     persons = Item.objects.all()
#     serializer = ItemSerializer(persons, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def addPerson(request):
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

@api_view(['GET'])
def getAll(request):
    users = User.objects.all().order_by('id')
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# @api_view(['POST'])
# def updatePerson(request, pk):
#     person = Person.objects.get(id=pk)
#     serializer = PersonSerializer(instance=person, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['PUT'])
# def updatePerson(request, pk):
#     person = Person.objects.get(id=pk)
#     serializer = PersonSerializer(instance=person, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['PATCH'])
# def updatePerson(request, pk):
#     person = Person.objects.get(id=pk)
#     serializer = PersonSerializer(instance=person, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
def updateUser(request, pk):
    try: 
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = UserSerializer(instance=user, data=request.data)
    elif request.method == 'PATCH':
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    person = User.objects.get(id=pk)
    person.delete()
    return Response('User successfully deleted!')

