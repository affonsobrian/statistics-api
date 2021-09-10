from django.http import Http404
from django.db.models.signals import post_save

class CreateOrUpdateIfExistsMixin:
    def create(self, request, *args, **kwargs):
        kwarg_field: str = self.lookup_url_kwarg or self.lookup_field
        self.kwargs[kwarg_field] = request.data.get(self.update_data_pk_field, None)
        try:
            instance = self.update(request, *args, **kwargs)
            post_save.send(type(instance), instance=instance, created=True)
            return instance
        except Http404:
            return super().create(request, *args, **kwargs)
