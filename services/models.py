from django.db import models
from django.contrib.auth.models import User
from boosters.models import BoosterProfile

STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('inprogress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

DOTA2_SERVER_CHOICES = [
    ('us_west', 'North America (US West)'),
    ('us_east', 'North America (US East)'),
    ('eu_west', 'Europe West'),
    ('eu_east', 'Europe East'),
    ('sea', 'Southeast Asia'),
    ('china', 'China'),
    ('russia', 'Russia'),
    ('sa', 'South America'),
    ('australia', 'Australia'),
    ('india', 'India'),
]


class MMRBoostingJob(models.Model):
    
    RANK_CONFIDENCE_CHOICES = [
        (0, '0-33'),
        (1, '34-66'),
        (2, '64-99'),
    ]

    user = models.ForeignKey(User, related_name='mmrboost_user', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    booster = models.ForeignKey(BoosterProfile, related_name='mmrboost_booster', on_delete=models.SET_NULL, null=True, blank=True)
    rank_confidence = models.IntegerField(choices=RANK_CONFIDENCE_CHOICES)
    current_mmr = models.IntegerField()
    desired_mmr = models.IntegerField()
    duo_queue = models.BooleanField(default=False)
    streaming = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)
    hero_preference = models.BooleanField(default=False)
    play_offline = models.BooleanField(default=False)
    server = models.CharField(max_length=20, choices=DOTA2_SERVER_CHOICES)
    
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    coupon_active = models.BooleanField(default=True)
    
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    deadline = models.DateField()

    def save(self, *args, **kwargs):
        if self.user:
            self.name = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"MMRBoostingJob(user={self.name}, status={self.status} ,current_mmr={self.current_mmr}, desired_mmr={self.desired_mmr})"

class Coaching(models.Model):
    user = models.ForeignKey(User, related_name='coaching_user', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    booster = models.ForeignKey(BoosterProfile, related_name='coached_booster', on_delete=models.SET_NULL, null=True, blank=True)
    hours = models.IntegerField()
    duo_queue = models.BooleanField(default=False)
    streaming = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)
    play_offline = models.BooleanField(default=False)
    server = models.CharField(max_length=20, choices=DOTA2_SERVER_CHOICES)
    
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    coupon_active = models.BooleanField(default=True)
    
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    deadline = models.DateField()

    def save(self, *args, **kwargs):
        if self.user:
            self.name = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Coaching(user={self.name}, status={self.status} , hours={self.hours}, total_value={self.total_value})"

class BehaviousScore(models.Model):
    BEHAVIOR_SCORE_CHOICES = [(i, str(i)) for i in range(1000, 13000, 1000)]

    user = models.ForeignKey(User, related_name='behaviour_user', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    booster = models.ForeignKey(BoosterProfile, related_name='behaviour_booster', on_delete=models.SET_NULL, null=True, blank=True)
    current_behavior_score = models.IntegerField(choices=BEHAVIOR_SCORE_CHOICES)
    desired_behavior_score = models.IntegerField(choices=BEHAVIOR_SCORE_CHOICES)
    duo_queue = models.BooleanField(default=False)
    streaming = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)
    play_offline = models.BooleanField(default=False)
    server = models.CharField(max_length=20, choices=DOTA2_SERVER_CHOICES)
    
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    coupon_active = models.BooleanField(default=True)
    
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    deadline = models.DateField()

    def save(self, *args, **kwargs):
        if self.user:
            self.name = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"BehaviousScore(user={self.name}, status={self.status} , current_behavior_score={self.current_behavior_score}, desired_behavior_score={self.desired_behavior_score})"

class LowPriority(models.Model):
    LOW_PRIORITY_GAME_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(User, related_name='low_priority_user', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    booster = models.ForeignKey(BoosterProfile, related_name='low_priority_booster', on_delete=models.SET_NULL, null=True, blank=True)
    low_priority_games = models.IntegerField(choices=LOW_PRIORITY_GAME_CHOICES)
    duo_queue = models.BooleanField(default=False)
    streaming = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)
    play_offline = models.BooleanField(default=False)
    server = models.CharField(max_length=20, choices=DOTA2_SERVER_CHOICES)
    
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    coupon_active = models.BooleanField(default=True)
    
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    deadline = models.DateField()

    def save(self, *args, **kwargs):
        if self.user:
            self.name = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"LowPriority(user={self.name}, status={self.status} , low_priority_games={self.low_priority_games}, total_value={self.total_value})"

class BattleCup(models.Model):
    user = models.ForeignKey(User, related_name='battlecup_user', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    booster = models.ForeignKey(BoosterProfile, related_name='battlecup_booster', on_delete=models.SET_NULL, null=True, blank=True)
    tier = models.IntegerField()
    duo_queue = models.BooleanField(default=False)
    streaming = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)
    play_offline = models.BooleanField(default=False)
    server = models.CharField(max_length=20, choices=DOTA2_SERVER_CHOICES)
    
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    coupon_active = models.BooleanField(default=True)
    
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    deadline = models.DateField()

    def save(self, *args, **kwargs):
        if self.user:
            self.name = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"BattleCup(user={self.name} , status={self.status}, tier={self.tier}, total_value={self.total_value})"
    

class NormalWins(models.Model):

    NORMAl_WINS = [(i, str(i)) for i in range(1, 100)]

    user = models.ForeignKey(User, related_name='normalwins_user', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    booster = models.ForeignKey(BoosterProfile, related_name='normalwins_booster', on_delete=models.SET_NULL, null=True, blank=True)
    normal_games = models.IntegerField(choices=NORMAl_WINS)
    duo_queue = models.BooleanField(default=False)
    streaming = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)
    play_offline = models.BooleanField(default=False)
    server = models.CharField(max_length=20, choices=DOTA2_SERVER_CHOICES)
    
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    coupon_active = models.BooleanField(default=True)
    
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    deadline = models.DateField()

    def save(self, *args, **kwargs):
        if self.user:
            self.name = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Normal Wins(user={self.name}, status={self.status}, normal_games={self.normal_games}, total_value={self.total_value})"

