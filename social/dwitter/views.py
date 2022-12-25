import os

from django.shortcuts import render,redirect, get_object_or_404, reverse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.test import APIClient
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Profile, Dweet, User
from .forms import DweetForm, DweetUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProfileUpdateForm, UserUpdateForm
from rest_framework import generics, request, permissions, viewsets, mixins
from .serializers import ProfilesSerializer, DweetSerializer





#
# class DweetListAPIView(generics.ListCreateAPIView):
#     serializer_class = DweetSerializer
#     queryset = Dweet.objects.all()
#
# class DweetViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     # queryset = Dweet.objects.all()
#     serializer_class = DweetSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Dweet.objects.all()[:3]
#         else:
#             return Dweet.objects.filter(pk=pk)



    # @action(methods=["get"], detail=True)
    # def specific_dweet(self, request, pk=None):
    #
    #     dweet = Dweet.objects.get(pk=pk)
    #     return Response({"dweet": [dweet.id , dweet.body,dweet.created_at]})

    # def post(self,request,*args,**kwargs):
    #     # user = User.objects.get(pk=self.request.user.id)
    #     # data = request.data.copy()
    #     # data["user"] = request.user.id
    #     # data = {"body": request.data.get("body"), "user": self.co}
    #     # User.objects.filter(pk=14)
    #     posted_data = DweetSerializer(data=request.data)
    #     # posted_data.initial_data['user'] = self.request.user.id
    #     posted_data.is_valid(raise_exception=True)
    #         # posted_data.validated_data['user'] = request.user
    #         # posted_data.validated_data["user"] = request.user.id
    #         # posted_data.validated_data
    #     posted_data.save(user=self.request.user)
    #     return Response({'new_dweet':posted_data.data})

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user


#
class DweetUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DweetSerializer
    queryset = Dweet.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    # def get_object(self):
    #     pk= self.kwargs.get("pk")
    #     return Dweet.objects.get(pk)

    # def get_queryset(self):
    #     pk= self.kwargs.get("pk")
    #     return Dweet.objects.filter(pk=pk)

    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     if not pk:
    #         return Response({"eror":"Method is not allowed"})
    #
    #     try:
    #         instance = Dweet.objects.get(pk=pk)
    #     except:
    #         return Response({"error":"There is no such object"})
    #
    #     serializer = DweetSerializer(data=request.data, instance=instance)
    #     serializer.is_valid()
    #     serializer.save()
    #     return Response({"dweet": serializer.data})

# class DweetAPIView(generics.ListAPIView):


    # client = APIClient()
    # client.login(username='Petyan22', password='Testing321')
    # user = User.objects.get(username='Petyan22')
    # client = APIClient()
    # client.force_authenticate(user=user)
    # queryset = Dweet.objects.all()
    # serializer_class = DweetSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     # current_user = self.request.user
    #     dweets = Dweet.objects.filter(user=self.request.user.id)
    #     return dweets


    # def get_queryset(self):
    #     user = User.objects.filter(pk=self.request.user.id)
    #     return user
    # def get_object(self):
    #     user = User.objects.filter(pk=self.request.user.id)
    #     return user
    # user = User.objects.get(pk=request.user.id)
    # def get(self, request):
    # # #     # dweets = Dweet.objects.filter(user=self.request.user.id)
    #     dweets = Dweet.objects.filter(user=self.request.user.id)
    #     return Response({'dweets': DweetSerializer(dweets,many=True).data})
    #
    # def post(self,request,*args,**kwargs):
    #     # user = User.objects.get(pk=self.request.user.id)
    #     # data = request.data.copy()
    #     # data["user"] = request.user.id
    #     # data = {"body": request.data.get("body"), "user": self.co}
    #     # User.objects.filter(pk=14)
    #     posted_data = DweetSerializer(data=request.data)
    #     # posted_data.initial_data['user'] = self.request.user.id
    #     posted_data.is_valid(raise_exception=True)
    #         # posted_data.validated_data['user'] = request.user
    #         # posted_data.validated_data["user"] = request.user.id
    #         # posted_data.validated_data
    #     posted_data.save(user=self.request.user)
    #     return Response({'new_dweet':posted_data.data})
    #
    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     if not pk:
    #         return Response({"eror":"Method is not allowed"})
    #
    #     try:
    #         instance = Dweet.objects.get(pk=pk)
    #     except:
    #         return Response({"error":"There is no such object"})
    #
    #     serializer = DweetSerializer(data=request.data, instance=instance)
    #     serializer.is_valid()
    #     serializer.save()
    #     return Response({"dweet": serializer.data})

class ProfilesAPIList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilesSerializer


class DashboardList(LoginRequiredMixin, ListView):

    template_name = 'dwitter/dashboard.html'
    context_object_name = 'dweets'

    def get_queryset(self):
        # upgraded_current_user_followers = User.objects.
        current_user_followers = self.request.user.profile.follows.all()
        # return Dweet.objects.filter(user__profile__in=current_user_followers).select_related('dweet').order_by('-created_at')
        return Dweet.objects.select_related('user').filter(user__profile__in=current_user_followers).order_by('-created_at')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DashboardList, self).get_context_data(**kwargs)
        context['form'] = DweetForm()
        return context

    def post(self, request, *args, **kwargs):
        form = DweetForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                dweet = form.save(commit=False)
                dweet.user = request.user
                dweet.save()
                return redirect('dwitter:dashboard')
        return render(request, 'dwitter/dashboard.html', {'form': form})


