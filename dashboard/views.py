from django.shortcuts import render
from farms.models import Farm, Field, Crop
from projects.models import Project, Task

def dashboard_view(request):
    total_farms = Farm.objects.count()
    total_fields = Field.objects.count()
    total_crops = Crop.objects.count()
    total_projects = Project.objects.count()

    task_counts = {
        'pending': Task.objects.filter(status='pending').count(),
        'in_progress': Task.objects.filter(status='in_progress').count(),
        'completed': Task.objects.filter(status='completed').count(),
    }

    context = {
        'total_farms': total_farms,
        'total_fields': total_fields,
        'total_crops': total_crops,
        'total_projects': total_projects,
        'task_counts': task_counts,
    }

    return render(request, 'dashboard/dashboard.html', context)