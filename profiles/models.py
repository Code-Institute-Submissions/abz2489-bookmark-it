from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

from books.models import Book


class UserProfile(models.Model):
    """User profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True)
    default_street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True)
    default_street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True)
    default_town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True)
    default_county = models.CharField(
        max_length=80,
        null=True,
        blank=True)
    default_postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True)
    default_country = CountryField(
        blank_label='Country',
        null=True,
        blank=True)
    
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class Bookmark(models.Model):
    """Bookmark model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        """Bookmark model constraint to ensure unique users and books"""
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'], name='unique_user_book')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"