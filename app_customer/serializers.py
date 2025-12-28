from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    created_up = serializers.DateTimeField(format="%d %B %Y, %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %B %Y, %I:%M %p", read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'address', 'department', 'created_up', 'updated_at')



# Serializer convert the complex Django objects into Python native data, so that they can be received by JSOn ( Vice Versa)

# class CustomerSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=50)
#     department = serializers.CharField(max_length=50)
#     created_up = serializers.DateTimeField(
#         format="%d %b %Y, %I:%M %p"                               # %b this will give the month as 3 letters word
#     )