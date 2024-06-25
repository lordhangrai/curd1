from django.db import models

# Create your models here.
STATE_CHOICE = (
('Purbaanchal','Purbaanchal'),
('Madeshperdesh','Madeshperdesh'),
('Bagmati Perdesh','Bagmati Perdesh'),
('Gandaki perdesh', 'Gandaki Perdesh'),
('Lumbani Perdesh', 'Lumbani Perdesh'),
('Karnali Perdesh', 'Karnali Perdesh'),
('Suderpashim Perdesh', 'Suderpashim Perdesh'),
)

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


class Resume(models.Model):
  name = models.CharField(max_length=100)
  dob = models.DateField(auto_now=False, auto_now_add=False)
  gender = models.CharField(max_length=100)
  locality = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  pin = models.PositiveIntegerField()
  state = models.CharField(choices=STATE_CHOICE, max_length=50)
  mobile = models.PositiveIntegerField()
  email = models.EmailField()
  job_city = models.CharField(max_length=50)
  profile_image = models.ImageField(upload_to='profileimg', blank=True)
  my_file = models.FileField(upload_to='doc', blank=True)
