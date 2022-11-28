from http.client import HTTPResponse
from smtplib import SMTPResponseException
from django.shortcuts import render
from django_user_agents.utils import get_user_agent


# Create your views here.

def home(request):

    return render(request, 'core/home.html')


def my_view(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return SMTPResponseException('User using mobile')
    elif user_agent.is_pc:
        vi=request.META['HTTP_USER_AGENT']
        print(vi)
        return HTTPResponse('User using Computer')


