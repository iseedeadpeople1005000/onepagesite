from django.shortcuts import render, HttpResponse, redirect
from . import forms
from .models import Comment
from django.template.context_processors import csrf
import json
from django.views.generic import CreateView

# Create your views here.


class FormView(CreateView):
    model = Comment
    fields = ('Comment_Text', 'Comment_Author')


def page(request):
    content = Comment.objects.all()[::-1]
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


def addcomm(request):
    if request.GET:
        forma = forms.CommentForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit=False)
            forma.save()
    return HttpResponse(forma)


def create_post(request):
    if request.POST:
        forma = forms.CommentForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit=False)
            forma.save()
        Comment_Text = request.POST.get('Comment_Text', '')
        Comment_Author = request.POST.get('Comment_Author', '')
        response_data = {}
        a = Comment.objects.create(
            Comment_Text=Comment_Text,
            Comment_Author=Comment_Author
        )
        a.save()
        response_data['form_ok'] = 1
        response_data['result'] = "Сообщение отправлено!"
        response_data.update(csrf(request))
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn`t happening"}),
            content_type="application/json"
        )
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