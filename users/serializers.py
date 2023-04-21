from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        fields = ('id', 'full_name', 'email',
                  'password', 'password2', 'date_joined', 'can_host')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        password2 = validated_data.pop('password2', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            if password != password2:
                raise serializers.ValidationError(
                    {'password': "Password not matched."})
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                if validated_data['password'] != validated_data['password2']:
                    raise serializers.ValidationError(
                        {'password': "Password not matched."})
                instance.set_password(value)
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance
