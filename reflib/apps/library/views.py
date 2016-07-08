from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, TemplateView, CreateView, ListView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from reflib.apps.library.forms import UserCreateForm

from imagestore.models import Album


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
    success_url = reverse_lazy('user_home')
    template_name = 'library/user-creation.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        self.object = form.save()
        create_new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
        login(self.request, create_new_user)
        return HttpResponseRedirect(self.get_success_url())


class UserLandingView (ListView):
    template_name = 'library/user-landing.html'
    model = Album

    # def dispatch(self, request, *args, **kwargs):
    #     album = get_object_or_404(Album)
    #     print(album)
    #
    #     return super(UserLandingView, self).dispatch(request, *args, **kwargs)



