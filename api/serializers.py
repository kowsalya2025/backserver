from rest_framework import serializers
from .models import MiniProject

class MiniProjectSerializer(serializers.ModelSerializer):
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = MiniProject
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at', 'updated_at')
