from rest_framework import serializers
from booktracker.models import(
    Author,
    Book,
    Publisher,
)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields= "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    
    class Meta:
        model = Book
        fields =  "__all__"
    
    def validate(self, data):
        author = data.pop("author", None)
        author_first_name = author.get("fist_name", None)
        author_middle_name = author.get("middle_name", None)
        author_last_name = author.get("last_name", None)
        author_birth = author.get("date_of_birth", None)
        author_death = author.get("date_of_death", None)
        #
        author,_ = Author.objects.get_or_create(
            author_first_name = author_first_name,
            author_middle_name = author_middle_name,
            author_last_name = author_last_name,
            date_of_birth = author_birth,
            date_of_death = author_death,
        )
        #
        data['author'] = author

        publisher = data.pop("publisher", None)
        publisher_name = publisher.get("name", None)
        publisher_navme = publisher.get("namessssdd", None)
        print(publisher_navme)
        publisher_address = publisher.get("address", None)
        publisher_phone = publisher.get("phone_no", None)
        #
        publisher, _ = Publisher.objects.get_or_create(
            name = publisher_name,
            address = publisher_address,
            phone_no = publisher_phone,
        )
        #
        data['publisher'] = publisher
        return data


class BookSerializerExperimental(serializers.ModelSerializer):
    """
        this serializer is experimental
    """
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
