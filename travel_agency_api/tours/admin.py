from django.contrib import admin
from .models import Tour, Booking, Review

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'price', 'created_at')
    search_fields = ('title', 'country')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'booking_date', 'number_of_people')
    list_filter = ('booking_date',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'rating', 'created_at')
    list_filter = ('rating',)