# Generated by Django 3.1.7 on 2022-04-17 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessPlanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planid', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('section1', 'section1'), ('section2', 'section2')], max_length=10)),
                ('question', models.CharField(max_length=100)),
                ('ans1', models.CharField(blank=True, max_length=50, null=True)),
                ('ans2', models.CharField(blank=True, max_length=50, null=True)),
                ('ans3', models.CharField(blank=True, max_length=50, null=True)),
                ('text_question', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPlanQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=50)),
                ('businessplanid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.businessplanmodel')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.question')),
            ],
        ),
    ]
