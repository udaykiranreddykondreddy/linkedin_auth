from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from urllib.parse import quote
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def linkedinauth(request):
    redirect_url = quote("http://127.0.0.1:8000/loginsuccess")
    return HttpResponseRedirect("https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=81dfb27otk5fni&redirect_uri="+redirect_url+"&scope=r_basicprofile,r_emailaddress&state=8897239179")

def loginsuccess(request):
    redirect_url = quote("https://referworthy.com/")
    authcode = request.GET.get('code')
    print(authcode)
    url = "https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&code="+authcode+"&client_id=81cbqkeac6bijl&client_secret=gadxzv9Vlivj8fnr&redirect_uri=https://referworthy.com/"
    print(url)
    access_token = requests.post("https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&code="+authcode+"&client_id=81cbqkeac6bijl&client_secret=gadxzv9Vlivj8fnr&redirect_uri=https://referworthy.com/")
    print(access_token.text)
    access_token = access_token.json()["access_token"]
    member_details = requests.get("https://api.linkedin.com/v1/people/~:(id,first-name,industry,picture-url,email-address)?oauth2_access_token"+access_token+"&format=json")
    print(member_details.text)
    return HttpResponseRedirect(redirect_url)
