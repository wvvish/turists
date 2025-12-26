from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tour, Booking, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
 
class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tour = TourSerializer(read_only=True)
    tour_id = serializers.PrimaryKeyRelatedField(
        queryset=Tour.objects.all(), write_only=True, source='tour'
    )

    class Meta:
        model = Booking
        fields = ['id', 'user', 'tour', 'tour_id', 'booking_date', 'number_of_people']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tour = TourSerializer(read_only=True)
    tour_id = serializers.PrimaryKeyRelatedField(
        queryset=Tour.objects.all(), write_only=True, source='tour'
    )

    class Meta:
        model = Review
        fields = ['id', 'user', 'tour', 'tour_id', 'rating', 'comment', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)