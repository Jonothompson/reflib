from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from reflib.apps.users.models import User


class LibraryBaseView (FormView):
    success_url = reverse_lazy('user_home')
    form_class = AuthenticationForm
    # redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'library/home.html'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LibraryBaseView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # self.object = form.save(commit=False)
        # self.object.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class AccountCreate (CreateView):
    model = User


class UserLandingView (TemplateView):
    template_name = 'library/user-landing.html'
