from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Concert, Ticket
from .forms import BookingForm


def concert_list(request):
    concerts = Concert.objects.all().order_by('id')
    return render(request, 'tickets/concert_list.html', {'concerts': concerts})


def concert_detail(request, concert_id):
    concert = get_object_or_404(Concert, id=concert_id)
    return render(request, 'tickets/concert_detail.html', {'concert': concert})


def concert_detail(request, concert_id):
    concert = get_object_or_404(Concert, id=concert_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            customer_full_name = '{} {}'.format(
                form.cleaned_data['first_name'], form.cleaned_data['last_name'])
            existing_ticket = Ticket.objects.filter(
                concert=concert, customer_full_name=customer_full_name).exists()
            if not existing_ticket:
                Ticket.objects.create(
                    concert=concert,
                    customer_full_name=customer_full_name,
                    payment_method=form.cleaned_data['payment_method'],
                    is_active=True
                )
                messages.success(request, '註冊成功！')
                return redirect(reverse('concert_detail', kwargs={'concert_id': concert_id}))
            else:
                return redirect('{}?registered=True'.format(reverse('concert_list')))

    else:
        form = BookingForm()

    return render(request, 'tickets/concert_detail.html', {
        'concert': concert,
        'form': form
    })
