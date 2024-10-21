from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from notes_app.models import Profile, Subject, Tag, Note, NoteTag, NoteSubject
from notes_app.serializers import ProfileSerializer, SubjectSerializer, TagSerializer, NoteSerializer, NoteTagSerializer, NoteSubjectSerializer
from django.contrib.auth.models import User
from notes_app.serializers import UserSerializer

from django.core.files.storage import default_storage

# The following api methods handle CRUD operations for the models

@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse(user_serializer.errors, safe=False)
    
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        try:
            user = User.objects.get(id=user_data['id'])
        except User.DoesNotExist:
            return JsonResponse("User Not Found", safe=False)
        
        user_serializer = UserSerializer(user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse(user_serializer.errors, safe=False)
    
    elif request.method == 'DELETE':
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def profileApi(request, id=0):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        profile_serializer = ProfileSerializer(profiles, many=True)
        return JsonResponse(profile_serializer.data, safe=False)

    elif request.method == 'POST':
        profile_data = JSONParser().parse(request)
        profile_serializer = ProfileSerializer(data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        profile_data = JSONParser().parse(request)
        profile = Profile.objects.get(id=profile_data['id'])
        profile_serializer = ProfileSerializer(profile, data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method == 'DELETE':
        profile = Profile.objects.get(id=id)
        profile.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def subjectApi(request, id=0):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        subject_serializer = SubjectSerializer(subjects, many=True)
        return JsonResponse(subject_serializer.data, safe=False)

    elif request.method == 'POST':
        subject_data = JSONParser().parse(request)
        subject_serializer = SubjectSerializer(data=subject_data)
        if subject_serializer.is_valid():
            subject_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        subject_data = JSONParser().parse(request)
        subject = Subject.objects.get(id=subject_data['id'])
        subject_serializer = SubjectSerializer(subject, data=subject_data)
        if subject_serializer.is_valid():
            subject_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        subject = Subject.objects.get(id=id)
        subject.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def tagApi(request, id=0):
    if request.method == 'GET':
        tags = Tag.objects.all()
        tag_serializer = TagSerializer(tags, many=True)
        return JsonResponse(tag_serializer.data, safe=False)

    elif request.method == 'POST':
        tag_data = JSONParser().parse(request)
        tag_serializer = TagSerializer(data=tag_data)
        if tag_serializer.is_valid():
            tag_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        tag_data = JSONParser().parse(request)
        tag = Tag.objects.get(id=tag_data['id'])
        tag_serializer = TagSerializer(tag, data=tag_data)
        if tag_serializer.is_valid():
            tag_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        tag = Tag.objects.get(id=id)
        tag.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def noteApi(request, id=0):
    if request.method == 'GET':
        notes = Note.objects.all()
        note_serializer = NoteSerializer(notes, many=True)
        return JsonResponse(note_serializer.data, safe=False)

    elif request.method == 'POST':
        note_data = JSONParser().parse(request)
        note_serializer = NoteSerializer(data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        note_data = JSONParser().parse(request)
        note = Note.objects.get(id=note_data['id'])
        note_serializer = NoteSerializer(note, data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        note = Note.objects.get(id=id)
        note.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def noteTagApi(request, id=0):
    if request.method == 'GET':
        note_tags = NoteTag.objects.all()
        note_tag_serializer = NoteTagSerializer(note_tags, many=True)
        return JsonResponse(note_tag_serializer.data, safe=False)

    elif request.method == 'POST':
        note_tag_data = JSONParser().parse(request)
        note_tag_serializer = NoteTagSerializer(data=note_tag_data)
        if note_tag_serializer.is_valid():
            note_tag_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        note_tag_data = JSONParser().parse(request)
        note_tag = NoteTag.objects.get(id=note_tag_data['id'])
        note_tag_serializer = NoteTagSerializer(note_tag, data=note_tag_data)
        if note_tag_serializer.is_valid():
            note_tag_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        note_tag = NoteTag.objects.get(id=id)
        note_tag.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def noteSubjectApi(request, id=0):
    if request.method == 'GET':
        note_subjects = NoteSubject.objects.all()
        note_subject_serializer = NoteSubjectSerializer(note_subjects, many=True)
        return JsonResponse(note_subject_serializer.data, safe=False)

    elif request.method == 'POST':
        note_subject_data = JSONParser().parse(request)
        note_subject_serializer = NoteSubjectSerializer(data=note_subject_data)
        if note_subject_serializer.is_valid():
            note_subject_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        note_subject_data = JSONParser().parse(request)
        note_subject = NoteSubject.objects.get(id=note_subject_data['id'])
        note_subject_serializer = NoteSubjectSerializer(note_subject, data=note_subject_data)
        if note_subject_serializer.is_valid():
            note_subject_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        note_subject = NoteSubject.objects.get(id=id)
        note_subject.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def saveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)