from requests import request
from rest_framework.authtoken.models import Token

from datetime import timedelta
from django.utils import timezone
from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime
import pytz

utc=pytz.UTC


#this return left time
def expires_in(token):
    time_elapsed = (token.created + timedelta(seconds=60)) -timezone.now() 
    left_time = timedelta(seconds = 60) - time_elapsed
    print("left time-",left_time)
    return time_elapsed

# token checker if token expired or not
def is_token_expired(token):
    current_time = datetime.now()
    token_expiration_time = token.created + timedelta(seconds= 60)
    print("compared time my", token_expiration_time)
    if utc.localize(current_time) < token_expiration_time:
        return False
    else:
        return True

# if token is expired new token will be established
# If token is expired then it will be removed
# and new one with different key will be created
def token_expire_handler(token):
    is_expired = is_token_expired(token)
    print("is expired", is_expired)
    if is_expired:
        token.delete()
        #token = Token.objects.create(user = token.user)
        #print(" new token generated ")
    return is_expired, token

 
 
 
def authenticate_credentials(key):
    try:
        token = Token.objects.get(key = key)
        print("key == ",token.key)
        print("user == ",token.user)
    except Token.DoesNotExist:
        raise AuthenticationFailed("Invalid Token")
    
    if not token.user.is_active:
        raise AuthenticationFailed("User is not active")

    is_expired, token = token_expire_handler(token)
    if is_expired:
        raise AuthenticationFailed("The Token is expired")
    
    return (token.user, token)   
   
#this return left time
# def expires_in(token):
#     time_elapsed = timezone.now() - token.created
#     print(type(token.created))
#     print("time elapsed",time_elapsed)
#     left_time = time_elapsed #timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
#     print("time left",left_time)
#     return left_time

# # token checker if token expired or not
# def is_token_expired(token, created_at_s):
#     time_elapsed = timezone.now() - token.created
#     print(time_elapsed)
#     now = datetime.now()
#     time1 = token.created
#     time1.strftime()
#     current_time = now.strftime("%H:%M:%S")
#     print(current_time)
#     #print(timedelta(current_time))
#     current_time_s = int(now.strftime("%S"))
#     current_time_m = int(now.strftime("%M"))
#     current_time_h = int(now.strftime("%H"))
#     print("Current Time =", current_time )
#     print("Current Time =", current_time_s )
#     print("Current Time =", current_time_m*60 )
#     print("Current Time =", current_time_h*3600 )
#     a = current_time_s
#     b = current_time_m*60
#     c = current_time_h*3600
#     current_in_s = a+b+c
#     print("current time in seconds ", current_in_s)
#     print("created at in sec ", created_at_s)
#     if current_in_s > created_at_s + 60:
#         return True
#     else:
#         return False
    
#     #return expires_in(token) < timedelta(seconds = 0)

# # if token is expired new token will be established
# # If token is expired then it will be removed
# # and new one with different key will be created
# def token_expire_handler(token,  created_at_s):
#     is_expired = is_token_expired(token,created_at_s)
#     if is_expired:
#         token.delete()
#         token = Token.objects.create(user = token.user)
#         print(token)
#     return is_expired, token
# 
#________________________________________________
#DEFAULT_AUTHENTICATION_CLASSES
# class ExpiringTokenAuthentication(TokenAuthentication):
#     """
#     If token is expired then it will be removed
#     and new one with different key will be created
#     """
    
#     def authenticate_credentials(self, key):
#         try:
#             token = Token.objects.get(key = key)
#         except Token.DoesNotExist:
#             raise AuthenticationFailed("Invalid Token")
        
#         if not token.user.is_active:
#             raise AuthenticationFailed("User is not active")

#         is_expired, token = token_expire_handler(token)
#         # is_expired = is_token_expired(token) 
#         if is_expired:
#             raise AuthenticationFailed("The Token is expired")
        
#         return (token.user, token)