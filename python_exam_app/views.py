from tkinter.tix import Tree
from django.shortcuts import render, redirect
from login_app.models import *
from python_exam_app.models import *
from django.contrib import messages

def dashboard(request):
    if 'user_id' in request.session:
        context = {
            'user':User.objects.get(id=request.session['user_id']),
            'all_trees':Tree.objects.all(),
        }
        return render(request,'dashboard.html', context)
    else:
        return redirect('/')

def plant_a_tree(request):
    if 'user_id' in request.session:
        context = {
            'user':User.objects.get(id=request.session['user_id']),
        }
        return render(request,'newtree.html', context)
    else:
        return redirect('/')

def add_plant(request):
    errors = Tree.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard/new/tree/')
    else:
        species = request.POST['species']
        location = request.POST['location']
        reason = request.POST['reason']
        date = request.POST['date']
        logged_user = User.objects.get(id=request.session['user_id'])
        Tree.objects.create(species = species, location = location, reason = reason, date = date, planted_by = logged_user)
    
    return redirect('/dashboard/new/tree/')


def show_my_tree(request):
    # this_user = User.objects.get(id=int(request.session['user_id'])),
    context = {
            'user':User.objects.get(id=int(request.session['user_id'])),
        }

    return render(request, 'mytree.html', context)

def edit_my_tree(request, id):
    context = {
            'user':User.objects.get(id=request.session['user_id']),
            'this_trees':Tree.objects.get(id=id),
            'tree_date':Tree.objects.get(id=id).date.strftime("%Y-%m-%d")
        }

    return render(request, 'edittree.html', context)

def update_tree(request, id):

    errors = Tree.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard/edit/'+str(id)+'/')
    else:
        edit_my_tree = Tree.objects.get(id=id)
        edit_my_tree.species = request.POST['species']
        edit_my_tree.location = request.POST['location']
        edit_my_tree.reason = request.POST['reason']
        edit_my_tree.date = request.POST['date']

        edit_my_tree.save()

    return redirect('/dashboard/user/account/')

def delete_tree(request, id):
    delete_tree = Tree.objects.get(id=id)
    delete_tree.delete()

    return redirect('/dashboard/user/account/')

def details(request, id):
    context = {
            'user':User.objects.get(id=request.session['user_id']),
            'all_trees':Tree.objects.get(id=id)
        }
    
    return render(request, 'details.html', context)

def visited_by(request, id):
    user_visit = User.objects.get(id=request.session['user_id'])
    visited_tree = Tree.objects.get(id=id)

    user_visit.viewed_trees.add(visited_tree)

    return redirect('/dashboard/show/'+str(id)+'/')