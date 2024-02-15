
class PricingCalculator:
    @staticmethod
    def calculate_total_price(pricing, total_distance):
        base_distance = pricing.base_distance_in_km
        km_price = pricing.km_price
        fix_price = pricing.fix_price

        if total_distance <= base_distance:
            total_price = fix_price
        else:
            total_price = fix_price + (total_distance - base_distance) * km_price

        return total_price
