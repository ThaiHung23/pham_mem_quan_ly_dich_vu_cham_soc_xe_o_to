# models/__init__.py
from .user import UserModel
from .customer import CustomerModel
from .vehicle import VehicleModel
from .service import ServiceModel
from .appointment import AppointmentModel
from .invoice import InvoiceModel

__all__ = [
    'UserModel', 'CustomerModel', 'VehicleModel',
    'ServiceModel', 'AppointmentModel', 'InvoiceModel'
]