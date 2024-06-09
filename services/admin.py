# Admin configuration
from django.contrib import admin
from .models import *

admin.site.register(MMRBoostingJob)
admin.site.register(Coaching)
admin.site.register(BehaviousScore)
admin.site.register(BattleCup)
admin.site.register(LowPriority)
admin.site.register(NormalWins)