from django.utils import timezone
from rest_framework import serializers

from .models import Note
from .functions import GoogleDocument


class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    author_account_id = serializers.IntegerField()
    creation_time = serializers.DateTimeField(default=timezone.now, read_only=True)
    template = serializers.ChoiceField(default='default', choices=(
        ('default', 'Empty Note'),
        ('cornell', 'Cornell Style'),
        ('matrix', 'Matrix'),
    ))
    google_doc_id = serializers.CharField(max_length=100, read_only=True)
    google_doc_url = serializers.CharField(max_length=100, read_only=True)
    content = serializers.JSONField(write_only=True)

    def create(self, validated_data):
        """
        Overwrites .create() method so that we can verify input and set datetime to current localtime of the server.
        """

        google_doc = GoogleDocument()
        
        if not google_doc.authenticate():
            raise RuntimeError("Google Doc authentication failed. Please refer to the logs.")

        title = validated_data.get('title', None)
        template = validated_data.get('template', None)
        content = validated_data.get('content', None)

        progress, created = Note.objects.update_or_create(
            title = title,
            template = template,
            creation_time = timezone.localtime(),
            author_account_id = validated_data.get('author_account_id', None),
            google_doc_id = google_doc.create(title=title, template=template, content=content)
        )

        return progress