from dataclasses import dataclass, field
from typing import List
from strenum import StrEnum


@dataclass
class Balance:
    type: str
    balance: float
    referral: float
    hold: float
    
@dataclass
class MoneyData:
    RUB: float = None
    UAH: float = None
    USD: float = None
    EUR: float = None
    
@dataclass
class Method:
    name: str
    min: MoneyData
    max: MoneyData
    commission_percent: float
    def __post_init__(self):
        self.min = MoneyData(**self.min)
        self.max = MoneyData(**self.max)
        
@dataclass
class PaymentMethodResponse:
    type: str
    list: List[Method] = field(default_factory=List[Method])
    def __post_init__(self):
        self.list = [Method(**self.list[x]) for x in self.list.keys()]
    def get_method(self, method_name: str) -> 'PaymentMethodResponse':
        for method in self.list:
            if method.name == method_name:
                return method
        return None
    
@dataclass
class Rate:
    type: str
    USD: float
    UAH: float
    USDT: float
    BTC: float
    
class Lang(StrEnum):
    RU = "ru"
    EN = "en"

class Currency(StrEnum):
    RUB = "RUB"    
    

class PaymentWebhook:
    merchant_id: str
    invoice_id: str
    order_id: str
    amount: float
    currency: Currency
    profit: float
    commission: float
    commission_client: float
    commission_type: str
    sign: str
    method: str
    desc: str
    email: str
    us_key: str