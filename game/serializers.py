from rest_framework import serializers
from .models import Player, Refree
class AddPlayerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
    class Meta:
        model= Player
        fields=('username','password','defencive_array','attacking_no')

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model= Player
        exclude=('first_name','last_name','email','is_staff','date_joined','groups','user_permissions','is_superuser','last_login', 'is_active','password',)

class RefreeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Refree
        fields='__all__'