from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from forms import UserCreateForm


class LibraryBaseView (FormView):
    success_url = reverse_lazy('user_home')
    form_class = AuthenticationForm
    template_name = 'library/home.html'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LibraryBaseView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())


class AccountCreate (CreateView):
    model = User
    success_url = reverse_lazy('user_home')
    template_name = 'library/user-creation.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, new_user)

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print('Please fill out the form correctly.')

        return super(AccountCreate, self).form_invalid(form)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower()
        return email


class UserLandingView (TemplateView):
    template_name = 'library/user-landing.html'
