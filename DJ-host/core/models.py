import os
import zipfile
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.exceptions import ValidationError
import uuid
# Function to define the upload path dynamically
def user_directory_path(instance, filename):
    return f'{instance.user.username}/{filename}'


class FileUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model
    file = models.FileField(upload_to=user_directory_path)

    def save(self, *args, **kwargs):
        # Save the file first
        super().save(*args, **kwargs)

        if self.file.name.endswith('.zip'):
            try:
                # Define the directory to extract the contents
                extract_path = os.path.join(
                    settings.MEDIA_ROOT,
                    self.user.username,
                    'extracted'
                )
                os.makedirs(extract_path, exist_ok=True)

                # Extract the ZIP file
                with zipfile.ZipFile(self.file.path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)

                print(f"Extracted contents of {self.file.name} to {extract_path}")
            except zipfile.BadZipFile:
                raise ValidationError("The uploaded file is not a valid ZIP archive.")
            except Exception as e:
                raise ValidationError(f"Error while extracting ZIP file: {str(e)}")

    def __str__(self):
        return f'File uploaded by {self.user.username}: {self.file.name}'
