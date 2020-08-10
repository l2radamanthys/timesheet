from django.db import migrations
from django.contrib.auth.models import User


def crear_usuario_administrador(apps, schema_editor):
    User.objects.create_superuser(username='admin', password='asdasd123', email='admin@admin.com')


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunPython(crear_usuario_administrador, migrations.RunPython.noop),
    ]
