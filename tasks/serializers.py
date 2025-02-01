from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task  # Import the Task model

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'created_at', 'updated_at', 'user']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
