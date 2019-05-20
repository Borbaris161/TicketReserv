from rest_framework import serializers
from .models import User
from django.db import transaction, IntegrityError


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'})
    tickets = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'created',
                  'password',
                  'tickets'
                  )

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail('cannot_create_user')
        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            user.is_active = False
            user.set_password(validated_data['password'])
            user.save()
            user.save(update_fields=['is_active'])
        return user
