from .models import Tasks
from .serializers.tasks_serializer import TasksSerializer
from .serializers.users_serializer import UserSerializer
from rest_framework import mixins
from rest_framework import generics
from django.http import HttpResponse
from .models import User
from .permissions import UpdateUserTasks
from .permissions import DeleteUserProfile
from rest_framework import permissions


# Create your views here.

def home(request):
    return HttpResponse("A simple to do list")

def user_profile(request):
    return HttpResponse("Welcome back!")

class TasksOverview(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    


class TasksDetails(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
        
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [permissions.IsAuthenticated,
                          UpdateUserTasks]
    # permission_classes = UpdateProfileAndTasks

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class UserList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class UserDetails(mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,
                          DeleteUserProfile,]


    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
        
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)



