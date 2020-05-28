from django.db import models

# Create your models here.
class Note(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()

	def __str__(self):
		return self.title

class Todo(models.Model):
	note = models.ForeignKey(Note, related_name='todos', on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	content = models.TextField()
	due_date = models.DateField()
	completed = models.BooleanField(default=False)

	class Meta:
		ordering = ['due_date']

	def __str__(self):
		return self.title
