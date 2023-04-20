from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from generic_relations.serializers import GenericModelSerializer

from .models import Image, File, Link, Submission


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file',)


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('link',)


class SubmissionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    hackathon = serializers.PrimaryKeyRelatedField(read_only=True)
    content_type = serializers.ChoiceField(choices=[('image', 'Image'), ('file', 'File'), ('link', 'Link')])

    class Meta:
        model = Submission
        fields = ('user', 'hackathon', 'name', 'summary', 'content_type', 'content_object')

    def create(self, validated_data):
        content_type = validated_data.pop('content_type')
        content_object_data = self.context.get('content_object_data', {})

        if content_type == 'image':
            serializer = ImageSerializer(data=content_object_data)
        elif content_type == 'file':
            serializer = FileSerializer(data=content_object_data)
        elif content_type == 'link':
            serializer = LinkSerializer(data=content_object_data)
        else:
            raise serializers.ValidationError("Invalid Content Type")

        serializer.is_valid(raise_exception=True)
        content_object = serializer.save()

        submission = Submission.objects.create(content_type=ContentType.objects.get_for_model(content_object),
                                               object_id=content_object.pk, content_object=content_object,
                                               **validated_data)

        return submission
