from django.utils import timezone
from rest_framework import serializers

from .models import Note
from .functions import GoogleDocument


class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, required=False)
    author_account_id = serializers.IntegerField(required=False)
    creation_time = serializers.DateTimeField(default=timezone.now, read_only=True)
    last_open_time = serializers.DateTimeField(read_only=True)
    template = serializers.ChoiceField(default='default', choices=(
        ('default', 'Empty Note'),
        ('cornell', 'Cornell Style'),
        ('matrix', 'Matrix'),
    ))
    google_doc_id = serializers.CharField(max_length=100, read_only=True)
    google_doc_url = serializers.CharField(max_length=100, read_only=True)
    content = serializers.JSONField(write_only=True, required=False)
    tags = serializers.ChoiceField(default=None, required=False, allow_null=True, choices=(
        ('calculus', 'Calculus'),
        ('algebra', 'Algebra'),
        ('statistics', 'Statistics'),
        ('economics', 'Economics'),
        ('astronomy', 'Astronomy'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('biology', 'Biology'),
        ('comp', 'Computer Science'),
    ))
    star = serializers.BooleanField(default=False, required=False)
    do_update_lastopen = serializers.BooleanField(write_only=True, default=False)

    def update(self, instance, validated_data):
        """
        Overwrites .update() method so that we can verify the input, set document as starred and update
        the last opened date/time.
        """

        if validated_data.get('do_update_lastopen', False):
            instance.last_open_time = timezone.now()
       
        instance.star = validated_data.get('star', instance.star)
        instance.save()

        return instance

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
            google_doc_id = google_doc.create(title=title, template=template, content=content),
            tags = validated_data.get('tags', None),
        )

        return progress