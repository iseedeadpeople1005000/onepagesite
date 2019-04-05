from django.shortcuts import render, HttpResponse, redirect
from . import forms
from .models import Comment
from django.template.context_processors import csrf

# Create your views here.

def page(request):
    content = Comment.objects.last()
    comment_form = forms.CommentForm
    return render(request, "onepage.html", {"content": content,
                                                "form": comment_form})

def addcom(request):
    if request.POST:
        forma = forms.CommentForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit=False)
            forma.save()
            return redirect("/")


  #  content = []
  #  if request.GET:
  #      return render(request, "onepage.html", {"content": content})
#
  #  if request.POST:
  #      forma = forms.CommentForm(request.POST)
  #      if forma.is_valid():
  #          content[0]=forma.__dict__.items()
  #          forma.save()
  #     #     return render(request, "onepage.html", {"content": content})