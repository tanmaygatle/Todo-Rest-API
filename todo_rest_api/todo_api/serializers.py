from rest_framework import serializers
from .models import Note,Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['id']

class NoteSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)

    class Meta:
        model = Note
        fields = ['id','title','content','todos']
        read_only_fields = ['id']

    def create(self, validated_data):
        todos_data = validated_data.pop('todos')
        note = Note.objects.create(**validated_data)
        for todo_data in todos_data:
            Todo.objects.create(note=note, **todo_data)
        return note