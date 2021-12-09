from datetime import datetime

from django.http import JsonResponse, HttpResponse
from rest_framework import generics, status

from helper_services.redis_request_cache import write_request_to_redis


class PerfAPIView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        duration = request.data.get("duration")
        callback_url = request.data.get("callback_url")
        request.data["start_time"] = datetime.utcnow()
        if duration is None or callback_url is None:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        write_request_to_redis(request)
        return JsonResponse({"result": "success", "message": "request will be operated"}, safe=False,
                            status=status.HTTP_200_OK)
