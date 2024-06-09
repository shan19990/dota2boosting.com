from rest_framework import generics
from rest_framework.views import APIView
from .models import MMRBoostingJob, Coaching, BehaviousScore, LowPriority, BattleCup, NormalWins
from .serializers import MMRBoostingJobSerializer, CoachingSerializer, BehaviousScoreSerializer, LowPrioritySerializer, BattleCupSerializer,NormalWinsSerializer,CombinedDataSerializer
from rest_framework.response import Response
from rest_framework import status

class MMRBoostingJobListCreate(generics.ListCreateAPIView):
    queryset = MMRBoostingJob.objects.all()
    serializer_class = MMRBoostingJobSerializer

class MMRBoostingJobRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = MMRBoostingJob.objects.all()
    serializer_class = MMRBoostingJobSerializer
    lookup_url_kwarg = 'id'

class CoachingListCreate(generics.ListCreateAPIView):
    queryset = Coaching.objects.all()
    serializer_class = CoachingSerializer

class CoachingRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coaching.objects.all()
    serializer_class = CoachingSerializer
    lookup_url_kwarg = 'id'

class BehaviousScoreListCreate(generics.ListCreateAPIView):
    queryset = BehaviousScore.objects.all()
    serializer_class = BehaviousScoreSerializer

class BehaviousScoreRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BehaviousScore.objects.all()
    serializer_class = BehaviousScoreSerializer
    lookup_url_kwarg = 'id'

class LowPriorityListCreate(generics.ListCreateAPIView):
    queryset = LowPriority.objects.all()
    serializer_class = LowPrioritySerializer

class LowPriorityRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = LowPriority.objects.all()
    serializer_class = LowPrioritySerializer
    lookup_url_kwarg = 'id'

class BattleCupListCreate(generics.ListCreateAPIView):
    queryset = BattleCup.objects.all()
    serializer_class = BattleCupSerializer

class BattleCupRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BattleCup.objects.all()
    serializer_class = BattleCupSerializer
    lookup_url_kwarg = 'id'

class NormalWinsListCreate(generics.ListCreateAPIView):
    queryset = NormalWins.objects.all()
    serializer_class = NormalWinsSerializer

class NormalWinsetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = NormalWins.objects.all()
    serializer_class = NormalWinsSerializer
    lookup_url_kwarg = 'id'


class MMRBoostingJobsForUser(generics.ListAPIView):
    serializer_class = MMRBoostingJobSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return MMRBoostingJob.objects.filter(user_id=user_id)

class MMRBoostingJobsForBooster(generics.ListAPIView):
    serializer_class = MMRBoostingJobSerializer

    def get_queryset(self):
        booster_id = self.kwargs['booster_id']
        return MMRBoostingJob.objects.filter(booster_id=booster_id)

class CoachingsForUser(generics.ListAPIView):
    serializer_class = CoachingSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Coaching.objects.filter(user_id=user_id)

class CoachingsForBooster(generics.ListAPIView):
    serializer_class = CoachingSerializer

    def get_queryset(self):
        booster_id = self.kwargs['booster_id']
        return Coaching.objects.filter(booster_id=booster_id)

class BehaviousScoresForUser(generics.ListAPIView):
    serializer_class = BehaviousScoreSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return BehaviousScore.objects.filter(user_id=user_id)

class BehaviousScoresForBooster(generics.ListAPIView):
    serializer_class = BehaviousScoreSerializer

    def get_queryset(self):
        booster_id = self.kwargs['booster_id']
        return BehaviousScore.objects.filter(booster_id=booster_id)

class LowPrioritiesForUser(generics.ListAPIView):
    serializer_class = LowPrioritySerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return LowPriority.objects.filter(user_id=user_id)

class LowPrioritiesForBooster(generics.ListAPIView):
    serializer_class = LowPrioritySerializer

    def get_queryset(self):
        booster_id = self.kwargs['booster_id']
        return LowPriority.objects.filter(booster_id=booster_id)

class BattleCupsForUser(generics.ListAPIView):
    serializer_class = BattleCupSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return BattleCup.objects.filter(user_id=user_id)

class BattleCupsForBooster(generics.ListAPIView):
    serializer_class = BattleCupSerializer

    def get_queryset(self):
        booster_id = self.kwargs['booster_id']
        return BattleCup.objects.filter(booster_id=booster_id)

class NormalWinsForUser(generics.ListAPIView):
    serializer_class = NormalWinsSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return NormalWins.objects.filter(user_id=user_id)

class NormalWinsForBooster(generics.ListAPIView):
    serializer_class = NormalWinsSerializer

    def get_queryset(self):
        booster_id = self.kwargs['booster_id']
        return NormalWins.objects.filter(booster_id=booster_id)

