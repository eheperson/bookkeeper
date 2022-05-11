from email.policy import default
from tabnanny import verbose
from xmlrpc.client import ServerProxy
from rest_framework import serializers
from booktracker.models import(
    Author,
    Book,
    Publisher,
    Genre,
    Format

)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "name",
            "date_of_birth",
            "date_of_death"
        ]
        # exclude = []

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields=[
            "name",
            "address",
            "phone_no"
        ]

class BookSerializer(serializers.ModelSerializer):
    author= AuthorSerializer()
    publisher=PublisherSerializer()
    class Meta:
        model = Book
        fields =  [
            "title",
            "author",
            "publisher",
            "genre",
            "format",
            "page_no",
            "is_readed",
            "note",
            "published_date"
        ]

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author_model = Author.objects.create(**author_data)

        publisher_data = validated_data.pop('publisher')
        publisher_model = Publisher.objects.create(**publisher_data)

        book_item = Book.objects.create(
            author=author_model, 
            publisher=publisher_model,
            **validated_data)
        # Return a Dataitem instance
        return book_item

    def update(self, instance, validated_data):
        """
            this approach preferred because of the :
                " Lists are not currently supported in HTML input"
            bug/error in django
        """
        print(validated_data)
        print(instance.author.name)

        if "author" in validated_data:
            author_data = validated_data.get("author")
            if author_data.get("name") and instance.author.name != author_data.get("name"):
                instance.author.name = author_data.get("name")
            if author_data.get("date_of_birth") and instance.author.date_of_birth != author_data.get("date_of_birth"):
                instance.author.date_of_birth= author_data.get("date_of_birth")
            if author_data.get("date_of_death") and instance.author.date_of_death != author_data.get("date_of_death"):
                instance.author.date_of_death= author_data.get("date_of_death")

        if "publisher" in validated_data:
            publisher_data = validated_data.get("publisher")
            if publisher_data.get("name") and instance.publisher.name != publisher_data.get("name"):
                instance.publisher.name = publisher_data.get("name")
            if publisher_data.get("address") and instance.publisher.address != publisher_data.get("address"):
                instance.publisher.address= publisher_data.get("address")
            if publisher_data.get("phone") and instance.publisher.phone != publisher_data.get("phone"):
                instance.publisher.phone= publisher_data.get("phone")
        
        instance.title = validated_data.get('title') if validated_data['title'] and validated_data['title'] != instance.title else instance.title
        #
        instance.published_date = validated_data.get('published_date') if 'published_date' in validated_data and validated_data['published_date'] != instance.published_date else instance.published_date
        #
        instance.genre = validated_data.get('genre') if 'genre' in validated_data and validated_data['genre'] != instance.genre else instance.genre
        #
        instance.format = validated_data.get('format') if 'format' in validated_data and validated_data['format'] != instance.format else instance.format
        #
        instance.page_no = validated_data.get('page_no') if 'page_no' in validated_data and validated_data['page_no'] != instance.page_no else instance.page_no
        #
        instance.is_readed = validated_data.get('is_readed') if 'is_readed' in validated_data and validated_data['is_readed'] != instance.is_readed else instance.is_readed
        #
        instance.note = validated_data.get('note') if 'note' in validated_data and validated_data['note'] != instance.note else instance.note
        
        print(instance.author.name)

        instance.save()
        return instance 

# class GeneralSerializer(serializers.Serializer):
#     author_name = serializers.CharField(required=True)
#     author_date_of_birth = serializers.DateField(required=False)
#     author_date_of_death = serializers.DateField(required=False)
#     #
#     publisher_name = serializers.CharField()
#     publisher_address = serializers.CharField()
#     publisher_phone_no = serializers.CharField()
#     #
#     genre = serializers.ChoiceField(choices=Genre.choices, default=Genre.DYST)
#     format = serializers.ChoiceField(choices=Format.choices, default=Format.EBK)
#     page_no = serializers.IntegerField()
#     is_readed = serializers.BooleanField()
#     note = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
#     #
#     class Meta:
#         # exclude = []
#         fields = [
#             'publish_date',
#             'title',
#             'genre',
#             'format',
#             'page_no',
#             'is_readed',
#             'note',
#             #
#             'author_name',
#             'author_date_of_birth',
#             'author_date_of_death',
#             #
#             'publisher_name',
#             'publisher_address',
#             'publisher_phone_no',
#         ]
        
#         # exclude = ['author', 'publisher']

#     # def validate(self, data):
#     #     print(data)
#     #     #
#     #     author_name = data.pop('author_name')
#     #     author_date_of_birth = data.pop('author_date_of_birth')
#     #     author_date_of_death = data.pop('author_date_of_death')
#     #     #
#     #     publisher_name = data.pop('publisher_name')
#     #     publisher_address = data.pop('publisher_address')
#     #     publisher_phone_no = data.pop('publisher_phone_no')
#     #     #
#     #     author = Author()
#     #     author.name = author_name
#     #     author.date_of_birth = author_date_of_birth
#     #     author.date_of_death = author_date_of_death 

#     #     # author,_ = Author.objects.get_or_create(
#     #     #     name = author_name,
#     #     #     date_of_birth = author_date_of_birth,
#     #     #     date_of_death = author_date_of_death,
#     #     # )

#     #     data['author'] = author

#     #     publisher=Publisher()

#     #     publisher.name = publisher_name
#     #     publisher.address = publisher_address
#     #     publisher.phone_no = publisher_phone_no

#     #     # publisher, _ = Publisher.objects.get_or_create(
#     #     #     name = publisher_name,
#     #     #     address = publisher_address,
#     #     #     phone_no = publisher_phone_no,
#     #     # )
#     #     # data['publisher'] = publisher
#     #     #
#     #     print("-------------------------------------")
#     #     print(data)
#     #     return data

#     def create(self, validated_data):
#         print(validated_data)
#         # validated_data.pop('author_name')
#         return validated_data

#     # def to_representation(self, instance):
#     #     print(instance)
        
        
#     #     return super().to_representation(instance)

#     # # def post(self, request, *args, **kwargs):
#     # #     print(request.data)
#     # #     request.data.pop('author_name')