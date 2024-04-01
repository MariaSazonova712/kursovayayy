from unittest import skip
from django.test import TransactionTestCase
from project_prj.models import Task


class WidgetTransactionTestCase(TransactionTestCase):
    def test_widget_creation(self):
        Task.objects.create(name='Фотостудия')
        Task.objects.create(name='Фото')
        self.assertEqual(Task.objects.count(), 2)
