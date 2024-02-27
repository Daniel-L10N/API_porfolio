from rest_framework import viewsets
from .serializer import IncentivesSerializer
from .models import Incentive

class IncentivesViewSet(viewsets.ModelViewSet):
    queryset = Incentive.objects.all()
    serializer_class = IncentivesSerializer
    


