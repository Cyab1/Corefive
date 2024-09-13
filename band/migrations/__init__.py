from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("band", "previous_migration"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
