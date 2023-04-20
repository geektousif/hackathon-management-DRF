from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated

from .serializers import SubmissionSerializer
from .models import Submission
from hackathons.models import Hackathon


class SubmissionCreateAPIView(CreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        hackathon_id = self.kwargs.get('hackathon_id')
        hackathon = Hackathon.objects.get(id=hackathon_id)

        submission_type = serializer.validated_data['content_type']

        if submission_type != hackathon.submission_type:
            raise ValidationError("Invalid submission type")

        serializer.save(user=self.request.user, hackathon=hackathon)


class SubmissionListView(ListAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = Submission.objects.filter(user=self.request.user.id)
        return queryset
