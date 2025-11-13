from django.shortcuts import render, redirect

VALID_EMAIL = 'clement1raka@gmail.com'
VALID_PASSWD = '123'

def index(request):
    
    submitted_email = request.GET.get('email')
    submitted_passwd = request.GET.get('passwd')
    
    if submitted_email == VALID_EMAIL and submitted_passwd == VALID_PASSWD:
        return redirect('result')
    else:
        context = {'error_msg' : 'Invalid Email or Password'}
        return render(request, 'index.html', context)
        


def result_page(request):
    
    return render(request, 'result.html')
# Create your views here.
