from django.shortcuts import render, get_object_or_404, redirect
from .models import Animation
from .forms import AnimationForm

def animation_list(request):
    animations = Animation.objects.all()
    return render(request, 'animations/animation_list.html', {'animations': animations})

def animation_detail(request, pk):
    animation = get_object_or_404(Animation, pk=pk)
    return render(request, 'animations/animation_detail.html', {'animation': animation})

def animation_create(request):
    if request.method == "POST":
        form = AnimationForm(request.POST, request.FILES)
        if form.is_valid():
            animation = form.save()
            return redirect('animation_detail', pk=animation.pk)
    else:
        form = AnimationForm()
    return render(request, 'animations/animation_form.html', {'form': form})

def animation_update(request, pk):
    animation = get_object_or_404(Animation, pk=pk)
    if request.method == "POST":
        form = AnimationForm(request.POST, request.FILES, instance=animation)
        if form.is_valid():
            animation = form.save()
            return redirect('animation_detail', pk=animation.pk)
    else:
        form = AnimationForm(instance=animation)
    return render(request, 'animations/animation_form.html', {'form': form})

def animation_delete(request, pk):
    animation = get_object_or_404(Animation, pk=pk)
    if request.method == "POST":
        animation.delete()
        return redirect('animation_list')
    return render(request, 'animations/animation_confirm_delete.html', {'animation': animation})

