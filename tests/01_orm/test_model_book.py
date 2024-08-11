import pytest
from django.db import models

from catalog.models import BookInstance


def test_ORM_150_book_model_structure_table_exists():
    try:
        from catalog.models import BookInstance  # noqa F401
    except ImportError:
        assert False
    else:
        assert True
 