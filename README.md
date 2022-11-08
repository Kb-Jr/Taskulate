# Taskulate

This is a task web app which serves as a to-do platform. The job of the web app is to help users keep track of activities that needs to be handled and the status of said activities. This app was built using the Django framework.


### Usage
In order to have access to this web application, users must be logged in (authenticated) which means first time visitors must first create an account and subsequently use their credentials to log in to the web app. When a user is logged in they are presented with the option to commence creating tasks they would like to keep track of. A user can click 'create new tasks' with the plus sign to create tasks. The title and description fields will be filled out and submitted to create a task successfully. To edit a task click on the particular task and edit any of the title, description or complete status fields to edit the task. To delete a task, click on the trash can icon to the right of the task and proceed to confirm delete. When a task complete status option is checked, the task title is struck through and the status is updated to 'complete' and vice versa when its incomplete. To re-order tasks, click and hold on the three vertical dots and drag to the desired position.


### Distinctiveness
A task app is very essential in todays world due to the increasing number of things that need to be done in everyday lives. A system which serves as some sort of a reminder on what needs to be done can be quite helpful in order to keep track of pending tasks and completed tasks.

This web app stands out from a basic to-do app due to its personalized function, that is to say created tasks are only accessible to the user that created said tasks. Another functionality is the "search" function which essentially checks through the lists of tasks and returns results which the title contains characters that are the same as those entered in the search field(Note: Search function is case sensitive). Users also have the ability to edit and re-edit details of created tasks. The number of incomplete tasks are shown on the header and are automatically updated as tasks are added or removed. Also the time which tasks are created are also shown alongside the details of the task.


### Complexity

This web-app was built using the django framework. The views were built by using a combination of both function based and class based views. The user authentication views were created using function based views while the other create, update, delete, tasks views were created using class based views. Class based views are django views written as python classes. The as_view() method was utilized in the urls.py file so the url resolver can successfully prcess the classes. It does so by processing the classes as functions. 

The create, read, update and delete (CRUD) functionalities were implemeented by using in-built views which were created by the django team. These views include the CreateView, DetailView, ListView, UpdateView, DeleteView. Other in-built views exist but were not utilized in this particular project. Also the "LoginRequiredMixin" which is also inbuilt was added as an argument to the classes. This was done to ensure that only authenticated users can access some views and functionalities. For more information on class based views visit any of the following (https://docs.djangoproject.com/en/4.1/topics/class-based-views/), (https://www.geeksforgeeks.orgclass-based-generic-views-django-create-retrieve-update-delete/), (https://dennisivy.com/django-class-based-views).
 
Two classes "Task" and "User", were created. The Task class had fields; "user", "title", "description", "complete" and "created on". The User class takes as input 'AbstractUser' which is built-in django and automatically creates fields in the database for users credentials.

For the interface CSS, bootstrap and jaavscript were utilized. CSS and bootstrap for the layout and styling while Javasript was used to enable a repositioning function, i.e the arrangement of tasks can be re-ordered by the user by clicking and dragging one task and placing it above or below another. The icons are delivered from the free tier of [fontawesome](https://fontawesome.com). To use free fontawesome on django it had to be installed first using adding it to the requirements.txt file, pip isntalling it and adding it to the list of installed apps in the settings.py file. 


### Files
-Templates folder contains html files for each of the views of the web app. This includes the authentication pages, the task list page, the task creation page and the delete confirmation page. In this folder there is also a layout.html file which essentially contains the design inherited by the other views. The styles were also defined in this layout.html file.

- Static folder contains the Javascript file and the favicon icon.

- The apps.py file contains a list of installed apps.

- The views.py file contains all the definition of views.

- The forms.py file contains a single class (PositionForm) which inherits from "forms" and was used to define the view for reordering tasks.

- The urls.py file contains all the url patterns.

- The models.py contains the Task and User model. Which were used in the views.py file


### Demonstration video: https://youtu.be/8y6GETvZO98



### Live link: https://taskulate.herokuapp.com/

 
