from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class TaggedItemManager(models.Manager):
    def ger_tags_for(self,obj_type,obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)

        queryset = TaggedItem.objects \
            .select_related('tag') \
            .filter(
                content_type=content_type,
                object_id = obj_id
            )


class Tag(models.Model):
    lavel = models.CharField(max_length=255)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()