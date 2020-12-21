from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics


class LeadListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
