from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db import IntegrityError
from django.http import JsonResponse

from .models import TestModel,TestModelSerializer


#DECLARE VAR
STATUS_KEY = 'status'

# Create your views here.

def testAPI(request):
    queryset = TestModel.objects.all()
    dataSerializer = TestModelSerializer(queryset, many=True).data
    return JsonResponse({
        STATUS_KEY:True,
        'data':dataSerializer
    })
    
@csrf_exempt
def testPost(request, *args, **kwargs):
    if request.method == 'POST':
        
        serializer = TestModelSerializer(data=request.POST)
        
        if serializer.is_valid():
            # Check if an item with the same name already exists
            item_name = serializer.validated_data['item']
            
            if TestModel.objects.filter(item=item_name).exists():
                return JsonResponse({STATUS_KEY:False, 'message':'item already exists'})
            # # If the input data is valid, create a new item
            serializer.save()
            return JsonResponse({STATUS_KEY:True, 'message':'item saved successfuly'})
        else:
            return JsonResponse({STATUS_KEY:False, 'message':'Invalid Request'})
        # tes = TestModel(item='item1', price=12.99)
        # try:
        #     # Save the instance
        #     tes.save()
        # except IntegrityError as error:
        #     # Handle the exception
        #     print(error)
        # return JsonResponse({
        #     STATUS_KEY:True,
        #     'message':'success'
        # })
    else:
        return JsonResponse({
            STATUS_KEY:False,
            'message':'invalid request'
        })
    