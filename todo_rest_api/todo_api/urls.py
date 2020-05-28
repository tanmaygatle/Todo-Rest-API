from django.urls import path
from .views import NoteAPIView,NoteDetailAPIView,TodoAPIView,TodoDetailAPIView

urlpatterns = [
    path('notes/', NoteAPIView.as_view(), name='note_view'),
    path('notes/<int:id>/', NoteDetailAPIView.as_view(), name='note_detail_view'),
    path('notes/<int:id>/todos/', TodoAPIView.as_view(), name='todo_view'),
    path('notes/<int:note_id>/todos/<int:todo_id>/', TodoDetailAPIView.as_view(), name='todo_detail_view'),
]
