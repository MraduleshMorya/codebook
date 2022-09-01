import datetime
from codebook_home.models import invoke_detail
from asgiref.sync import sync_to_async,async_to_sync
import json
import asyncio
from django.utils.decorators import async_only_middleware,sync_and_async_middleware
import tracemalloc
import time
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

#@async_only_middleware
# #@sync_and_async_middleware
# @sync_to_async
# class save_api_detail_middleare:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.

#     #@sync_to_async
    
#     async def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#         response = await self.get_response(request)
#         await asyncio.wait(response)

#         # Code to be executed for each request/response after
#         # the view is called.
#         try:
#             print("\n entered custome middleware to store data  ")
#             print("request.method == ", request.method)
#             #print("request.headers == ", request.headers)
#             print("request.path == ", request.path_info)
#             print("request.session[username] ", request.session["username"])
#             obj = invoke_detail(
#                 username=request.session["username"], invoked_api=request.path_info, invokation_method=request.method, request_headers=dict(request.headers))
#             print("obj == ",obj)
#             obj.save(using='mongo')
#             print("data saved successfully")
#             # except:
#             #     print("\n caught exception in custom middleware ")
#             #     pass
#             print("returning response ")
#             print("response == ", response)
#         except:
#             pass
#         return await response

def save_api_detail_middleare(get_response):
    # One-time configuration and initialization.


    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.


        # commenting this one to test app without storing logs
        # start = time.time()
        # print("code is exucting before the api is invoked ")
        response = get_response(request)
        try:
            pass
             # print("\n entered custome middleware to store data  ")
            # print("request.method == ", request.method)
            # #print("request.headers == ", request.headers)
            # print("request.path == ", request.path_info)
            # print("request.session[username] ", request.session["username"])

            # commenting this one to test app without storing logs
            # obj = invoke_detail(
            #     username=request.session["username"], invoked_api=request.path_info, invokation_method=request.method, request_headers=dict(request.headers))
            # # print("obj == ",obj)
            # obj.save(using='mongo')
            # print("data saved successfully")


            # except:
            #     print("\n caught exception in custom middleware ")
            #     pass
            # print("returning response ")
            # print("response == ", response)

            # Code to be executed for each request/response after
            # the view is called.
            # print("execution completed of middleware ")
            # end = time.time()
            # print("took this much time --", end - start)
            # return response
        except:
            pass

        # Code to be executed for each request/response after
        # the view is called.
        # print("execution completed of middleware ")
        # end = time.time()
        # print("took this much time --", end - start)
        return response

    return middleware


class check_to_many_attempts:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        api_list = ["/user_profile/", "/test/"]
        # Code to be executed for each request/response after
        # the view is called.
        try:
            # print("\n entered custome middleware to store data  ")
            # print("request.method == ", request.method)
            # print("request.headers == ", request.headers)
            print("request.path == ", request.path_info)
            if request.path_info in api_list:
                print("path matched ")
                ip = request.META["REMOTE_ADDR"]
                temp = {f"{request.path_info}":1}
                cache_result = cache.get(f"{ip}")

                if cache_result == None:
                    print("cache null :-")
                    cache.add(f"{ip}",temp)
                else:
                    print("cache found for ip :- ",ip)
                    if f"{request.path_info}" in cache_result.keys():
                        print("key found for ip :-")
                        if cache_result[f"{request.path_info}"] < 10:
                            print("hits:----",cache_result[f"{request.path_info}"])
                            cache_result[f"{request.path_info}"] = cache_result[f"{request.path_info}"] + 1
                            cache.set(f"{ip}",cache_result)
                        else :
                            print("hits:----", cache_result[f"{request.path_info}"])
                            return JsonResponse({"status":429})
                    else :
                        cache_result[f"{request.path_info}"] = 1
                        cache.set(f"{ip}", cache_result)




            # print("request.session[username] ",request.session["username"])

            # commenting this one to test app without storing logs
        except Exception as e:
            print("\n caught exception in custom middleware :-",e)
            pass
        # print("returning response ")
        return response
