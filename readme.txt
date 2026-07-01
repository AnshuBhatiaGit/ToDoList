todo_main   ---> settings.py
            *** Register the application in Installed app section

todo_main   ---> urls.py
            *** Define the url patters for admin and todo app

todo_main   ---> admin.py
            *** To change the columns in admin site

todo_main   ---> views.py
            *** Method def home(request): get data from Model(models.py) for home page and display on home.html

todo        ---> models.py
            *** Create the database model (table, fields)

templates   ---> home.html
            *** Displays the Front End UI

todo        ---> urls.py
            *** Define all the url patterns for todo app (Add, Edit, Update, Delete)

todo        ---> views.py
            Method def mark_as_done(request, pk):
            Method def mark_as_undone(request, pk):
            Method def edit_task(request, pk):
            Method def delete_task(request, pk):
            *** Get data from Model(models.py) for Home page & Edit page and display on home.html, edit.html
            Related methods for CRUD Operations (Add, Edit, Update, Delete) 

templates   ---> edit.html
            *** Displays the Front End UI