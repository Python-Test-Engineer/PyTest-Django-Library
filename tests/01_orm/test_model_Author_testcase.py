from django.test import TestCase

# Create your tests here.

from catalog.models import Author, Book


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Author.objects.create(first_name="Big", last_name="Bob")

    @classmethod
    def tearDownData(cls):
        """Tear down non-modified objects used by all test methods."""
        pass

    def test_ORM_140_Author_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_ORM_141_Author_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_ORM_142_Author_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("date_of_birth").verbose_name
        self.assertEqual(field_label, "date of birth")

    def test_ORM_143_Author_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("date_of_death").verbose_name
        self.assertEqual(field_label, "died")

    def test_ORM_144_Author_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 100)

    def test_ORM_145_Author_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("last_name").max_length
        self.assertEqual(max_length, 100)

    def test_ORM_145_Author_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = "{0}, {1}".format(author.last_name, author.first_name)

        self.assertEqual(str(author), expected_object_name)

    def test_ORM_146_Author_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), "/catalog/author/1")
