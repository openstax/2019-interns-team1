from rest_framework import serializers
from .models import Note

from django.utils import timezone

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note

        # Fields to provide to API endpoint
        fields = ('id', 'title', 'author_account_id', 'google_doc_id', 'creation_time',)

        # Arguments for the fields, used to declare whether these are read or write only
        extra_kwargs = {'creation_time': {'read_only': True}, 'google_doc_id': {'read_only': True}}

    def create(self, validated_data):
        """
        Overwrites .create() method so that we can verify input and set datetime to current localtime of the server.
        """
        progress, created = Note.objects.update_or_create(
            title = validated_data.get('title', None),
            creation_time = timezone.localtime(),
            author_account_id = validated_data.get('author_account_id', None),
            google_doc_id = validated_data.get('google_doc_id', None)
        )

        return progress