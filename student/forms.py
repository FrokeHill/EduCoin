from django import forms
from home.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'phone', 'phone2', 'profil_pic']

        widgets = {
            'email': forms.TextInput(attrs= {
                'class': (
                    'w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-xl '
                    'text-gray-900 placeholder-gray-400 shadow-inner '
                    'focus:ring-4 focus:ring-blue-200 focus:border-blue-500 '
                    'transition-all duration-200 ease-in-out'
                ),
                'placeholder': 'Email manzilingiz',
            }),
            'phone': forms.TextInput(attrs= {
                'class': (
                    'w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-xl '
                    'text-gray-900 placeholder-gray-400 shadow-inner '
                    'focus:ring-4 focus:ring-blue-200 focus:border-blue-500 '
                    'transition-all duration-200 ease-in-out'
                ),
                'placeholder': 'Telefon raqamingiz',
            }),
            'phone2': forms.TextInput(attrs= {
                'class': (
                    'w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-xl '
                    'text-gray-900 placeholder-gray-400 shadow-inner '
                    'focus:ring-4 focus:ring-blue-200 focus:border-blue-500 '
                    'transition-all duration-200 ease-in-out'
                ),
                'placeholder': 'Qo\'shimcha telefon raqamingiz',
            }),
            'profil_pic': forms.ClearableFileInput(attrs={
                'class': (
                    'block w-full text-sm text-gray-900 border border-gray-300 '
                    'rounded-xl cursor-pointer bg-gray-50 '
                    'focus:outline-none file:mr-4 file:py-2 file:px-4 '
                    'file:rounded-lg file:border-0 file:text-sm file:font-semibold '
                    'file:bg-blue-600 file:text-white hover:file:bg-blue-700 '
                    'transition-all duration-200 ease-in-out'
                ),
            }),
        }
