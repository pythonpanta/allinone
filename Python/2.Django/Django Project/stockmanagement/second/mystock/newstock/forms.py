from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')

        # for instance in Stock.objects.all():
        #     if instance.category == category:
        #         raise forms.ValidationError(
        #             str(category) + ' is already created')
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        return item_name

    def clean_quantity(self):
        item_name = self.cleaned_data.get('quantity')
        if not item_name:
            raise forms.ValidationError('This field is required')
        return item_name


class StockSearchForm(forms.ModelForm):
    # export_to_CSV = forms.BooleanField()

    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'export_to_CSV']


# for updating the data
class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['issue_quantity', 'issue_to']


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity', 'receive_by']


class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level']