class PendingMMRBoostingJobList(generics.ListAPIView):
    queryset = MMRBoostingJob.objects.filter(status='pending')
    serializer_class = MMRBoostingJobSerializer

class InProgressMMRBoostingJobList(generics.ListAPIView):
    queryset = MMRBoostingJob.objects.filter(status='inprogress')
    serializer_class = MMRBoostingJobSerializer

class CompletedMMRBoostingJobList(generics.ListAPIView):
    queryset = MMRBoostingJob.objects.filter(status='completed')
    serializer_class = MMRBoostingJobSerializer

class CancelledMMRBoostingJobList(generics.ListAPIView):
    queryset = MMRBoostingJob.objects.filter(status='cancelled')
    serializer_class = MMRBoostingJobSerializer


# Coaching views
class PendingCoachingList(generics.ListAPIView):
    queryset = Coaching.objects.filter(status='pending')
    serializer_class = CoachingSerializer

class InProgressCoachingList(generics.ListAPIView):
    queryset = Coaching.objects.filter(status='inprogress')
    serializer_class = CoachingSerializer

class CompletedCoachingList(generics.ListAPIView):
    queryset = Coaching.objects.filter(status='completed')
    serializer_class = CoachingSerializer

class CancelledCoachingList(generics.ListAPIView):
    queryset = Coaching.objects.filter(status='cancelled')
    serializer_class = CoachingSerializer


# BehaviousScore views
class PendingBehaviousScoreList(generics.ListAPIView):
    queryset = BehaviousScore.objects.filter(status='pending')
    serializer_class = BehaviousScoreSerializer

class InProgressBehaviousScoreList(generics.ListAPIView):
    queryset = BehaviousScore.objects.filter(status='inprogress')
    serializer_class = BehaviousScoreSerializer

class CompletedBehaviousScoreList(generics.ListAPIView):
    queryset = BehaviousScore.objects.filter(status='completed')
    serializer_class = BehaviousScoreSerializer

class CancelledBehaviousScoreList(generics.ListAPIView):
    queryset = BehaviousScore.objects.filter(status='cancelled')
    serializer_class = BehaviousScoreSerializer


# LowPriority views
class PendingLowPriorityList(generics.ListAPIView):
    queryset = LowPriority.objects.filter(status='pending')
    serializer_class = LowPrioritySerializer

class InProgressLowPriorityList(generics.ListAPIView):
    queryset = LowPriority.objects.filter(status='inprogress')
    serializer_class = LowPrioritySerializer

class CompletedLowPriorityList(generics.ListAPIView):
    queryset = LowPriority.objects.filter(status='completed')
    serializer_class = LowPrioritySerializer

class CancelledLowPriorityList(generics.ListAPIView):
    queryset = LowPriority.objects.filter(status='cancelled')
    serializer_class = LowPrioritySerializer


# BattleCup views
class PendingBattleCupList(generics.ListAPIView):
    queryset = BattleCup.objects.filter(status='pending')
    serializer_class = BattleCupSerializer

class InProgressBattleCupList(generics.ListAPIView):
    queryset = BattleCup.objects.filter(status='inprogress')
    serializer_class = BattleCupSerializer

class CompletedBattleCupList(generics.ListAPIView):
    queryset = BattleCup.objects.filter(status='completed')
    serializer_class = BattleCupSerializer

class CancelledBattleCupList(generics.ListAPIView):
    queryset = BattleCup.objects.filter(status='cancelled')
    serializer_class = BattleCupSerializer

# NormalWins views
class PendingNormalWinsList(generics.ListAPIView):
    queryset = NormalWins.objects.filter(status='pending')
    serializer_class = NormalWinsSerializer

class InProgressNormalWinsList(generics.ListAPIView):
    queryset = NormalWins.objects.filter(status='inprogress')
    serializer_class = NormalWinsSerializer

class CompletedNormalWinsList(generics.ListAPIView):
    queryset = NormalWins.objects.filter(status='completed')
    serializer_class = NormalWinsSerializer

class CancelledNormalWinsList(generics.ListAPIView):
    queryset = NormalWins.objects.filter(status='cancelled')
    serializer_class = NormalWinsSerializer

class CombinedDataView(APIView):
    def get(self, request, format=None):
        mmr_boosting_jobs = MMRBoostingJob.objects.all()
        coaching = Coaching.objects.all()
        behaviour_scores = BehaviousScore.objects.all()
        low_priority = LowPriority.objects.all()
        battle_cup = BattleCup.objects.all()
        normal_wins = NormalWins.objects.all()

        data = {
            'mmr_boosting_jobs': mmr_boosting_jobs,
            'coaching': coaching,
            'behaviour_scores': behaviour_scores,
            'low_priority': low_priority,
            'battle_cup': battle_cup,
            'normal_wins': normal_wins
        }

        serializer = CombinedDataSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
