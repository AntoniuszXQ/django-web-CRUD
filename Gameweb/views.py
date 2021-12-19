from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Game
from .forms import GameForm
from django.contrib.auth.decorators import login_required


def read(request):
    all=Game.objects.all()
    return render(request,'game_read.html',{"Games":all})

@login_required()
def add(request):
    add_form = GameForm(request.POST or None, request.FILES or None)

    if add_form.is_valid():
        add_form.save()

    return render(request,'game_form.html',{'form':add_form,'new':True})

@login_required()
def update(request,id):
    game=get_object_or_404(Game,pk=id)
    edit_form=GameForm(request.POST or None, request.FILES or None, instance=game)

    if edit_form.is_valid() :
        edit_form.save()
        return redirect(read)

    return render(request,'game_form.html', {'form':edit_form,'new':False})

@login_required()
def delete(request,id):
    game=get_object_or_404(Game,pk=id)

    if request.method=='POST':
        game.delete()
        return redirect(read)

    return  render(request,'delete.html',{'game':game})