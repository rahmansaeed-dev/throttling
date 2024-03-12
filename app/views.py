from .models import Person
from  .serilizers import PersonModelSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from rest_framework.authentication import SessionAuthentication
from app.throttling import MyThrottleClass

class ModelViewSetview(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,MyThrottleClass]



