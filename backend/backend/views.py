from rest_framework.response import Response
from rest_framework import status, generics
import math
from datetime import datetime 

from .models import Users, Message, Food, Rating, Comment
from .serializer import UserSerializer, MessageSerializer, FoodSerializer, RatingSerializer, CommentSerializer


#View for the food list CRUD API
class FoodList(generics.GenericAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

    #Endpoint to return the list of foods in json form
    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1)*limit_num
        end_num = limit_num*page_num
        search_param = request.GET.get("search")
        notes = Food.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(title__icontains = search_param)
        serializer = self.serializer_class(notes[start_num:end_num], many = True)
        return Response(
            {
                'status' : 'success',
                'total' : total_notes,
                'notes' : serializer.data
            }
        )
    
    #End point for post request so ass to add a new post to the data base
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : "Success",
                "note" : serializer.data
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                'status' : 'failed',
                'message' : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)

class FoodDetails(generics.GenericAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

    def get_note(self, pk):
        try:
            return Food.objects.get(pk = pk)
        except:
            return None

    #Endpoint to get a food by its primary key attribute
    def get(self, request, pk):
        note = self.get_note(pk = pk)
        if note == None:
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(note)
        return Response({
            'status' : 'success',
            'note' : serializer.data
        })

    #Endpoint to update a particuler table attribute
    def patch(self, request, pk):
        note = self.get_note(pk = pk)
        if note == None :
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(note, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({
                'status' : 'Success',
                'note' : serializer.data
            })
        return Response({
                'status' : 'failed',
                'message' : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)

    #Endpoint to delete a post from the db
    def delete(self, request, pk):
        note = self.get_note(pk)
        if note == None :
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        note.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




#Creating endpoints to handle users

class UserList(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

    #Endpoint to return the list of foods in json form
    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1)*limit_num
        end_num = limit_num*page_num
        search_param = request.GET.get("search")
        notes = Users.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(title__icontains = search_param)
        serializer = self.serializer_class(notes[start_num:end_num], many = True)
        return Response(
            {
                'status' : 'success',
                'total' : total_notes,
                'notes' : serializer.data
            }
        )
    
    #End point for post request so ass to add a new post to the data base
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : "Success",
                "note" : serializer.data
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                'status' : 'failed',
                'message' : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)

class UserDetails(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

    def get_note(self, pk):
        try:
            return Users.objects.get(pk = pk)
        except:
            return None

    #Endpoint to get a user by its primary key attribute
    def get(self, request, pk):
        note = self.get_note(pk = pk)
        if note == None:
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(note)
        return Response({
            'status' : 'success',
            'note' : serializer.data
        })

    #Endpoint to update a particuler user  attribute
    def patch(self, request, pk):
        note = self.get_note(pk = pk)
        if note == None :
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(note, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({
                'status' : 'Success',
                'note' : serializer.data
            })
        return Response({
                'status' : 'failed',
                'message' : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)

    #Endpoint to delete a user from the db
    def delete(self, request, pk):
        note = self.get_note(pk)
        if note == None :
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        note.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        




class MessageList(generics.GenericAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    #Endpoint to return the list of foods in json form
    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1)*limit_num
        end_num = limit_num*page_num
        search_param = request.GET.get("search")
        notes = Message.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(title__icontains = search_param)
        serializer = self.serializer_class(notes[start_num:end_num], many = True)
        return Response(
            {
                'status' : 'success',
                'total' : total_notes,
                'notes' : serializer.data
            }
        )
    
    #End point for post request so ass to add a new post to the data base
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : "Success",
                "note" : serializer.data
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                'status' : 'failed',
                'message' : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)

class MessageDetails(generics.GenericAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get_note(self, pk):
        try:
            return Message.objects.get(pk = pk)
        except:
            return None

    #Endpoint to get a user by its primary key attribute
    def get(self, request, pk):
        note = self.get_note(pk = pk)
        if note == None:
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(note)
        return Response({
            'status' : 'success',
            'note' : serializer.data
        })
    #Endpoint to delete a user from the db
    def delete(self, request, pk):
        note = self.get_note(pk)
        if note == None :
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        note.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        



class RatingList(generics.GenericAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    #Endpoint to return the list of foods in json form
    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1)*limit_num
        end_num = limit_num*page_num
        search_param = request.GET.get("search")
        notes = Rating.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(title__icontains = search_param)
        serializer = self.serializer_class(notes[start_num:end_num], many = True)
        return Response(
            {
                'status' : 'success',
                'total' : total_notes,
                'notes' : serializer.data
            }
        )
    
    #End point for post request so ass to add a new post to the data base
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : "Success",
                "note" : serializer.data
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                'status' : 'failed',
                'message' : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)


class RatingDetails(generics.GenericAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def get_note(self, pk):
        try:
            return Rating.objects.get(pk = pk)
        except:
            return None

    #Endpoint to get a user by its primary key attribute
    def get(self, request, pk):
        note = self.get_note(pk = pk)
        if note == None:
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(note)
        return Response({
            'status' : 'success',
            'note' : serializer.data
        })
    #Endpoint to delete a user from the db
    def delete(self, request, pk):
        note = self.get_note(pk)
        if note == None :
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        note.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class CommentList(generics.GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    #Endpoint to return the list of foods in json form
    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1)*limit_num
        end_num = limit_num*page_num
        search_param = request.GET.get("search")
        notes = Comment.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(title__icontains = search_param)
        serializer = self.serializer_class(notes[start_num:end_num], many = True)
        return Response(
            {
                'status' : 'success',
                'total' : total_notes,
                'notes' : serializer.data
            }
        )
    
    #End point for post request so ass to add a new post to the data base
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : "Success",
                "note" : serializer.data
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                'status' : 'failed',
                'message' : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)

class CommentDetails(generics.GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_note(self, pk):
        try:
            return Comment.objects.get(pk = pk)
        except:
            return None

    #Endpoint to get a user by its primary key attribute
    def get(self, request, pk):
        note = self.get_note(pk = pk)
        if note == None:
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(note)
        return Response({
            'status' : 'success',
            'note' : serializer.data
        })
    #Endpoint to delete a user from the db
    def delete(self, request, pk):
        note = self.get_note(pk)
        if note == None :
            return Response(
                {
                    'status' : 'failed',
                    'message' : f"Note with Id: {pk} not found"
                }, status = status.HTTP_404_NOT_FOUND
            )
        note.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        

        



    