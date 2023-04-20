from django.urls import path

from .views import CreateHackathonView, ListHackathonView, EnrollHackathonView, ListEnrolledHackathonView

urlpatterns = [
    path('create', CreateHackathonView.as_view(), name='create_hackathon'),
    path('list', ListHackathonView.as_view(), name='list_hackathons'),
    path('<int:pk>/enroll', EnrollHackathonView.as_view(),
         name='enroll_to_hackathon'),
    path('my_enrollments', ListEnrolledHackathonView.as_view(), name='enrolled_hackathons')
]
