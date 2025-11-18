from django.db import models
from django.urls import reverse



# Make a contact card or footer note using this
class Contact(models.Model):
    platform_name = models.CharField(max_length=30)
    user_identifier = models.CharField(max_length=30)
    platform_icon = models.ImageField(upload_to='platform_icons/',blank=True,null=True)

    def __str__(self):
        return f"{self.platform_name} ({self.user_identifier})"
    
class QuickMenu(models.Model):
    title = models.CharField(max_length=30)
    overview = models.CharField(max_length=200)
    refimage = models.ImageField(upload_to='quickmenuimages/',blank=True,null=True)
    def __str__(self):
        return f"{self.title} "

# Feature system still underprogress
# Thinking about multiple features and loop over each feature each day if we run out then reloop and when it is updated continue the loop where we left off
class Featured(models.Model):
    title = models.CharField(max_length=50)
    overview = models.CharField(max_length=200)
    file = models.FileField(upload_to='featured/',blank=True,null=True)
    def __str__(self):
        return f"{self.title} "