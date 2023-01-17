from django.http import JsonResponse
import json
import os 
def index(request):

    data = {
        'msg' : 'Welcome to the COVID API'
    }
    return JsonResponse( data )

def api_map( request, zip_code ):
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open( dir_path + '/test_data.json' )
    data = json.load( f )

    f.close()
    
    return JsonResponse( data )

def api_ppe( request ):
    pass
