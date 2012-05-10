from django.http import HttpResponse
from django.core import serializers
from items.models import *

def index(request):
#    data = serializers.serialize('json', Review.objects.all(),indent=4,relations=('user','item',))
#    i = Item.objects.get(id=1)

    data = serializers.serialize('json', Item.objects.all(),indent=4,relations=('review','bookmark',))
    response = HttpResponse(data, mimetype='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response