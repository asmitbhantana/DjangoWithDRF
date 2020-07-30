from rest_framework import serializers
from .models import Info


class AddTwoNumbersSerializers(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()


class InfoSerailizers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=200)

    def create(self, validated_data):
        print("context is", self.context)
        return Info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        name = validated_data['name']
        address = validated_data['address']
        instance.name = name
        instance.address = address
        instance.save()
        return instance


class InfoModelSerializers(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()

    class Meta:
        model = Info
        fields = ['name', 'address', 'message', 'id']
        read_only_fields = ['id']

    @staticmethod
    def get_message(obj):
        name = obj.name
        return f"hi, my name is {name}"

    @staticmethod
    def validate_name(name):
        if len(name) <= 2:
            raise serializers.ValidationError(detail="Name field should not be smaller than length 2")
        return name

    def validate(self, attrs):
        name = attrs['name']
        address = attrs['address']

        if name == address:
            raise serializers.ValidationError(detail="Name and address cannot be same!")

        return attrs
