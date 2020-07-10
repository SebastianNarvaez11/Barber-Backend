from django.db import models
from modules.base.softdelete import SoftDeletionManager
from modules.base.utils import get_guid

class Base(models.Model):
    id = models.CharField(primary_key=True, blank=True, max_length=40, verbose_name="ID")
    deleted = models.BooleanField(default=False)
    owner = models.ForeignKey('users.User', related_name="+", blank=True, null=True, verbose_name='Propietario', on_delete=models.CASCADE)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)
    
    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, update_fields=None, using=None, request=None):
        is_new = False

        if not self.id:
            is_new = True
            self.id = get_guid()

        if not self.owner and request:
            self.owner = request.user


        super(Base, self).save(force_insert, force_update, using, update_fields)
    
    def delete(self, request=None):
        self.deleted = True
        self.save(request=request)