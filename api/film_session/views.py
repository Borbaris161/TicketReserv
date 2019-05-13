from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import \
    (status, generics)

from rest_framework.permissions import \
    (AllowAny, IsAdminUser)


from .serializers import FilmSessionSerializer


class CreateSessionAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        session = request.data
        serializer = FilmSessionSerializer(data=session)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SessionList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FilmSessionSerializer

    def list(self, request):
        serializer = self.serializer_class(data=request.user, many=True)
        return Response(serializer.data)