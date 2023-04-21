from django.urls import path

from .views import SubmissionAPIView, SubmissionListView

urlpatterns = [
    path('hackathon_<int:hackathon_id>/make_submission',
         SubmissionAPIView.as_view(), name='make_submission'),
    path('my_submissions', SubmissionListView.as_view(), name='my_submissions'),

]
