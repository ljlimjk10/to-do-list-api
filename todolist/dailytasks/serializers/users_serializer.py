from rest_framework import serializers
from dailytasks.models import User
from dailytasks.models import Tasks

class UserSerializer(serializers.ModelSerializer):
    
    tasks = serializers.PrimaryKeyRelatedField(many=True,queryset=Tasks.objects.all())

    class Meta:
        model = User
        fields = ['id','username','email','password','tasks']
        extra_kwargs = {
            'password': {
                'write_only': True,
                }
           }
        
    

    def create(self,validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )

        return user
    
