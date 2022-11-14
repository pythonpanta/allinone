from django.shortcuts import redirect, render
from .models import Stock
from .forms import ReorderLevelForm, StockCreateForm, StockSearchForm, StockUpdateForm
from django.contrib import messages
from django.http import HttpResponse
import csv
from .forms import IssueForm, ReceiveForm


def home(request):
    context = {"title": 'Home Page', }
    return render(request, "stockmgmt/home.html", context)


def list_item(request):
    title = 'List of Items'
    if request.method == 'POST':
        form = StockSearchForm(request.POST)
        queryset = Stock.objects.filter(category__id__icontains=form['category'].value(),
                                        item_name__icontains=form['item_name'].value(
        )
        )
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow(
                    [stock.category, stock.item_name, stock.quantity])

            return response

    else:
        form = StockSearchForm()
        queryset = Stock.objects.all()
    context = {"form": form, "queryset": queryset, "title": title, }
    return render(request, "stockmgmt/list_item.html", context)


def add_items(request):
    if request.method == 'POST':
        form = StockCreateForm(request.POST)
        c = request.POST['category']
        i = request.POST['item_name']
        q = request.POST['quantity']

        if c == '' or i == '' or q == '':
            messages.success(request, 'Pleasee Filled all the input fields')
            return redirect('/add_items')

        for instance in Stock.objects.all():
            if instance.category == c:
                messages.success(
                    request, f'{c} category is already in our list , Add New Catrgory 👩‍🦳👩‍🦳')
                return redirect('/add_items')

        if form.is_valid():
            form.save()
            messages.success(request, 'Data Successfully added')
        return redirect('/list_item')

    else:
        form = StockCreateForm(request.POST)

    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "stockmgmt/add_items.html", context)


def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_item')

    context = {
        'form': form,
        "title": "Update Item",
    }
    return render(request, 'stockmgmt/add_items.html', context)


def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_item')
    return render(request, 'stockmgmt/delete_items.html')


def stock_detail(request, pk):
    queryset = Stock.objects.get(id=pk)
    context = {
        "title": queryset.item_name,
        "queryset": queryset,
    }
    return render(request, "stockmgmt/stock_detail.html", context)


def issue_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = IssueForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity -= instance.issue_quantity
        instance.issue_by = str(request.user)
        messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) +
                         " " + str(instance.item_name) + "s now left in Store")
        instance.save()

        return redirect('/stock_detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": 'Issue ' + str(queryset.item_name),
        "queryset": queryset,
        "form": form,
        "username": 'Issue By: ' + str(request.user),
    }
    return render(request, "stockmgmt/add_items.html", context)


def receive_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity += instance.receive_quantity
        instance.save()
        messages.success(request, "Received SUCCESSFULLY. " +
                         str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")

        return redirect('/stock_detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": 'Reaceive ' + str(queryset.item_name),
        "instance": queryset,
        "form": form,
        "username": 'Receive By: ' + str(request.user),
    }
    return render(request, "stockmgmt/add_items.html", context)


def reorder_level(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = ReorderLevelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Reorder level for " + str(instance.item_name) +
                         " is updated to " + str(instance.reorder_level))

        return redirect("/list_item")
    context = {
        "instance": queryset,
        "form": form,
    }
    return render(request, "stockmgmt/add_items.html", context)
