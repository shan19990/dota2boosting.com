from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import MMRBoostingJob, Coaching, BehaviousScore, LowPriority, BattleCup, NormalWins

@receiver(post_save, sender=MMRBoostingJob)
@receiver(post_save, sender=Coaching)
@receiver(post_save, sender=BehaviousScore)
@receiver(post_save, sender=LowPriority)
@receiver(post_save, sender=BattleCup)
@receiver(post_save, sender=NormalWins)
def update_booster_profile(sender, instance, created, **kwargs):
    if instance.status == 'completed' and instance.booster:
        instance.booster.orders_completed += 1
        instance.booster.save()