class ProfileListView(ListView):
    model = Profile
    # profiles = Profile.objects.exclude(user=request.user)
    # context = {'profiles':profiles}
    # return render(request,'dwitter/profile_list.html',context)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.exclude(user=self.request.user).select_related('user')
        return context

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile

    # queryset = Profile.objects.select_related()
    # pk_url_kwarg = 'pk'
    template_name = 'dwitter/profile.html'

    # def get_object(self, queryset=None):
    #     pk_ = self.kwargs.get('pk')
    #     return get_object_or_404(Profile, pk=pk_)
    # def get_queryset(self):
    #     pk_ = self.kwargs.get('pk')
    #     return Profile.objects.filter(pk=pk_)

    def get_context_data(self,**kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        # context['current_user'] = User.objects.get(pk=self.request.user.id)
        context['profile_user'] = Profile.objects.prefetch_related('followed_by').get(id=self.object.user.id)
        context['dweetss'] = Dweet.objects.select_related().filter(user=self.object.user.id)
        return context


    # def get_context_data(self, **kwargs):
    #     context = super(ProfileDetailView, self).get_context_data(**kwargs)
    #     context['user_form'] = UserUpdateForm()
    #     context['profile_form'] = ProfileUpdateForm()
    #     return context

    # def get(self, request, *args, **kwargs):
    #     user_form = self.user_update_form
    #     profile_form = self.profile_update_form
    #     return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            # user_update_form = UserUpdateForm(post_data, instance=self.request.user)
            # profile_update_form = ProfileUpdateForm(post_data, instance=self.request.user )
            current_user_profile = Profile.objects.select_related('user').get(user=request.user.id)
            data = request.POST
            action = data.get("follow")
            if action == "follow":
                current_user_profile.follows.add(self.kwargs.get('pk'))
            elif action == "unfollow":
                current_user_profile.follows.remove(self.kwargs.get('pk'))
            # if user_update_form.is_valid() and profile_update_form.is_valid():
                # current_user_profile_name = user_update_form.cleaned_data['username']
                # user_update_form.save()
                # profile_update_form.save()
                # return render(request, 'dwitter/profile.html', {'profile': Profile.objects.get(pk=self.kwargs.get('pk'))})
            current_user_profile.save()
            # return redirect('dwitter/profile/')
        return render(request, 'dwitter/profile.html', {'profile_user': Profile.objects.get(pk=self.kwargs.get('pk'))})

class ProfileUpdateView( UserPassesTestMixin, LoginRequiredMixin, UpdateView):

    model = Profile
    form_class = UserUpdateForm
    # fields = ['username','email']

    template_name = 'dwitter/profile_update.html'

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False

    # def get_queryset(self):
    #     return Profile.objects.select_related('user').all()

    # def get_object(self, queryset=None):
    #     pk_ = self.kwargs.get('pk')
    #     # return get_object_or_404(Profile, pk= pk_)
    #     return Profile.objects.select_related('user').get(pk=pk_)

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        current_user = self.request.user
        context['profile'] = Profile.objects.select_related('user').get(pk=current_user.id)
        context['user_form'] = UserUpdateForm(instance=current_user)
        context['profile_form'] = ProfileUpdateForm(instance=current_user.profile)
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            current_user = self.request.user
            user_update_form = UserUpdateForm(request.POST, instance=current_user)
            profile_update_form = ProfileUpdateForm(request.POST,request.FILES, instance=current_user.profile)
            if profile_update_form.is_valid() and user_update_form.is_valid():
                user_update_form.save()
                profile_update_form.save()
                # return render(request, 'dwitter/profile_update.html',
                #               {'user_form': user_update_form,
                #                'profile_form': profile_update_form})
                return redirect('/profile_update/%d' %current_user.id)

            return redirect('/profile_update/%d' %current_user.id)

        # return render(request,'dwitter/profile_update.html', {'profile_update_form': profile_update_form})

class DweetDeleteView( UserPassesTestMixin, DeleteView):

    model = Dweet
    template_name = "dwitter/dweet_delete.html"
    success_url = '/'

    def test_func(self):
        dweet = self.get_object()
        if self.request.user == dweet.user:
            return True
        return False

class DweetUpdateView( UserPassesTestMixin, UpdateView):

    model = Dweet
    template_name = "dwitter/dweet_update.html"
    form_class = DweetUpdateForm

    success_url = '/'

    def test_func(self):
        dweet = self.get_object()
        if self.request.user == dweet.user:
            return True
        return False







# def profile(request, pk):
#     if not hasattr(request.user,'profile'):
#         missing_attr = Profile(user=request.user)
#         missing_attr.save
#     profile = Profile.objects.get(pk=pk)


