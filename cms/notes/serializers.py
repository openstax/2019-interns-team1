from django.utils import timezone
from rest_framework import serializers

from .models import Note
from .functions import GoogleDocument


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note

        # Fields to provide to API endpoint
        fields = ('id', 'title', 'author_account_id', 'google_doc_id', 'google_doc_url', 'creation_time',)

        # Arguments for the fields, used to declare whether these are read or write only
        extra_kwargs = {
            'creation_time': {'read_only': True}, 
            'google_doc_id': {'read_only': True},
            
            # For form creation purposes:
            'notetemplate': {'write_only': True}
        }

    def create(self, validated_data):
        """
        Overwrites .create() method so that we can verify input and set datetime to current localtime of the server.
        """

        google_doc = GoogleDocument()
        
        if not google_doc.authenticate():
            raise RuntimeError("Google Doc authentication failed. Please refer to the logs.")

        title = validated_data.get('title', None)

        progress, created = Note.objects.update_or_create(
            title = title,
            creation_time = timezone.localtime(),
            author_account_id = validated_data.get('author_account_id', None),
            google_doc_id = google_doc.create(title = title)
        )

        return progress