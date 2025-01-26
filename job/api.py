from rest_framework.response import Response
from .models import Job
from rest_framework.decorators import api_view
from .serializers import JobSerializer

@api_view(['GET'])
def joblistapi(request):
    all_jobs= Job.objects.all()
    data= JobSerializer(all_jobs, many= True).data
    return Response({'data': data})