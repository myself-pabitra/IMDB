from rest_framework import serializers
from watchlist.models import Show,StreamPlatform,Review

# Working with ModelSerializer
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('showlist', )
        read_only_fields = ('id',)



class ShowSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Show
        fields = '__all__'
        read_only_fields = ('id',)


class PlatformSerializer(serializers.ModelSerializer):
    showlist = ShowSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
        read_only_fields = ('id',)

     









     
       
    # def validate_title(self, value):
    #     if Movie.objects.filter(title=value).exists():
    #         raise serializers.ValidationError('Movie title already exists')
    #     return value

    # def validate(self,data):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError('Title and Description cannot be same')
    #     return data


# Working with Regular Serializer

'''
Validating titlte using validator 
'''

# def validate_title(value):
#     if Movie.objects.filter(title=value).exists():
#         raise serializers.ValidationError('Movie title already exists')

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(validators=[validate_title])
#     description = serializers.CharField()
#     category = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.category = validated_data.get('category', instance.category)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

'''
    Field level Validation methods
'''

# def validate_title(self, value):
#     if Movie.objects.filter(title=value).exists():
#         raise serializers.ValidationError('Movie title already exists')
#     return value

'''
    Object level Validation methods
'''
# def validate(self,data):
#     if data['title'] == data['description']:
#         raise serializers.ValidationError('Title and Description cannot be same')
#     return data
