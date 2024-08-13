from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Certif
from .serialicers import CertifSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        "GET /api",
        "GET /api/certifs",
        "GET /api/certifs/:id"
    ]
    return Response(routes)

@api_view(['GET'])
def get_certifs(request):
    certifs = Certif.objects.all()
    serializer = CertifSerializer(certifs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_certif(request, id):
    certif = Certif.objects.get(id=id)
    serializer = CertifSerializer(certif, many=False)
    return Response(serializer.data) 