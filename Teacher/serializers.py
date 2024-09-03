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
        fields = ['id', 'body', 'created', 'rating', 'reviewer', 'course']
    def get_reviewer_name(self, obj):
        return obj.reviewer.username  # Or obj.reviewer.get_full_name() if you want the full name

    def get_course_name(self, obj):
        return obj.course.title