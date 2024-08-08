# tareas/migrations/0001_initial.py

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # ('another_app', 'some_migration'),  # Asegúrate de que esto no crea una referencia circular
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
               
            ],
        ),
    ]
