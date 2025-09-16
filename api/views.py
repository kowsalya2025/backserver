from .permissions import IsTrainerOrOwnerOrReadOnly
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny  # ✅ important
from django.contrib.auth.models import User
from .models import MiniProject
from .serializers import MiniProjectSerializer

class MiniProjectViewSet(viewsets.ModelViewSet):
    queryset = MiniProject.objects.all().order_by('-created_at')
    serializer_class = MiniProjectSerializer
    permission_classes = [IsTrainerOrOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'priority']

class RegisterView(APIView):
    permission_classes = [AllowAny]  # ✅ allow anyone to register

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response(
                {"detail": "Username already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response(
            {"detail": "User created successfully"},
            status=status.HTTP_201_CREATED
        )

