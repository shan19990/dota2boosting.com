from django.db import models

class Account(models.Model):
    email = models.EmailField(blank=True, null=True)
    heroes = models.CharField(max_length=255,blank=True, null=True)
    region = models.CharField(max_length=100,blank=True, null=True)
    mmr = models.CharField(max_length=5)
    rank = models.CharField(max_length=20)
    behaviour = models.CharField(max_length=5)
    communication = models.CharField(max_length=5)
    hours_played = models.IntegerField()
    phone_number = models.BooleanField(default=False)
    add_friends = models.BooleanField(default=False)
    community_market = models.BooleanField(default=False)
    dota_plus_shard = models.IntegerField()
    steam_account_level = models.IntegerField()
    steam_account_age = models.IntegerField()
    steam_account_id = models.CharField(max_length=50)
    steam_account_password = models.CharField(max_length=255)
    email_account_password = models.CharField(max_length=255)
    email_account_id = models.EmailField()

    def __str__(self):
        return f"{self.email}'s Account"
