import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_passage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='passage_id',
            field=models.CharField(default=uuid.UUID('4a3e1dbb-31ec-4d29-8c8c-4bdad05002e4'), max_length=255, unique=True),
            field=models.CharField(default=uuid.UUID('f2ff1d20-ecd0-4797-9e96-c90efb8296b1'), max_length=255, unique=True),
        ),
    ]
