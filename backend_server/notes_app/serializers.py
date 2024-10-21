from rest_framework import serializers
from django.contrib.auth.models import User
from notes_app.models import Profile, Subject, Tag, Note, NoteTag, NoteSubject

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(user=user, bio=validated_data.pop('bio'), profile_picture=validated_data.pop('profile_picture', None))
        return profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()

        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        password = user_data.get('password')
        if password:
            user.set_password(password)
        user.save()

        return instance

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'profile_picture')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class NoteSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'file', 'owner')

class NoteTagSerializer(serializers.ModelSerializer):
    note = NoteSerializer()
    tag = TagSerializer()

    class Meta:
        model = NoteTag
        fields = ('id', 'note', 'tag')

class NoteSubjectSerializer(serializers.ModelSerializer):
    note = NoteSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = NoteSubject
        fields = ('id', 'note', 'subject')
