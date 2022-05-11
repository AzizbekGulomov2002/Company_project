from django.shortcuts import render, redirect

from .models import Exercises, Work_table, Worker

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def main(request):
    if request.user.is_superuser:
        user = request.user.id
        base = Work_table.objects.filter(name_id = user)
        return redirect('admin/')
    else:
        user = request.user.id
        base = Work_table.objects.filter(name_id = user)
        return render(request, 'base.html', {'base': base})


def worker(request):    
    worker=Worker.objects.all()
    return render(request, 'blog/workers.html',{'worker':worker})


def ish_olish(request):
    user = request.user.id
    base = Work_table.objects.filter(name_id = user)
    base.update(status = 'accept')
    print(base)
    return redirect('/')

def ish_stop(request):
    user = request.user.id
    base = Work_table.objects.filter(name_id = user)
    base.update(status = 'cancel')
    print(base)
    return redirect('/')
