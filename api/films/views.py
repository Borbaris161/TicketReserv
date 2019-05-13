from rest_framework.views import APIView

from rest_framework import (
    status,
    generics)

from rest_framework.decorators import (
    api_view,
    permission_classes
)

from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
)

from rest_framework.response import Response

from .serializers import FilmSerializer

from .models import Film


@api_view(['POST'])
@permission_classes([IsAdminUser, ])
def create_film(request):
    if request.user:
        film = request.data
        serializer = FilmSerializer(data=film)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Create': 'films with title %s' % request.data['title']}, status=status.HTTP_201_CREATED)


class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = FilmSerializer


    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)