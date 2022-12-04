from django.http import request
from django.shortcuts import render
from pizza_store.forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza


def home(request):
    return render(request, 'pizza_store/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = "Thank You for Ordering. Your Hot %s %s and %s is on its Way!" % (
                filled_form.cleaned_data['size'],
                filled_form.cleaned_data['swallow'],
                filled_form.cleaned_data['soup'],)
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = 'Pizza Order Has Failed. Try Again!'
        return render(request, 'pizza_store/order.html',
                      {'created_pizza_pk': created_pizza_pk, 'pizzaform': filled_form, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza_store/order.html', {'pizzaform': form, 'multiple_form': multiple_form})


def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number_of_plates']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['swallow'])
            note = "Your Order is Successful!"
        else:
            note = "Order Not Successful, Please Try Again!"
        return render(request, 'pizza_store/pizzas.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza_store/pizzas.html', {'formset': formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = "Your Order has Been Updated"
            return render(request, 'pizza_store/edit_order.html', {'note': note, 'pizza': pizza})

    return render(request, 'pizza_store/edit_order.html', {'pizzaform': form, 'pizza': pizza})
