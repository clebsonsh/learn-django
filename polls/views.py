from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_at")[:5]

    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list,
    })
def detial(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
