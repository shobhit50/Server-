from rest_framework import serializers
from .models import Data , Webhook
from bson import ObjectId

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields=('name','description')

class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webhook
        fields = '__all__'  
    # def create(self, validated_data):
    #     # Convert the string representation of ObjectId to an ObjectId object
    #     validated_data['id'] = ObjectId(validated_data['id'])
    #     return Webhook.objects.create(**validated_data)