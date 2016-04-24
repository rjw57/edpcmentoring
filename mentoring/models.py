from django.db import models
from django.contrib.auth.models import User

class RelationshipManager(models.Manager):
    def active(self):
        """A query-set of active relationships."""
        return self.filter(is_active=True)

    def inactive(self):
        """A query-set of inactive relationships."""
        return self.filter(is_active=False)

class Relationship(models.Model):
    """
    Records a mentorship relation.

    """
    mentor = models.ForeignKey(
        User, related_name='mentor_relationships',
        on_delete=models.CASCADE)
    mentee = models.ForeignKey(
        User, related_name='mentee_relationships',
        on_delete=models.CASCADE)

    started_on = models.DateField()
    ended_on = models.DateField(blank=True, null=True)
    ended_by = models.ForeignKey(
        User, related_name='mentor_relationships_ended',
        blank=True, null=True)

    is_active = models.BooleanField(default=True)

    objects = RelationshipManager()

    def __str__(self):
        return '{} mentoring {}'.format(self.mentor, self.mentee)

