from django.http import HttpResponse
from django.core import serializers
from items.models import Item

def index(request):
    data = serializers.serialize('json', Item.objects.all(),indent=4)
    return HttpResponse(data, mimetype='application/json')