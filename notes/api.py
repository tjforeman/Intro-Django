from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()

def get_queryset(self):

    logged_in_user = self.request.user

    
    if user.is_anonymous:
        return PersonalNote.objects.none()
    else:
        return PersonalNote.objects.filter( )
