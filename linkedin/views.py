from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from urllib.parse import quote
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def linkedinauth(request):
    redirect_url = quote("")#add your redirect url
    return HttpResponseRedirect("https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={}&redirect_uri="+redirect_url+"&scope=r_basicprofile,r_emailaddress&state=88972239179")

def loginsuccess(request):
    redirect_url = quote("")#add your redirect url
    #authcode = request.GET.get('code')
    access_token = requests.get("https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&code="+str(request.GET.get('code'))+"&client_id={}&client_secret={}&redirect_uri="+redirect_url)
    print(access_token)
    print(access_token.text)
    return render(request,"linkedin/login.html")
#def profile(request):
