from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework import permissions
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework.authentication import TokenAuthentication
from timesheet.serializers.clientes import Cliente, ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (permissions.AllowAny,)
    serializer_class = ClienteSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
