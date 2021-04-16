import uuid
from django.db import models
from django.conf import settings


def make_upload_path(instance=None, filename=None):
    """
    Create unique name for image or file
    Add to model property image_folder_name and images of this model
    will be uploaded to this folder in media
    """
    image_folder_name = getattr(instance, 'image_folder_name', 'images')
    new_name = uuid.uuid4().hex
    file_extension = filename.split('.')[-1]
    filename = f'{new_name}.{file_extension}'
    return u"%s/%s" % (image_folder_name, filename)


class CreatedUpdatedModel(models.Model):
    """
    Absrtact model
    Add to standart models date of
    crete and update
    """
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date')

    class Meta:
        abstract = True

