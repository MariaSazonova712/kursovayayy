from .models import Task, Orders
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "place", "price", "square"]
        widgets ={
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),
            "place": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Объём'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            "square": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ["created", "phone", "description"]
        widgets = {
            "created": TextInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон',
                'type': 'text'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
