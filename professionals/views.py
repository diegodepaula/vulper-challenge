from rest_framework.views import APIView
from .models import Professional
from .serializers import ProfessionalSerializer, ProfessionalPagination
from django.http import HttpResponse
import requests
import json

class ProfessionalListView(APIView):

	def get(self, *args, **kwargs):
		language = self.request.GET.get('language')
		location = self.request.GET.get('location')
		url = "https://api.github.com/search/users?q=language:{}+location:{}&type=Users".format(language, location)

		result = requests.get(url).json()
		professionals = []
		for item in result['items']:
			professional = Professional()
			professional.login = item['login']
			professional.picture = item['avatar_url']
			if item['score'] < 3.5:
				professional.classification = 'Aprendiz Jedi'
			else:
				professional.classification = 'Cavaleiro Jedi'

			professionals.append(professional)

		serializer = ProfessionalSerializer(data=professionals, many=True)
		serializer.is_valid()
		return HttpResponse(json.dumps(serializer.data))
