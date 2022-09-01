from codebook_home.models import invoke_detail
from asgiref.sync import sync_to_async
import json


class save_api_detail_middleare:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        try:
            # print("\n entered custome middleware to store data  ")
            # print("request.method == ", request.method)
            # print("request.headers == ", request.headers)
            # print("request.path == ", request.path_info)
            # print("request.session[username] ",request.session["username"])

            # commenting this one to test app without storing logs
            obj = invoke_detail(
                username=request.session["username"], invoked_api=request.path_info, invokation_method=request.method, request_headers=json.dump(request.headers), )
            obj.save(using='mongo')
            print("data saved successfully")
        except:
            #print("\n caught exception in custom middleware ")
            pass
        # print("returning response ")
        return response


class check_to_many_attempts:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        try:
            # print("\n entered custome middleware to store data  ")
            # print("request.method == ", request.method)
            # print("request.headers == ", request.headers)
            # print("request.path == ", request.path_info)
            # print("request.session[username] ",request.session["username"])

            # commenting this one to test app without storing logs
            obj = invoke_detail(
                username=request.session["username"], invoked_api=request.path_info, invokation_method=request.method, request_headers=json.dump(request.headers), )
            obj.save(using='mongo')
            print("data saved successfully")
        except:
            #print("\n caught exception in custom middleware ")
            pass
        # print("returning response ")
        return response
