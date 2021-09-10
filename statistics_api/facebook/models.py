from django.db import models
from django.db.models.aggregates import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import date, timedelta

class Post(models.Model):
    user_id = models.CharField(max_length=255)
    post_id = models.CharField(max_length=255, primary_key=True)
    likes = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class PostHistory(models.Model):
    user_id = models.CharField(max_length=255, db_index=True)
    post_id = models.CharField(max_length=255)
    likes = models.IntegerField()
    created_at = models.DateField()
    
    @staticmethod
    def get_average_of_likes_from_past_thirty_days(queryset):
        return queryset.values("user_id", "created_at").order_by("created_at").annotate(average_likes=Avg("likes"))

    @receiver(post_save, sender=Post)
    def save_history(sender, instance, *args, **kwargs):
        history_query = PostHistory.objects.filter(
            user_id=instance.user_id,
            post_id=instance.post_id,
            created_at=instance.updated_at
        )

        if history_query.count() == 0:
            history = PostHistory()
        else:
            history = history_query.first()

        history.user_id=instance.user_id
        history.post_id=instance.post_id
        history.likes=instance.likes
        history.created_at=instance.updated_at
        history.save()
