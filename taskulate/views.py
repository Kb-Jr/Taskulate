from django.db import transaction
from sqlite3 import IntegrityError
from venv import create
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from .models import Task, User
from .forms import PositionForm
from django.views import View
from django.shortcuts import redirect


# Create your views here

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("tasks"))
        
        else:
            return render(request, "taskulate/login.html", {
                "message": "Invalid username and/or password."
            }) 
    
    else:
        return render(request, "taskulate/login.html")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))




def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']

        # Ensure password matches confirmation
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, "taskulate/register.html", {
                "message": "passwords must match"
            })

         # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "taskulate/register.html", {
                "message": "credentials already exist"
            })
        login(request,user)
        return HttpResponseRedirect(reverse("tasks"))
    else:
        return render(request, "taskulate/register.html")



#Login required
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'   
    
    queryset : Task.objects.all()


    def get_context_data(self, **kwargs):
        #filter tasks to be user specific
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        #get results based on input value in the search bar, if whats input in the search bar exists in the tasks, display the task(s)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context



#Login required
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'taskulate/task.html'


#Login required
class TaskCreate(LoginRequiredMixin, CreateView):
    #task form to create task, if form is valid return tasklist
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)



#Login required
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


#Login required
class DeleteView(LoginRequiredMixin, DeleteView):
    #delete a task from tasks belonging to particular user, redirect to tasklist page if successful
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)



class TaskReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(positionList)

        return redirect(reverse_lazy('tasks'))
