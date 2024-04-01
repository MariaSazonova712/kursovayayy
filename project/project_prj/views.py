from django.shortcuts import render, redirect
from .models import Task, Orders
from .forms import TaskForm
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import OrderForm
from django.contrib import messages


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'project_prj/index.html', {
        'title': 'Главная страница сайта', 'tasks': tasks})


def rasp(request):
    return render(request, 'project_prj/rasp.html')


# def news(request):
#     tasks = Task.objects.order_by('id')
#     return render(request, 'project_prj/task_list.html', {'title': 'Список услуг', 'tasks': tasks})
class TaskListView(ListView):
    model = Task
    template_name = 'blog/task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список услуг'
        return context



def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверно'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'project_prj/create.html', context)


class Del(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'project_prj/task-delete.html'


class Upd(UpdateView):
    model = Task
    template_name = 'project_prj/create.html'
    form_class = TaskForm
    success_url = '/'


def booking(request):
    return render(request, 'project_prj/booking.html')


def kontakt(request):
    return render(request, 'project_prj/kontakt.html')


class OrderCreateView(LoginRequiredMixin, CreateView):
    # model = Orders
    # fields = ["created", "car", "description", "owner", "stat"]
    form_class = OrderForm
    template_name = 'project_prj/task-form.html'
    success_url = '/'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'В поле {field} возникла ошибка: {error}')
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        print(self.request)
        print(self.kwargs['pk'])
        form.instance.task = Task.objects.get(id=self.kwargs['pk'])  # Выбираем авто по pk
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['header_text'] = "My Form"
        pk = self.kwargs.get('pk')
        selected_car = Task.objects.get(id=pk)
        context['task_info'] = f'Услуга: {selected_car.name}'
        return context


class UserOrdersListView(ListView):
    model = Orders
    context_object_name = 'orders'
    extra_context = {'title': 'История записей'}

    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Orders.objects.filter(owner=self.request.user).order_by('-created')
