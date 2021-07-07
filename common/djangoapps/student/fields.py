from django.db.models import CharField
from django.conf import settings
from hasher import AESCipher


class AESCharField(CharField):
    """
    AESCharField
    - Compatible with unencrypted data, the encrypted string will be carried
    """

    def __init__(self, *args, **kwargs):
        """
        init
        :param prefix: prefix
        """
        if 'prefix' in kwargs:
            self.prefix = kwargs['prefix']
            del kwargs['prefix']
        else:
            self.prefix = "aes_str:::"

        self.cipher = AESCipher(settings.AES_KEY)
        super(AESCharField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(AESCharField, self).deconstruct()

        if self.prefix != "aes_str:::":
            kwargs['prefix'] = self.prefix
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection, context):
        """
        decode
        """
        if value is None:
            return value
        if value.startswith(self.prefix):
            value = value[len(self.prefix):]
            value = self.cipher.decrypt(value)

        return value

    def to_python(self, value):
        if value is None:
            return value
        elif value.startswith(self.prefix):
            value = value[len(self.prefix):]
            value = self.cipher.decrypt(value)

        return value

    def get_prep_value(self, value):
        """
        in
        """
        if isinstance(value, str) or isinstance(value, unicode):
            value = self.cipher.encrypt(value)
            value = self.prefix + value
        elif value is not None:
            raise TypeError(str(value)+" is not a valid value for AESCharField")

        return value
