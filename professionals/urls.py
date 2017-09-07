from django.conf.urls import url
from .views import ProfessionalListView

urlpatterns = [
	url(r'^professional', ProfessionalListView.as_view(), name='professionals-list'),
]