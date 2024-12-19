from django.db import models


# The model for Homes with all the required fields and validation for each field
class Home(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    emailAddress = models.EmailField()
    addressFirstLine = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    homeNotes = models.CharField(max_length=500)


# The model for Vacant Homes with all the required fields and validation for each field
class VacantHome(models.Model):
    addressFirstLine = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    dateOfLastOccupancy = models.DateField()
    homeNotes = models.CharField(max_length=500)

