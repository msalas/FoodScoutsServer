from django.http import HttpResponse
from django.core import serializers
from items.models import *
from django.db.models import Avg
from django.db.models import Q

def recommendations(request,user_id):
   #data = serializers.serialize('json', Item.objects.annotate(average=Avg('review__rating')).exclude(review__user=user_id).filter(Q(average__gt=3) | Q(review__isnull=True)).order_by('-average').distinct('id'),indent=4)
    data = serializers.serialize('json', Item.objects.raw('select distinct * from items_item ii where ii.id not in (select item_id from items_review where user_id=%s) and (3<=(select avg(rating) from items_review where ii.id=item_id) or ii.id not in (select item_id from items_review)) order by (select avg(rating) from items_review where ii.id=item_id) desc',[user_id]),indent=4)
    response = HttpResponse(data, mimetype='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response

def items(request):
	    data = serializers.serialize('json', Item.objects.order_by('name'),indent=4)
	    response = HttpResponse(data, mimetype='application/json')
	    response['Access-Control-Allow-Origin'] = '*'
	    return response

def my_reviews(request,user_id):
    data = serializers.serialize('json', Review.objects.filter(user=user_id).order_by('-pub_date'),indent=4,relations=('item'))
    response = HttpResponse(data, mimetype='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response

def my_bookmarks(request,user_id):
    data = serializers.serialize('json', Bookmark.objects.filter(user=user_id).exclude(item__review__user=user_id).order_by('-id'),indent=4,relations=('item'))
    response = HttpResponse(data, mimetype='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response

def reviews(request,item_id):
    data = serializers.serialize('json', Review.objects.filter(item=item_id).order_by('-pub_date'),indent=4,relations={'user':{'fields':('username')}})
    response = HttpResponse(data, mimetype='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    return response
