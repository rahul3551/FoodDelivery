from strategies.discount import FestivalDiscount, PremiumDiscount, NoDiscount


class DiscountFactory:
    @staticmethod
    def create(discount_type):
        if discount_type == "festival":
            return FestivalDiscount()
        elif discount_type == "premium":
            return PremiumDiscount()
        else:
            return NoDiscount()  # No discount for unknown customer types