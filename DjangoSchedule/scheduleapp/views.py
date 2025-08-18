from django.shortcuts import render, redirect, get_object_or_404
from .models import Schedule
from .forms import ScheduleForm

# Create your views here.


def list_schedules(request):
    if request.user.is_authenticated:
        # Filtra as anotações para mostrar apenas as do usuário logado
        schedules = Schedule.objects.filter(author=request.user).order_by('-created_at')
        return render(request, 'scheduleapp/list_schedules.html', {'schedules': schedules})
    else:
        # Se o usuário não estiver logado, não há anotações para mostrar
        return render(request, 'scheduleapp/list_schedules.html', {'schedules': []})


def create_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('scheduleapp:list')
    else:
        form = ScheduleForm()
    return render(request, 'scheduleapp/create_schedule.html', {'form': form})


def edit_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('scheduleapp:list')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'scheduleapp/edit_schedule.html', {'form': form})


def delete_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('scheduleapp:list')
    return redirect('scheduleapp:list')
