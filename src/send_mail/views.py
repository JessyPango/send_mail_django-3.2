
from django.core import mail

from django.http import HttpResponse
from django.shortcuts import render

import core.settings 
# Create your views here.

def send_mail(request):


	if request.method == "POST":

		subject = request.POST.get('subject',None)
		message = request.POST.get('message',None)
		from_email =  request.POST.get('from_email',None)
		recipient_list = request.POST.get('recipient_list',None)
		auth_user = request.POST.get('auth_user',core.settings.EMAIL_HOST_USER)
		auth_password = request.POST.get('auth_password',core.settings.EMAIL_HOST_PASSWORD)
		
		html_message = request.POST.get('html_message',None)

		if subject and (message or html_message) and (from_email or  auth_user ) and recipient_list and auth_password :
			recipient_list = recipient_list.split(',')

			result = mail.send_mail(subject, message, 'auth_user', recipient_list,fail_silently=False, html_message=html_message)
			if result:
				return HttpResponse("Mail has send.")
			else:
				return HttpResponse("Mail has not send.")

		else:

			return HttpResponse("Mail has not send.")


	return render(request,'send_mail/index.html')