from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import Q
from farms.models import Farm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# Project Views
@csrf_exempt
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_status = request.POST.get('new_status')
        task.status = new_status
        task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('project_list')
    return render(request, 'projects/project_form.html', {'form': form})

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project_list')
    return render(request, 'projects/project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

# Task Views
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'projects/task_list.html', {'tasks': tasks})

def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'projects/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'projects/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'projects/task_confirm_delete.html', {'task': task})



def task_calendar_view(request):
    return render(request, 'projects/task_calendar.html')



def task_json(request):
    tasks = Task.objects.all()
    data = []

    for task in tasks:
        data.append({
            'title': task.title,
            'start': task.due_date.isoformat(),
            'url': reverse('task_detail', args=[task.id])  # NEW
        })

    return JsonResponse(data, safe=False)

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'projects/task_detail.html', {'task': task})


def task_filter_view(request):
    status = request.GET.get('status')
    user = request.GET.get('user')
    farm = request.GET.get('farm')

    tasks = Task.objects.all()

    if status:
        tasks = tasks.filter(status=status)
    if user:
        tasks = tasks.filter(assigned_to__username=user)
    if farm:
        tasks = tasks.filter(project_farm_name=farm)

    return render(request, 'projects/task_filter.html', {
        'tasks': tasks,
        'status_filter': status,
        'user_filter': user,
        'farm_filter': farm,
    })



