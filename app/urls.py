from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BranchList, Ifsc

urlpatterns = [
    path('branchlist/', BranchList.as_view()),
    path('ifsc/<str:ifsc>/', Ifsc.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

