from rest_framework import viewsets, filters
from .models import MiniProject
from .serializers import MiniProjectSerializer
from .permissions import IsTrainerOrOwnerOrReadOnly

class MiniProjectViewSet(viewsets.ModelViewSet):
    queryset = MiniProject.objects.all().order_by('-created_at')
    serializer_class = MiniProjectSerializer
    permission_classes = [IsTrainerOrOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'priority']

