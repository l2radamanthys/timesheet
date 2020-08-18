from rest_framework import viewsets
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from timesheet.serializers.users import User, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # resource_name = 'users'
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny,)
    # http_method_names = ['get']
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='mi-perfil')
    def mi_perfil(self, request, *args, **kwargs):
        perfil = request.user
        data = {
            'id': perfil.id,
            'username': perfil.username,
            'nombre': perfil.first_name,
            'apellido': perfil.last_name,
            'email': perfil.email,
            'es_admin': perfil.is_superuser
        }
        return Response(data)
