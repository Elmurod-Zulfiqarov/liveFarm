from rest_framework import serializers
from .models import Farm, Pet, Milk, Fodder


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class MilkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milk
        fields = '__all__'


class FodderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fodder
        fields = '__all__'
