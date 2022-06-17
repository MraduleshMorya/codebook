#
# session authorization function and is user logged in function 
#
from django.http import HttpResponse
from django.shortcuts import redirect
from httplib2 import Http
from requests import request
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from datetime import datetime
import pytz

utc = pytz.UTC

def is_user_loggedin(request):
    
    print("\n \n running is user logge din function ")
    if "username" not in request.session:
        print("inside if block ")
        try:
            return redirect("index")
        except:
            return HttpResponse("not working ")
    else :
        print("\n \n request  == ",request.session["username"])
        return True
    # if "username" not in request.session:
    #     return redirect("index")
    #     # request.session.get_expire_at_browser_close()
    #     # print("\n \n print expiry time ", request.session.get_expiry_age())
    #     # return True
        
    #     # created_at = request.session["created_at"]
    #     # current_datetime = datetime.now()
    #     # expires_at = created_at + timedelta(seconds=900)
        
    #     # print("\n \n session expires at --", expires_at)
    #     # if utc.localize(current_datetime) < expires_at:
    #     #     return True
    #     # else:
    #     #     del request.session
    # else:
    #     return True
    
    
