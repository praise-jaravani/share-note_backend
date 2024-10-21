from django.db import models

# Django comes with a native user model that includes fields like username, password, email, first_name, last_name, and methods for managing user authentication and permissions.
# Here, we've just imported that model to be used further in additional models.

from django.contrib.auth.models import User

# Create your models here.

# The Profile model uses a OneToOneField to the User model, which extends the User model with additional fields like bio and profile_picture.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# The Note model uses a ForeignKey to the User model, which associates each note with its owner (the user who created it).
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='notes/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class NoteTag(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.note.title} - {self.tag.name}"

class NoteSubject(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.note.title} - {self.subject.name}"
