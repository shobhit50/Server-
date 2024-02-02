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