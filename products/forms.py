from django import forms
from products.models import Product

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
    # def save(request):
    #     img = Image_product(nome = request.POST['nome'], image = request.FILE['image'])
    #     img.save()

    #     prd = Product(titulo =, descricao = , preco = )
    #     prd.save()

    #     for im in img.all:
    #         prd.image.add(im)
    #         prd.save()