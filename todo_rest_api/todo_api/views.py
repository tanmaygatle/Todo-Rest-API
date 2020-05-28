from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Note,Todo
from .serializers import NoteSerializer,TodoSerializer

# Create your views here.

class NoteAPIView(APIView):

    def get(self,request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data)

    def post(self,request):
        if not request.data.get('todos'):
            request.data['todos'] = []
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class NoteDetailAPIView(APIView):

    def get_note(self, id):
        try:
            return Note.objects.get(id=id)
        except:
            return None

    def get(self, request, id):
        note = self.get_note(id)
        if not note:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, id):
        note = self.get_note(id)
        if not note:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        note = self.get_note(id)
        if not note:
            return Response(status=status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TodoAPIView(APIView):
    def get_note(self, id):
        try:
            return Note.objects.get(id=id)
        except:
            return None

    def get(self, request, id):
        note = self.get_note(id)
        if not note:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note)
        return Response(serializer.data['todos'])

    def post(self, request, id):
        note = self.get_note(id)
        if not note:
            return Response(status=status.HTTP_404_NOT_FOUND)
        request.data['note'] = getattr(note,"id")
        print(request.data)
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailAPIView(APIView):

    def get_note(self, note_id):
        try:
            return Note.objects.get(id=note_id)
        except:
            return None

    def get_todo(self, note, todo_id):
        try:
            return Todo.objects.get(id=todo_id)
        except:
            return None

    def get(self, request, note_id, todo_id):
        note = self.get_note(note_id)
        if not note:
            return Response(status=status.HTTP_404_NOT_FOUND)
        todo = self.get_todo(note,todo_id)
        if not todo:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, note_id, todo_id):
        note = self.get_note(note_id)
        if not note:
            return Response(status=status.HTTP_404_NOT_FOUND)
        todo = self.get_todo(note, todo_id)
        if not todo:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, note_id, todo_id):
        note = self.get_note(note_id)
        if not note:
            return Response(status=status.HTTP_404_NOT_FOUND)
        todo = self.get_todo(note, todo_id)
        if not todo:
            return Response(status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)