# MT-PY-File-upload
# Upload File to AWS S3

This script demonstrates how to upload a file to AWS S3 using the 
` boto3 ` 
library in  Python.

## Prerequisites

- Python 3.x
- AWS account with S3 access
- AWS credentials configured (via environment variables or AWS CLI)

## Setup

1. Install the required dependencies by running the following command:

```cmd
   pip install MT-PY-File-upload 
```
2. Some support-package to work with file upload package.

```cmd
pip instal boto3 python-dotenv
```

* Create a .env file in the same directory as the script and provide the necessary 
AWS credentials and region:

```note
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_S3_REGION_NAME=your-s3-region
AWS_STORAGE_BUCKET_NAME=bucket-name
```

## Usage
### Import the necessary libraries:

```py
import boto3
import os
from dotenv import load_dotenv
load_dotenv()

```

* Define the function Upload_file_to_s3 to upload a file to S3:

```py
Upload_file_to_s3(file_path, bucket_name, object_name,aws_access_key,
    aws_secret_key,region_name )

```

* Call the function with the required parameters:

```py
Upload_file_to_s3("path/to/file", "your-bucket-name", "object-key-name",
"aws_access_key","aws_secret_key","region_name")

```
## References

[boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
[python-dotenv documentation](https://github.com/theskumar/python-dotenv)

# Custom FileField with Extension Validation

This code provides custom file field classes for Django models with extension validation. 
It extends Django's built-in FileField and adds additional validation for allowed file extensions.

## Prerequisites

- Django framework

## Usage

### Mt_FileField

A custom FileField that validates the file extension based on a list of allowed extensions.

### Example usage:

```py
from django.db.models import FileField
from django.core.validators import FileExtensionValidator

class Mt_FileField(FileField):
    def __init__(self, *args, allowed_extensions=None, **kwargs):
        self.allowed_extensions = allowed_extensions or []
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)

        # Use Django's FileExtensionValidator to validate the file extension
        validator = FileExtensionValidator(allowed_extensions=self.allowed_extensions)

        # Validate the file
        try:
            validator(value)
        except ValidationError as e:
            # If the file is not valid, raise a ValidationError with a custom error message
            raise ValidationError('Invalid file format. Only {} files are allowed.'.format(
                ', '.join(self.allowed_extensions))
            ) from e
```

# Custom FileField with Extension Validation

This code provides custom file field classes for Django models 
with extension validation. It extends Django's built-in FileField
and adds additional validation for allowed file extensions.


## Usage

## Mt_FileField

A custom FileField that validates the file extension based on a list of allowed extensions.



## implement in models.py
### Example:


```py
from mt_django_file_upload.file_upload import Mt_fileUploadField,Mt_FileField
class SaveFile(models.Model):
    file1=Mt_fileUploadField(upload_to="newDoc",null=True,blank=True)
    # Yo can limit your file fields
    file2=Mt_FileField(upload_to="doc", 
    null=True,blank=True,allowed_extensions=['txt','doc','docx'])
```
## implement in views.py
### Example:

```py
def home(request,*args,**kwargs):
    if(request.method=="POST"):

        filled_form=Doc_fields(request.POST,request.FILES)
        note=''
        header = "Upload folder form"

        if(filled_form.is_valid()):
            filled_form.save()
            note=f"{filled_form.cleaned_data['text']} item was saved successfully"
        else:
            note="Somthing went wrong"
        return render(request,'local_upload/index.html',
        {"note":note,"form":
        filled_form,"header":"Save file,image using mt_django_file_upload package in mysqlite"})    
    else:
        form =Doc_fields()
        return render(request,"local_upload/index.html",{"form":form,
        "header":"Saving file,image using mt_django_file_upload package in mysqlite"})
    
def example(request):
    context={
        "hello":_("Hello")
    }
    return render(request,'local_upload/example.html',context)
```
## implement in settings.py
### Example:

```py
MEDIA_ROOT=BASE_DIR/'media'
MEDIA_URL='/media/'
```
* **You can change database by changing database configuration in settings.py**
```py
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
```py
from django.db.models import FileField
from django.core.validators import FileExtensionValidator

class Mt_FileField(FileField):
    def __init__(self, *args, allowed_extensions=None, **kwargs):
        self.allowed_extensions = allowed_extensions or []
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)

        # Use Django's FileExtensionValidator to validate the file extension
        validator = FileExtensionValidator(allowed_extensions=self.allowed_extensions)

        # Validate the file
        try:
            validator(value)
        except ValidationError as e:
            # If the file is not valid, raise a ValidationError with a custom error message
            raise ValidationError('Invalid file format. Only {} files are allowed.'.format(
                ', '.join(self.allowed_extensions))
            ) from e
```

## Mt_form_fileUploadField
A custom form file field that extends Django's built-in FileField.

### Example usage:

```py

from django.forms import FileField as f_FileField

class Mt_form_fileUploadField(f_FileField):
    pass
```
## Mt_fileUploadField
A custom file field that extends Django's built-in FileField.

### Example usage:

```py

from django.db.models import FileField

class Mt_fileUploadField(FileField):
    pass
```


## References
[Django FileField documentation](https://docs.djangoproject.com/en/4.2/ref/models/fields/#filefield)
[Django FileExtensionValidator documentation](https://docs.djangoproject.com/en/4.2/ref/validators/#fileextensionvalidator)

```note

This documentation provides an overview of the custom field classes and how to use them in 
your Django models or forms. It also includes references to the relevant Django documentation
for further details.

```