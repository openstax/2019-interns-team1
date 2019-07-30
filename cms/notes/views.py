from rest_framework import viewsets, mixins
from .serializers import NoteSerializer
from .models import Note

# REST Permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EntriesView(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
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
        title = self.request.query_params.get('title', None)
        star = self.request.query_params.get('star', None)
        tags = self.request.query_params.get('tags', None)

        if account is not None:
            queryset = queryset.filter(author_account_id=account)

        if title is not None:
            queryset = queryset.filter(title__contains=title)
        
        if star is not None:
            if star == True or star == False:
                queryset = queryset.filter(star=star)

        if tags is not None and tags != "":
            tags = tags.split(",")

            if tags[-1] == "":
                tags.pop(-1)
            
            queryset = queryset.filter(tags__in = tags)

        return queryset