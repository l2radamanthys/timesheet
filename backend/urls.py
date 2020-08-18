from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView, RedirectView
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from timesheet.views.clientes import ClienteViewSet
from timesheet.views.proyectos import ProyectoViewSet
from timesheet.views.tareas import TareaViewSet
from timesheet.views.users import UserViewSet
from timesheet.views.tareas_proyecto import TareaProyectoViewSet
admin.site.site_header = 'TimeSheet'

router = routers.DefaultRouter(trailing_slash=False)
router.register('clientes', ClienteViewSet)
router.register('proyectos', ProyectoViewSet)
router.register('tareas', TareaViewSet)
router.register('users', UserViewSet)
router.register('tareas-proyectos', TareaProyectoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth', obtain_auth_token),
    path('api/', include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),
]
