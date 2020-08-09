from rest_framework import serializers
from csvparser.models import UserProfile, Orders


class OrdersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Orders
    fields = ('start_date', 'goods')

class UserSerializer(serializers.ModelSerializer):
  order = OrdersSerializer(read_only=True)

  class Meta:
    model = UserProfile
    fields = ('first_name',
              'last_name',
              'birthday',
              'registration_date',
              'order')