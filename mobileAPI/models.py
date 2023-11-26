from django.db import models
from rest_framework import serializers

# Create your models here.
class TestModel(models.Model):
    item = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    createdDate = models.DateField(auto_now_add=True)
    
class TestModelSerializer(serializers.ModelSerializer):
     # Map client's 'name' field to model's 'item' field
    name = serializers.CharField(source='item', max_length=255)
    # price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = TestModel
        fields = ['name', 'price']
        
    # class Meta:
    #     model = TestModel
    #     fields = '__all__'
    #     # fields = [item, price]

