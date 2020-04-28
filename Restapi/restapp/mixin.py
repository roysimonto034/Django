from  django.http import HttpResponse
from django.http import JsonResponse
import json
class My_httpresponse_mixins(object):

      def render_response(self,data):
          return JsonResponse(data)

      def render_http_response(self,jsdata):
          data=json.dumps(jsdata)
          return HttpResponse(data,content_type='application/json')