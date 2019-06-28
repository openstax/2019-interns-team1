from rest_framework import viewsets, mixins
from .serializers import NoteSerializer
from .models import Note

# REST Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EntriesView(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    
    # Initializing the serializer
    serializer_class = NoteSerializer

    # Setting the permission
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Setting the queryset
    queryset = Note.objects.all().order_by('-id')