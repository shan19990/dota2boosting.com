from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='wallet')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    PERKS_CHOICES = [
        ('', 'Default'),
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('diamond', 'Diamond'),
        ('platinum', 'Platinum'),
    ]
    perk = models.CharField(max_length=10, choices=PERKS_CHOICES, default='')
    total_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.user.username}\'s Wallet'

class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE , related_name='transaction')
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    change = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction for {self.wallet.user.username} at {self.transaction_date}'
