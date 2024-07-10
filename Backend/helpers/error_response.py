from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


def error_response(error_message , status):
    response = Response({"error":error_message}, status=status)
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context = {}
    return response  

    