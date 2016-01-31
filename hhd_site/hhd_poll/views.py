from django.shortcuts import *
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import *

# Create your views here.
def huanhda(request):
	latest_question_list = Question.objects.order_by('-pub_date')[2:5]
	hhd_name = 'ni hao , wo shi huan hong da !!! '
	context = {'latest_question_list': latest_question_list, 'hhd_name': hhd_name}
	return render(request, 'hhd_poll/index.html', context)


def test(request):
	return HttpResponse('hahahahahahhahaha')

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'hhd_poll/detail.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'hhd_poll/results.html', {'question':question,})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		render(request, 'hhd_poll/detail.html', 
			{'question': question, 'error_message':'You have not selected a choice!',})
	else:
		choice.vote +=1
		choice.save()
		return redirect(reverse('hhd_poll:results', args=(question.id,)))

