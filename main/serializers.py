from rest_framework import serializers
from .models import SmartBin, Pickup, WasteReport,Feedback,UserProfile

class SmartBinSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartBin
        fields = '__all__'  
        
class PickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pickup
        fields = '__all__'
        
class WasteReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteReport
        fields = '__all__'
        
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
        
        
        

