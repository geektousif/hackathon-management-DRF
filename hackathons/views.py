from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import HackathonSerializer, EnrollmentSerializer
from .models import Hackathon, Enrollment


class CreateHackathonView(CreateAPIView):
    serializer_class = HackathonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class ListHackathonView(ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


class EnrollHackathonView(CreateAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        hackathon = Hackathon.objects.filter(id=pk).first()
        serializer.save(user=self.request.user, hackathon=hackathon)


class ListEnrolledHackathonView(ListAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        queryset = Enrollment.objects.filter(user=user)
        return queryset
