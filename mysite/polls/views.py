from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views here.

def index(request) -> HttpResponse:
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_questions_list }
    return render(request, 'polls/index.html', context)

def detail(request, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {"question": question})

def results(request, question_id: int) -> HttpResponse:
    return HttpResponse(f'you are looking at results of question {question_id}')

def vote(request, question_id: int) -> HttpResponse:
    return HttpResponse(f'you are looking at the votes of question {question_id}')
