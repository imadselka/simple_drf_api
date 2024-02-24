from rest_framework.response import Response
from rest_framework.decorators import api_view  # Import the api_view decorator
from base.models import User  # Import the User class
from .serializers import UserSerializer  # Import the UserSerializer class

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)