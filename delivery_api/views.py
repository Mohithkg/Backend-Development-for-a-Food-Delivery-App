# views.py
from django.shortcuts import render
from .models import Pricing
from .services import PricingCalculator

def calculate_price(request):
    if request.method == 'POST':
        zone = request.POST.get('zone')
        organization_id = request.POST.get('organization_id')
        total_distance = int(request.POST.get('total_distance'))
        item_type = request.POST.get('item_type')
        base_distance_in_km = int(request.POST.get('base_distance_in_km'))
        km_price = float(request.POST.get('km_price'))
        fix_price = float(request.POST.get('fix_price'))

        # Create a temporary Pricing object to pass to the PricingCalculator
        pricing = Pricing(
            organization_id=organization_id,
            item_id=None,  # Assuming item_id is not provided through the form
            zone=zone,
            base_distance_in_km=base_distance_in_km,
            km_price=km_price,
            fix_price=fix_price
        )

        total_price = PricingCalculator.calculate_total_price(pricing, total_distance)
        return render(request, 'calculate_price.html', {'total_price': total_price})

    return render(request, 'calculate_price.html')
