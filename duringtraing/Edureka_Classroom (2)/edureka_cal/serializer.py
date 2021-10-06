from rest_framework import serializers
from .models import Instructor

class InstructorSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100)
    # specialization = serializers.CharField(max_length=200)
    class Meta:
        model = Instructor
        fields = '__all__'

    def validate_specialization(self, value):
        if 'python' not in value.lower():
            raise serializers.ValidationError("Have to be specialized in Python")
        return value
    # def create(self, validated_data):
    #     return Instructor.objects.create(**validated_data)
    #
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.specialization = validated_data.get('specialization', instance.specialization)
    #     instance.save()
    #     return instance

