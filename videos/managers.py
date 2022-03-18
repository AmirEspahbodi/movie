import magic

from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat
from django.core.exceptions import ValidationError



def FileValidator(data):
    error_messages = {
     'max_size': ("Ensure this file size is not greater than %(max_size)s."
                  " Your file size is %(size)s."),
     'min_size': ("Ensure this file size is not less than %(min_size)s. "
                  "Your file size is %(size)s."),
     'content_type': "Files of type %(content_type)s are not supported.",
    }

    max_size = None 
    content_types = ['mp4', 'mkv', 'matroska', 'ogg', 'mov', 'quicktime', 'wmv', 'webm']
    min_size = None

    if max_size is not None and data.size > max_size:
        params = {
            'max_size': filesizeformat(max_size), 
            'size': filesizeformat(data.size),
        }
        raise ValidationError(error_messages['max_size'],
                                'max_size', params)

    if min_size is not None and data.size < min_size:
        params = {
            'min_size': filesizeformat(min_size),
            'size': filesizeformat(data.size)
        }
        raise ValidationError(error_messages['min_size'], 
                                'min_size', params)

    if content_types:
        magic.Magic(mime=True, uncompress=True)
        fie_content_type = magic.from_buffer(data.read(), mime=True)
        fie_content_type = fie_content_type.lower()
        
        data.seek(0)
        its_movie = False
        for i in content_types:
            if i in fie_content_type:
                its_movie = True
                break
        if not its_movie:
            params = { 'content_type': fie_content_type }
            raise ValidationError(error_messages['content_type'],
                                'content_type', params)
