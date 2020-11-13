#%%
from dataclasses import dataclass

#%%
@dataclass
class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    tip_amount: float = 0.0

bill0 = Bill(table_number=5, meal_amount=50.5, served_by="John", tip_amount=7.5)
print(f"Today's first bill: {bill0!r}")


#%%
Bill.__annotations__


#%%
@dataclass
class SpecialBill:
    table_number: int = 888
    meal_amount: float
    served_by: str
    tip_amount: float = 0.0


#%%
class OldBill:
    def __init__(self, table_number: int, meal_amount: float, served_by: str, tip_amount: float):
        self.table_number = table_number
        self.meal_amount = meal_amount
        self.served_by = served_by
        self.tip_amount = tip_amount


old_bill0 = OldBill(table_number=3, meal_amount=20.5, served_by="Dan", tip_amount=5)
old_bill1 = OldBill(table_number=3, meal_amount=20.5, served_by="Dan", tip_amount=5)
print("Comparison Between Regular Instances:", old_bill0 == old_bill1)


#%%
bill0 = Bill(table_number=5, meal_amount=50.5, served_by="John", tip_amount=7.5)
bill1 = Bill(table_number=5, meal_amount=50.5, served_by="John", tip_amount=7.5)
print("Comparison Between Data Class Instances:", bill0 == bill1)


#%%
@dataclass(order=True)
class ComparableBill:
    meal_amount: float
    tip_amount: float


#%%
bill1 = ComparableBill(meal_amount=50.5, tip_amount=7.5)
bill2 = ComparableBill(meal_amount=50.5, tip_amount=8.0)
bill3 = ComparableBill(meal_amount=60, tip_amount=10)
print("Is bill1 less than bill2?", bill1 < bill2)
print("Is bill2 less than bill3?", bill2 < bill3)

#%%
@dataclass(unsafe_hash=True)
class HashableBill:
    meal_amount: float
    tip_amount: float

hashable_bill0 = HashableBill(20, 5)

hash(hashable_bill0)

#%%
from collections import namedtuple
NamedTupleBill = namedtuple("NamedBill", "meal_amount tip_amount")

@dataclass
class DataClassBill:
    meal_amount: float
    tip_amount: float

namedtuple_bill = NamedTupleBill(20, 5)
dataclass_bill = DataClassBill(20, 5)

namedtuple_bill.tip_amount = 6
dataclass_bill.tip_amount = 6

@dataclass(frozen=True)
class ImmutableBill:
    meal_amount: float
    tip_amount: float

immutable_bill = ImmutableBill(20, 5)
immutable_bill.tip_amount = 7

#%%
@dataclass
class BaseBill:
    meal_amount: float

@dataclass
class TippedBill(BaseBill):
    tip_amount: float

tipped_bill = TippedBill(meal_amount=20, tip_amount=5)


#%%
@dataclass
class BaseBill:
    meal_amount: float = 20

@dataclass
class TippedBill(BaseBill):
    tip_amount: float

tipped_bill = TippedBill(meal_amount=20, tip_amount=5)

class IncorrectBill:
    def __init__(self, costs_by_dish=[]):
        self.costs_by_dish = costs_by_dish

bill0 = IncorrectBill()
bill1 = IncorrectBill()
bill0.costs_by_dish.append(5)
bill1.costs_by_dish.append(7)
print("Bill 0 costs:", bill0.costs_by_dish)
print("Bill 1 costs:", bill1.costs_by_dish)
bill0.costs_by_dish is bill1.costs_by_dish

@dataclass
class IncorrectBill:
    costs_by_dish: list = []

from dataclasses import field
@dataclass
class CorrectBill:
    costs_by_dish: list = field(default_factory=list)

bill0 = CorrectBill()
bill0.costs_by_dish.append(5)
bill1 = CorrectBill()
bill1.costs_by_dish.append(7)
print("Bill 0 costs:", bill0.costs_by_dish)
print("Bill 1 costs:", bill1.costs_by_dish)
bill0.costs_by_dish is bill1.costs_by_dish


