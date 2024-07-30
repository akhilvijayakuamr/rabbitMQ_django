from django.http import JsonResponse
from django.views import View
from .rpc_client import RpcClinent



class sendNumber(View):
    def get(self, request, *args, **kwargs):
        n1 = int(request.GET.get('number1', 0))
        n2 = int(request.GET.get('number2', 0))
        client = RpcClinent()
        response = client.call(n1, n2)
        return JsonResponse({'response':response})