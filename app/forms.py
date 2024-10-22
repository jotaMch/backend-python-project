from django.forms import ModelForm
from app.models import Pratos

# Create the form class.
class PratosForm(ModelForm):
    class Meta:
        model = Pratos
        fields = ["prato", "preco", "porcao"]
