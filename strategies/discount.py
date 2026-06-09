
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return 0  # No discount applied

class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.2  # 20% discount 

class FestivalDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.1  # 10% discount during festivals
    
