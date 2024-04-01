from unittest import skip
from django.test import TestCase, RequestFactory
from unittest.mock import Mock, patch
from project_prj.models import Task
from project_prj.views import index


class GoogListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_name_list_view(self):
        Task.objects.create(title='Жёлтый', price=200)
        Task.objects.create(title='Красный', price=500)

        request = self.factory.get('/index/')

        mock_queryset = Mock(spec=Task.objects.all())
        mock_queryset.return_value = [
            Mock(title='Фото', price=100),
            Mock(title='Услуга', price=1000)
        ]

        with patch('blog.views.Goog.objects.all', mock_queryset):
            response = index(request)

        self.assertEqual(response.status_code, 300)

        self.assertContains(response, 'Жёлтый', 200)
        self.assertContains(response, 'Красный', 500)