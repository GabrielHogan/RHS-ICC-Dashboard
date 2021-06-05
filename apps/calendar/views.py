import os
from django.utils import timezone
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rhs_icc_dashboard.permissions import IsGet
from .serializers import *

class EventsListView(APIView):
    permission_classes = [IsGet]

    def get(self, request):
        """
        Get list of all events.
        """
        events = Event.objects.all()

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Add a new event.
        """
        serializer = EventSerializer(request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)