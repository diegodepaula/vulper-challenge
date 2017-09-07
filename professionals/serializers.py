from rest_framework.serializers import ModelSerializer
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from .models import Professional

class ProfessionalSerializer(ModelSerializer):

	class Meta:
		model = Professional
		fields = '__all__'


class ProfessionalPagination(PageNumberPagination):
	page_size = settings.DEFAULT_PAGE_SIZE