from rest_framework import serializers
from dailytasks.models import Tasks


class TasksSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Tasks
        fields = ['id','created','title','description','status','user']
        





    