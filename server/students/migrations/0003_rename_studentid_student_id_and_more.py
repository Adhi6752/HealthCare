# Generated by Django 4.1.1 on 2023-12-15 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='studentId',
            new_name='Id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Course',
            new_name='Text',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='FirstName',
        ),
        migrations.RemoveField(
            model_name='student',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='student',
            name='RegistrationNo',
        ),
    ]
