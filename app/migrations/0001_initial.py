# Generated by Django 4.2.3 on 2023-08-17 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DEPT',
            fields=[
                ('DNAME', models.CharField(max_length=100)),
                ('LOCATION', models.CharField(max_length=100)),
                ('DEPTNO', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EMP',
            fields=[
                ('EMPNO', models.IntegerField(primary_key=True, serialize=False)),
                ('ENAME', models.CharField(max_length=100)),
                ('JOB', models.CharField(max_length=100)),
                ('HIREDATE', models.DateField()),
                ('SAL', models.IntegerField()),
                ('COMM', models.IntegerField(blank=True, null=True)),
                ('DEPTNO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
