from .production import *


if FEATURES.get('ENABLE_MEMBERSHIP_INTEGRATION', False):
    INSTALLED_APPS.append('membership')
    REST_FRAMEWORK.update({'EXCEPTION_HANDLER': 'membership.utils.customer_exception_handler'})

############## Settings for python-social-auth ######################
SOCIAL_AUTH_TRAILING_SLASH = ENV_TOKENS.get('SOCIAL_AUTH_TRAILING_SLASH', False)

# Aliyun oss
ALIYUN_OSS = AUTH_TOKENS.get('ALIYUN_OSS', {})

OSS_ACCESS_KEY_ID = ALIYUN_OSS.get("OSS_ACCESS_KEY_ID", "")
OSS_ACCESS_KEY_SECRET = ALIYUN_OSS.get("OSS_ACCESS_KEY_SECRET", "")
OSS_ENDPOINT = ALIYUN_OSS.get("OSS_ENDPOINT", "")
OSS_BUCKET_NAME = ALIYUN_OSS.get("OSS_BUCKET_NAME", "")

#for SMS
SMS_API = AUTH_TOKENS.get('SMS_API','')
SMS_API_BY_LINKGROUP = AUTH_TOKENS.get('SMS_API_BY_LINKGROUP','')
SMS_API_URL = ENV_TOKENS.get('SMS_API_URL','')
SMS_API_URL_BY_LINKGROUP = ENV_TOKENS.get('SMS_API_URL_BY_LINKGROUP','')

######################## Professors ###########################

if FEATURES.get('ENABLE_PROFESSORS'):
    INSTALLED_APPS.append('professors')

############################ WEIXINAPPID_AND_WEIXINAPPSECRET #########################
WEIXINAPPID = ''
WEIXINAPPSECRET = ''
WEIXINAPPID = ENV_TOKENS.get('WEIXINAPPID', WEIXINAPPID)
WEIXINAPPSECRET = ENV_TOKENS.get('WEIXINAPPSECRET', WEIXINAPPSECRET)
