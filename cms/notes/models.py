from django.db import models
from django.utils import timezone

class Note(models.Model):
    """
    Model for individual notes.
    """
    title = models.CharField(max_length=100, null=True, blank=True)
    author_account_id = models.IntegerField(null=True, blank=True)
    google_doc_id = models.CharField(max_length=100, null=True, blank=True)
    creation_time = models.DateTimeField(default=timezone.now)
    template = models.CharField(max_length=20, default='default', choices=(
        ('default', 'Empty Note'),
        ('cornell', 'Cornell Style'),
        ('matrix', 'Matrix'),
    ))

    @property
    def google_doc_url(self):
        return 'https://docs.google.com/document/d/'+str(self.google_doc_id)+'/edit' if self.google_doc_id else None

    def __str__(self):
        """
        Returns a human-readable string for the instance.
        """
        return self.title + " by " + str(self.author_account_id)