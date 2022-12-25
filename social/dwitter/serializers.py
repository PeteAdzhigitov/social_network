from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Profile, Dweet, User




class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =['user','image','follows']


class DweetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    # body = serializers.CharField(max_length=255)
    # created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Dweet
        # read_only_fields  = ['user']
        fields = "__all__"
        # query_set = User.objects.filter(pk=self.request.user.id)

    #
    # def save(self, **kwargs):
    #     """Include default for read_only `user` field"""
    #     kwargs["user"] = self.fields["user"].get_default()
        # return super(DweetSerializer,self).save(**kwargs)

    # def validate_user(self):
    #     return self.context['request'].user
    #
    # def create(self, validated_data):
    # #     # validated_data['user'] = self.context['request'].user.username
    # #     # validated_data['user'] = self.fields['user'].get_default()
    #     return Dweet.objects.create(user = validated_data.get("user"), body = validated_data.get("body"), created_at =validated_data.get("created_at") )
    #
    # #     # user = self.context["user"]
    # #     # request = self.context.get("request")
    # #     # user = request.user
    # def update(self, instance, validated_data):
    #     instance.user = validated_data.get("user", instance.user)
    #     instance.body = validated_data.get("body", instance.body)
    #     instance.created_at = validated_data.get("created_at", instance.created_at)
    #     instance.save()
    #     return instance


    #
    #
    #     new_dweet = Dweet.objects.create(**validated_data)
    #     new_dweet["user"] = self.validated_data["user"]
    #     return new_dweet
        # new_dweet.user = self.fields['user'].get_default()
        # print(new_dweet.user)
        # new_dweet.user = validated_data.get("user")
        # new_dweet.user = validated_data.get("user")





    # def save(self, **kwargs):
    #     """Include default for read_only `user` field"""
        # kwargs["user"] = self.fields["user"].get_default()
        # return super().save(**kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)





