# TODO Rest API Django

The required dependencies are<br>
`python3`<br>
`django`<br>
`djangorestframework`<br>

These can be installed using `pip`.<br>
The server can be started by doing a `cd` into the directory and running the following command<br>
`python3 manage.py runserver`<br>.
The server is up on `localhost:8000`.<br><br>
There are two tables `notes` and `todos` where one note can have many todos.<br><br>
`notes` have the following structure:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;"title":"..",<br>
&nbsp;&nbsp;&nbsp;&nbsp;"content":"..",<br>
&nbsp;&nbsp;&nbsp;&nbsp;"todos":[..]<br>
}
<br><br>
`todos` have the following structure:<br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;"title":"..",<br>
&nbsp;&nbsp;&nbsp;&nbsp;"content":"..",<br>
&nbsp;&nbsp;&nbsp;&nbsp;"due_date":"YYYY-MM-DD",<br>
&nbsp;&nbsp;&nbsp;&nbsp;"completed":"true/false"<br>
}
<br><br>
The rest server has four endpoints:<br>
1. /notes/<br>
`GET` to get all notes. `POST` to create a new note. `todos` can be left blank.<br>
2. /notes/{note_id}/<br>
`GET` to get the specific note. `PUT` to update the note (partial updates can be done). `DELETE` to delete the note and all todos inside.<br>
3. /notes/{note_id}/todos/<br>
`GET` to get all todos within the note. `POST` to create a new todo for that note.<br>
4. /notes/{note_id}/todos/{todo_id}<br>
`GET` to get the specific todo. `PUT` to update the todo (partial updates can be done). `DELETE` to delete the todo.<br>
