from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    Catagory = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Teacher
        fields = '__all__'
class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Catagory
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'