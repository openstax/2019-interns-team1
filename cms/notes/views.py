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
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `account` query parameter in the URL.
        """
        queryset = Note.objects.all().order_by('-id')
        account = self.request.query_params.get('account', None)

        if account is not None:
            queryset = queryset.filter(author_account_id=account)
        
        return queryset