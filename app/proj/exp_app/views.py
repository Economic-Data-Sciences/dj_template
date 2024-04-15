from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime
from django.views.generic import TemplateView
from typing import Any


# Create your views here.

# Class Based Views
class Index(TemplateView):
    template_name = 'index.html'

    # write a function to pass in current date and time to template
    async def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # get current date and time
        current_date_time = datetime.now()
        # pass current date and time to template
        context = {'current_date_time': current_date_time}
        # render the template
        return render(request, self.template_name, context)
