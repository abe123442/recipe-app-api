"""
Views for the user API
"""

from rest_framework import generics

from user.serialisers import UserSerialiser

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerialiser


# Create your views here.
