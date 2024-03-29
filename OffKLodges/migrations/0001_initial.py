# Generated by Django 3.2.7 on 2023-01-21 07:50

import datetime
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
            name='AgentPersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_fname', models.CharField(max_length=200)),
                ('agent_lname', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('phone_number2', models.IntegerField(blank=True, null=True)),
                ('agent_email', models.EmailField(max_length=254)),
                ('home_address1', models.CharField(max_length=500)),
                ('home_address2', models.CharField(blank=True, max_length=500, null=True)),
                ('state', models.CharField(choices=[('abuja', 'Abuja'), ('abia', 'Abia'), ('adamawa', 'Adamawa'), ('anambra', 'Anambra'), ('akwa Ibom', 'Akwa Ibom'), ('bauchi', 'Bauchi'), ('bayelsa', 'Bayelsa'), ('benue', 'Benue'), ('borno', 'Borno'), ('cross River', 'cross River'), ('delta', 'Delta'), ('ebonyi', 'Ebonyi'), ('edo', 'Edo'), ('ekiti', 'Ekiti'), ('enugu', 'Enugu'), ('gombe', 'Gombe'), ('imo', 'Imo'), ('jigawa', 'Jigawa'), ('kaduna', 'Kaduna'), ('kano', 'Kano'), ('katsina', 'Katsina'), ('kebbi', 'kebbi'), ('kogi', 'Kogi'), ('kwara', 'Kwara'), ('lagos', 'Lagos'), ('nassarawa', 'Nassarawa'), ('niger', 'Niger'), ('ogun', 'Ogun'), ('ondo', 'Ondo'), ('osun', 'Osun'), ('oyo', 'Oyo'), ('plateau', 'Plateau'), ('rivers', 'Rivers'), ('sokoto', 'Sokoto'), ('taraba', 'Taraba'), ('yobe', 'Yobe'), ('zamfara', 'Zamfara')], max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FindRoomMate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email_i', models.EmailField(max_length=254)),
                ('state', models.CharField(choices=[('abuja', 'Abuja'), ('abia', 'Abia'), ('adamawa', 'Adamawa'), ('anambra', 'Anambra'), ('akwa Ibom', 'Akwa Ibom'), ('bauchi', 'Bauchi'), ('bayelsa', 'Bayelsa'), ('benue', 'Benue'), ('borno', 'Borno'), ('cross River', 'cross River'), ('delta', 'Delta'), ('ebonyi', 'Ebonyi'), ('edo', 'Edo'), ('ekiti', 'Ekiti'), ('enugu', 'Enugu'), ('gombe', 'Gombe'), ('imo', 'Imo'), ('jigawa', 'Jigawa'), ('kaduna', 'Kaduna'), ('kano', 'Kano'), ('katsina', 'Katsina'), ('kebbi', 'kebbi'), ('kogi', 'Kogi'), ('kwara', 'Kwara'), ('lagos', 'Lagos'), ('nassarawa', 'Nassarawa'), ('niger', 'Niger'), ('ogun', 'Ogun'), ('ondo', 'Ondo'), ('osun', 'Osun'), ('oyo', 'Oyo'), ('plateau', 'Plateau'), ('rivers', 'Rivers'), ('sokoto', 'Sokoto'), ('taraba', 'Taraba'), ('yobe', 'Yobe'), ('zamfara', 'Zamfara'), ("I don't care", "I don't care")], default="I don't care", max_length=200)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ("I don't care", "I don't care")], default="I don't care", max_length=200)),
                ('level', models.CharField(choices=[('100L', '100L'), ('200L', '200L'), ('300L', '300L'), ('400L', '400L'), ('500L', '500L'), ("I don't care", "I don't care")], default="I don't care", max_length=200)),
                ('earlywake', models.CharField(choices=[('early', 'Early'), ('late', 'Late'), ("I don't care", "I don't care")], default="I don't care", max_length=200)),
                ('noise', models.CharField(choices=[('silence', 'Silence'), ('background noise', 'Background noise'), ("I don't care", "I don't care")], default="I don't care", max_length=200)),
                ('organizedSpace', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ("I don't care", "I don't care")], default="I don't care", max_length=200)),
                ('grocries', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ("I don't care", "I don't care")], default="I don't care", max_length=200)),
                ('personalSpace', models.CharField(choices=[('spend time with my roomate', 'Spend time with my roomate'), ('have my own space and time', 'Have my own space and time'), ("I don't care", "I don't care")], default="I don't care", max_length=200)),
                ('disabilites', models.CharField(choices=[('allergies', 'Allergies'), ('disabilities', 'Disabilities'), ("I don't care", "I don't care")], default="I don't care", max_length=200)),
                ('date_created', models.DateTimeField(default=datetime.date.today)),
                ('match_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lodge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('homeImg', models.ImageField(blank=True, default='Profile-Photo-Place-Holder.PNG', null=True, upload_to='home_img')),
                ('self_con', models.CharField(default='1 Bedroom Self contain', max_length=200)),
                ('elec_water', models.CharField(default='Stable Electricity and Water', max_length=200)),
                ('distance', models.CharField(default='200 meters from school', max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('ref', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='Profile-Photo-Place-Holder.png', upload_to='profile_pics')),
                ('uni_level', models.CharField(choices=[('100L', '100L'), ('200L', '200L'), ('300L', '300L'), ('400L', '400L'), ('500L', '500L')], default='100L', max_length=200)),
                ('phone_number', models.IntegerField(null=True)),
                ('email', models.EmailField(default='egwusamuel2015@gmail.com', max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LodgeProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sorrounding', models.ImageField(blank=True, null=True, upload_to='home_img')),
                ('lodge_interior', models.ImageField(blank=True, null=True, upload_to='home_img')),
                ('roomFront', models.ImageField(blank=True, null=True, upload_to='home_img')),
                ('roomBack', models.ImageField(blank=True, null=True, upload_to='home_img')),
                ('roomKitchen', models.ImageField(blank=True, null=True, upload_to='home_img')),
                ('roomToiletBath', models.ImageField(blank=True, null=True, upload_to='home_img')),
                ('bedRoom', models.ImageField(blank=True, null=True, upload_to='home_img')),
                ('roomsTotalNum', models.PositiveSmallIntegerField()),
                ('roomsAvailable', models.PositiveSmallIntegerField()),
                ('lodge', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='OffKLodges.lodge')),
            ],
        ),
        migrations.CreateModel(
            name='BookedLodge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('price', models.IntegerField()),
                ('lodge', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='OffKLodges.lodge')),
            ],
        ),
        migrations.CreateModel(
            name='AgentProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lodge_name', models.CharField(max_length=200, null=True)),
                ('homeImg', models.ImageField(default='Profile-Photo-Place-Holder.png', upload_to='agent_img')),
                ('sorrounding', models.ImageField(default='Profile-Photo-Place-Holder.png', upload_to='agent_img')),
                ('lodge_interior', models.ImageField(default='Profile-Photo-Place-Holder.png', upload_to='agent_img')),
                ('roomFront', models.ImageField(default='Profile-Photo-Place-Holder.png', upload_to='agent_img')),
                ('roomBack', models.ImageField(default='Profile-Photo-Place-Holder.png', upload_to='agent_img')),
                ('roomKitchen', models.ImageField(default='Profile-Photo-Place-Holder.png', upload_to='agent_img')),
                ('roomToiletBath', models.ImageField(default='Profile-Photo-Place-Holder.png', upload_to='agent_img')),
                ('bedRoom', models.ImageField(default='Profile-Photo-Place-Holder.png', upload_to='agent_img')),
                ('price', models.FloatField()),
                ('elec_water', models.CharField(default='Stable Electricity and Water', max_length=200)),
                ('distance', models.CharField(default='200 meters from school', max_length=200)),
                ('roomsTotalNum', models.PositiveSmallIntegerField()),
                ('roomsAvailable', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('agent_ersonal_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OffKLodges.agentpersonalinfo')),
            ],
        ),
    ]
