from csvparser.models import UserProfile
from .serializers import UserSerializer



class Users(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

