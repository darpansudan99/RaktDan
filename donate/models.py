from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.validators import validate_international_phonenumber


unit_choices = [
    ("AB-", "AB Negative"),
    ("AB+", "AB Positive"),
    ("A-", "A Negative"),
    ("A+", "A Positive"),
    ("B-", "B Negative"),
    ("B+", "B Positive"),
    ("O-", "O Negative"),
    ("O+", "O Positive")
]

class User(AbstractUser):
    gender_choice = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other")
    ]
    is_hospital = models.BooleanField(default = False)
    street = models.CharField (max_length=64)
    city = models.CharField (max_length=64)
    state = models.CharField (max_length=64)
    phone_no = models.CharField(max_length=15, unique=True,null=True, blank=True)
    dob = models.DateField(auto_now_add=False, blank=True, null=True)
    blood_type = models.CharField(choices=unit_choices, max_length=64, blank=True)
    gender = models.CharField(choices=gender_choice, max_length=1, blank=True)
    requests = models.ManyToManyField("User", blank=True, through="BloodRequest")

    def __str__(self):
        if self.is_hospital:
            return f'{self.username}'
        else:
            return f'{self.username} ({self.first_name} {self.last_name})'
    
    def serialize(self):
        return{
            "name": self.username,
            "city": self.city
        }


class BloodRequest(models.Model):
    hospital = models.ForeignKey("User", on_delete=models.CASCADE, related_name="requester")
    donor = models.ForeignKey("User", on_delete=models.CASCADE, related_name="requested_donor")
    status_choice = [
        ("P", "Pending"),
        ("A", "Accepted"),
        ("D", "Denied")
    ]
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=status_choice, max_length=1, default="P")

    def __str__(self):
        return f"{self.hospital} | {self.donor} | {self.donor.blood_type}"


class DonationPlace(models.Model):
    name = models.CharField(max_length=64,unique=True)
    street = models.CharField (max_length=64)
    city = models.CharField (max_length=64)
    state = models.CharField (max_length=64)
    phone_no = models.CharField(max_length=15, validators=[validate_international_phonenumber], unique=True)
    donors = models.ManyToManyField(User, blank=True, related_name="donations")

    def __str__(self):
        return f"{self.id}: {self.name} | {self.city}"


class BloodBank(models.Model):
    dp_no = models.OneToOneField(DonationPlace, on_delete=models.CASCADE, related_name="bank")

    def __str__(self):
        return f'{self.dp_no.name}'
    
    def serialize(self):
        return{
            "name": self.dp_no.name,
            "city": self.dp_no.city
        }


class DonationCamp(models.Model):
    dp_no = models.OneToOneField(DonationPlace, on_delete=models.CASCADE, related_name="camp")
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return f'{self.dp_no.name}'

    def save(self, *args, **kwargs):
        if self.end_date >= self.start_date:
            super().save(*args, **kwargs)  # Call the "real" save() method.
        else:
            print("error")
            return

    def serialize(self):
        return{
            "name": self.dp_no.name,
            "street": self.dp_no.street,
            "city": self.dp_no.city,
            "state": self.dp_no.state,
            "start_date": self.start_date,
            "end_date":self.end_date,
            "phone_no": self.dp_no.phone_no
        }


class BloodUnit(models.Model):

    blood_bank = models.ForeignKey("BloodBank", on_delete=models.CASCADE, related_name="blood_unit")
    blood_group = models.CharField(max_length=4, choices=unit_choices)
    no_of_units = models.IntegerField()

    def __str__(self):
        return f"{self.blood_bank} | {self.blood_group} | {self.no_of_units}"
    
    def serialize(self):
        return{
            "blood_bank": self.blood_bank.dp_no.name,
            "city": self.blood_bank.dp_no.city,
            "no_of_units": self.no_of_units
        }

    class Meta :
        unique_together = ("id", "blood_bank")