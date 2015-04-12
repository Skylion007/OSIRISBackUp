import pickle
import base64
import os
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')
    def filename(self):
        return os.path.basename(self.docfile.name)
    def fileloc(self):
        return os.path.dirname(self.docfile.name)

