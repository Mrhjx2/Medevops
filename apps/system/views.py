from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.base import TemplateView

from .mixin import LoginRequiredMixin
from apps.custom import BreadcrumbMixin

# Create your views here.


# class SystemView(LoginRequiredMixin, View):
#     """
#     view system
#     """
#     def get(self, request):
#         return render(request, 'system/system_index.html')
class SystemView(LoginRequiredMixin, BreadcrumbMixin, TemplateView):
    """
    system view
    """
    template_name = 'system/system_index.html'
