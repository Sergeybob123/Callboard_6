from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView

from .models import BaseRegisterForm
from mmonews.models import User





class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/confirm/'


class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self,  request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'sign/invalid_code.html')
            return redirect('/')