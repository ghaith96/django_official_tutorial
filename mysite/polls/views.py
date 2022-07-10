from typing import Optional
from urllib.request import HTTPRedirectHandler
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


from .models import Choice, Question

# Create your views here.

class IndexView(generic.ListView):
    template_name: str = 'polls/index.html'
    context_object_name: Optional[str] = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailsView(generic.DetailView):
    model = Question
    template_name: str = 'polls/details.html'

class ResultView(generic.DetailView):
    model = Question
    template_name: str = 'polls/results.html'

def vote(request, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result'), args=(question_id))
