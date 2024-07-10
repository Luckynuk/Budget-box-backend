from rest_framework import status
import datetime
from .models import User
from Backend.helpers import error_response


class CustomLoginRequiredMixin():

    def dispatch(self,request,*args, **kwargs):
        if "Authorization" not in request.headers:
            return error_response("please set Auth-Token.", status.HTTP_401_UNAUTHORIZED)
        
        token = request.headers["Authorization"]
        now = datetime.datetime.now()
        login_user = User.object.filter(token=token, token_expires__gt=now)
        if len(login_user) == 0:
            return error_response('the token is invalid or expired.', status.HTTP_401_UNAUTHORIZED)
        
        request.login_user = login_user[0]
        return super().dispatch(request, *args, **kwargs )