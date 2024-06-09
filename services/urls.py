from django.urls import path
from . import views

urlpatterns = [
    path('mmrboostingjobs/', views.MMRBoostingJobListCreate.as_view(), name='mmrboostingjob-list'),
    path('mmrboostingjobs/<int:id>/', views.MMRBoostingJobRetrieveUpdateDelete.as_view(), name='mmrboostingjob-detail'),

    path('coaching/', views.CoachingListCreate.as_view(), name='coaching-list'),
    path('coaching/<int:id>/', views.CoachingRetrieveUpdateDelete.as_view(), name='coaching-detail'),

    path('behaviourscores/', views.BehaviousScoreListCreate.as_view(), name='behaviourscore-list'),
    path('behaviourscores/<int:id>/', views.BehaviousScoreRetrieveUpdateDelete.as_view(), name='behaviourscore-detail'),

    path('lowpriority/', views.LowPriorityListCreate.as_view(), name='lowpriority-list'),
    path('lowpriority/<int:id>/', views.LowPriorityRetrieveUpdateDelete.as_view(), name='lowpriority-detail'),

    path('battlecup/', views.BattleCupListCreate.as_view(), name='battlecup-list'),
    path('battlecup/<int:id>/', views.BattleCupRetrieveUpdateDelete.as_view(), name='battlecup-detail'),

    path('normalwins/', views.NormalWinsListCreate.as_view(), name='normalwins-list'),
    path('normalwins/<int:id>/', views.NormalWinsetrieveUpdateDelete.as_view(), name='normalwins-detail'),
    
    # Views for user and booster lookup
    path('mmrboostingjobs/user/<int:user_id>/', views.MMRBoostingJobsForUser.as_view(), name='mmrboostingjobs-for-user'),
    path('mmrboostingjobs/booster/<int:booster_id>/', views.MMRBoostingJobsForBooster.as_view(), name='mmrboostingjobs-for-booster'),

    path('coaching/user/<int:user_id>/', views.CoachingsForUser.as_view(), name='coachings-for-user'),
    path('coaching/booster/<int:booster_id>/', views.CoachingsForBooster.as_view(), name='coachings-for-booster'),

    path('behaviourscores/user/<int:user_id>/', views.BehaviousScoresForUser.as_view(), name='behaviourscores-for-user'),
    path('behaviourscores/booster/<int:booster_id>/', views.BehaviousScoresForBooster.as_view(), name='behaviourscores-for-booster'),

    path('lowpriority/user/<int:user_id>/', views.LowPrioritiesForUser.as_view(), name='lowpriorities-for-user'),
    path('lowpriority/booster/<int:booster_id>/', views.LowPrioritiesForBooster.as_view(), name='lowpriorities-for-booster'),

    path('battlecup/user/<int:user_id>/', views.BattleCupsForUser.as_view(), name='battlecups-for-user'),
    path('battlecup/booster/<int:booster_id>/', views.BattleCupsForBooster.as_view(), name='battlecups-for-booster'),

    path('normalwins/user/<int:user_id>/', views.NormalWinsForUser.as_view(), name='battlecups-for-user'),
    path('normalwins/booster/<int:booster_id>/', views.NormalWinsForBooster.as_view(), name='battlecups-for-booster'),

    path('mmrboostingjobs/pending/', views.PendingMMRBoostingJobList.as_view(), name='pending-normalwins-list'),
    path('mmrboostingjobs/inprogress/', views.InProgressMMRBoostingJobList.as_view(), name='inprogress-normalwins-list'),
    path('mmrboostingjobs/completed/', views.CompletedMMRBoostingJobList.as_view(), name='completed-normalwins-list'),
    path('mmrboostingjobs/cancelled/', views.CancelledMMRBoostingJobList.as_view(), name='cancelled-normalwins-list'),

    # Coaching URLs
    path('coaching/pending/', views.PendingCoachingList.as_view(), name='pending-coaching-list'),
    path('coaching/inprogress/', views.InProgressCoachingList.as_view(), name='inprogress-coaching-list'),
    path('coaching/completed/', views.CompletedCoachingList.as_view(), name='completed-coaching-list'),
    path('coaching/cancelled/', views.CancelledCoachingList.as_view(), name='cancelled-coaching-list'),

    # BehaviousScore URLs
    path('behaviourscores/pending/', views.PendingBehaviousScoreList.as_view(), name='pending-behaviourscore-list'),
    path('behaviourscores/inprogress/', views.InProgressBehaviousScoreList.as_view(), name='inprogress-behaviourscore-list'),
    path('behaviourscores/completed/', views.CompletedBehaviousScoreList.as_view(), name='completed-behaviourscore-list'),
    path('behaviourscores/cancelled/', views.CancelledBehaviousScoreList.as_view(), name='cancelled-behaviourscore-list'),

    # LowPriority URLs
    path('lowpriority/pending/', views.PendingLowPriorityList.as_view(), name='pending-lowpriority-list'),
    path('lowpriority/inprogress/', views.InProgressLowPriorityList.as_view(), name='inprogress-lowpriority-list'),
    path('lowpriority/completed/', views.CompletedLowPriorityList.as_view(), name='completed-lowpriority-list'),
    path('lowpriority/cancelled/', views.CancelledLowPriorityList.as_view(), name='cancelled-lowpriority-list'),

    # BattleCup URLs
    path('battlecup/pending/', views.PendingBattleCupList.as_view(), name='pending-battlecup-list'),
    path('battlecup/inprogress/', views.InProgressBattleCupList.as_view(), name='inprogress-battlecup-list'),
    path('battlecup/completed/', views.CompletedBattleCupList.as_view(), name='completed-battlecup-list'),
    path('battlecup/cancelled/', views.CancelledBattleCupList.as_view(), name='cancelled-battlecup-list'),

    path('normalwins/pending/', views.PendingNormalWinsList.as_view(), name='pending-normalwins-list'),
    path('normalwins/inprogress/', views.InProgressNormalWinsList.as_view(), name='inprogress-normalwins-list'),
    path('normalwins/completed/', views.CompletedNormalWinsList.as_view(), name='completed-normalwins-list'),
    path('normalwins/cancelled/', views.CancelledNormalWinsList.as_view(), name='cancelled-normalwins-list'),

    path('all/', views.CombinedDataView.as_view(), name='all'),


]
