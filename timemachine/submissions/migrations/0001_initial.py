# Generated by Django 2.0.2 on 2018-03-11 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restapi', '0014_auto_20180307_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('completed', models.BooleanField(default=False)),
                ('success', models.BooleanField(default=False)),
                ('error', models.TextField(blank=True)),
                ('execution_time_millis', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TestCaseJob',
            fields=[
                ('job_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='submissions.Job')),
            ],
            bases=('submissions.job',),
        ),
        migrations.AddField(
            model_name='job',
            name='solution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='restapi.Solution'),
        ),
        migrations.AddField(
            model_name='job',
            name='testcase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='restapi.TestCase'),
        ),
    ]
