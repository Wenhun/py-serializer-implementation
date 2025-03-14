from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(required=True, max_length=64)
    model = serializers.CharField(required=True, max_length=64)
    horse_powers = serializers.IntegerField(
        required=True, max_value=1914, min_value=1)
    is_broken = serializers.BooleanField(required=True)
    problem_description = serializers.CharField(required=False)

    def create(self, validated_data: dict) -> Car:
        return Car.objects.create(**validated_data)

    def update(self, instance: Car, validated_data: dict) -> Car:
        instance_manufacturer = validated_data.get(  # noqa: F841
            "manufacturer", instance.manufacturer)
        instance_model = validated_data.get(  # noqa: F841
            "model", instance.model)
        instance_horse_powers = validated_data.get(  # noqa: F841
            "horse_powers", instance.horse_powers)
        instance_is_broken = validated_data.get(  # noqa: F841
            "is_broken", instance.is_broken)
        instance_problem_description = validated_data.get(  # noqa: F841
            "problem_description", instance.problem_description)
        instance.save()
        return instance
