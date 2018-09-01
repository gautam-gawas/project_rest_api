from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name')

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('id','user')

class ProjectSerializer(serializers.ModelSerializer):
    last_updated_on = serializers.DateTimeField(format=("%d %b"),read_only= True, required=False)
    created_on = serializers.DateTimeField(format=("%d %b, %Y"),read_only= True,  required=False)
    profile = ProfileSerializer(many=True,write_only=True)

    class Meta:
        model = Project
        fields = ( 'id','project_name', 'form_submitted','total',
                   'last_updated_on','created_on','description','count','profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        project = Project.objects.create(**validated_data)
        for profile in profile_data:
            Profile.objects.create(album=project, **profile)
        return project

class FormSerializer(serializers.ModelSerializer):
    updated_on = serializers.DateTimeField(format=("%d %b"),read_only= True,  required=False)
    created_on = serializers.DateTimeField(format=("%d %b, %Y"),read_only= True,  required=False)

    class Meta:
        model = Form
        fields = ( '__all__')

