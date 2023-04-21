from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import SubmissionSerializer
from .models import Submission
from hackathons.models import Hackathon, Enrollment


class SubmissionAPIView(CreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        hackathon_id = self.kwargs.get('hackathon_id')
        user = request.user

        try:
            hackathon = Hackathon.objects.get(id=hackathon_id)
        except:
            raise ValidationError("Enter correct Hackathon id")

        try:
            Enrollment.objects.get(user=user.id, hackathon=hackathon.id)
        except:
            raise ValidationError("You are not enrolled for this hackathon")

        if Submission.objects.filter(user=user.id, hackathon=hackathon.id).exists():
            raise ValidationError(
                "You have already submitted for this hackathon")

        data = {'user': user.id, 'hackathon': hackathon.id, 'name': request.data.get(
            'name'), 'summary': request.data.get('summary')}

        if hackathon.submission_type == 'link':
            if request.data.get('submission_link') is None:
                raise ValidationError("Submission Link is required")
            data['submission_link'] = request.data.get('submission_link')
        elif hackathon.submission_type == 'image':
            if request.FILES.get('submission_image') is None:
                raise ValidationError("Submission Image is required")
            data['submission_image'] = request.FILES.get('submission_image')
        elif hackathon.submission_type == 'file':
            if request.FILES.get('submission_file') is None:
                raise ValidationError("Submission File is required")
            data['submission_file'] = request.FILES.get('submission_file')

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(hackathon=hackathon,
                        user=get_user_model().objects.get(id=user.id))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SubmissionListView(ListAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = Submission.objects.filter(user=self.request.user.id)
        return queryset
