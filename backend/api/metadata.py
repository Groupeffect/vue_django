from rest_framework.metadata import SimpleMetadata
from rest_framework.utils.field_mapping import ClassLookupDict
from rest_framework import serializers

class ApiMetaData(SimpleMetadata):

    label_lookup = ClassLookupDict({
        serializers.Field: 'field',
        serializers.BooleanField: 'radio',
        serializers.NullBooleanField: 'boolean',
        serializers.CharField: 'text',
        serializers.UUIDField: 'id',
        serializers.URLField: 'url',
        serializers.EmailField: 'email',
        serializers.RegexField: 'regex',
        serializers.SlugField: 'slug',
        serializers.IntegerField: 'number',
        serializers.FloatField: 'number',
        serializers.DecimalField: 'number',
        serializers.DateField: 'date',
        serializers.DateTimeField: 'date',
        serializers.TimeField: 'time',
        serializers.ChoiceField: 'choice',
        serializers.MultipleChoiceField: 'multiple choice',
        serializers.FileField: 'file upload',
        serializers.ImageField: 'image upload',
        serializers.ListField: 'list',
        serializers.DictField: 'nested object',
        serializers.Serializer: 'nested object',
    })