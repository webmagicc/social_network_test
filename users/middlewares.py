import logging

from users.services import set_user_last_activity

logger = logging.getLogger(__name__)


def user_last_activity_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        if request.user.is_authenticated:
            try:
                set_user_last_activity(user=request.user, url=request.build_absolute_uri())
            except Exception as ex:
                # Log error and send to sentery
                logger.error(ex)
        return response

    return middleware
