"""
URLs for user API
"""

from django.conf import settings
from django.conf.urls import url

from .views import UserCourseEnrollmentsList, UserCourseStatus, UserDetail, UserDeactivateLogoutView

urlpatterns = [
    url('^' + settings.USERNAME_PATTERN + '$', UserDetail.as_view(), name='user-detail'),
    url(
        '^' + settings.USERNAME_PATTERN + '/course_enrollments/$',
        UserCourseEnrollmentsList.as_view(),
        name='courseenrollment-detail'
    ),
    url('^{}/course_status_info/{}'.format(settings.USERNAME_PATTERN, settings.COURSE_ID_PATTERN),
        UserCourseStatus.as_view(),
        name='user-course-status'),
    url(
        '^' + settings.USERNAME_PATTERN + '/deactivate_logout/$',
        UserDeactivateLogoutView.as_view(),
        name='user-deactivate-logout'
    ),    
]
