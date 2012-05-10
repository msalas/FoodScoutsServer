from django.http import HttpResponse
from django.core import serializers
from items.models import *


def recommendations(request):
    data = serializers.serialize('json', Item.objects.all(),indent=4)
    response = HttpResponse(data, mimetype='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response

def items(request):
	    data = serializers.serialize('json', Item.objects.all(),indent=4)
	    response = HttpResponse(data, mimetype='application/json')
	    response['Access-Control-Allow-Origin'] = '*'
	    return response

def my_reviews(request,user_id):
    data = serializers.serialize('json', Review.objects.filter(user=user_id),indent=4,relations=('item'))
    response = HttpResponse(data, mimetype='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response

def my_bookmarks(request,user_id):
    data = serializers.serialize('json', Bookmark.objects.filter(user=user_id),indent=4,relations=('item'))
    response = HttpResponse(data, mimetype='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response

def reviews(request,item_id):
    data = serializers.serialize('json', Review.objects.filter(item=item_id),indent=4,relations={'user':{'fields':('username')}})
    response = HttpResponse(data, mimetype='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response
