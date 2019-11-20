from ..models import Household, Person, Discount, DuesPlan
import factory

from faker import Faker
fake = Faker()

class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    given_name = factory.Faker('first_name')
    family_name = factory.Faker('last_name')
    email = factory.Faker('safe_email')
    member_since = factory.Faker('past_date', start_date="-10y")
    address_street1 = factory.Faker('street_address')
    address_city = factory.Faker('city')
    address_state = 'MN'
    address_zip = factory.Faker('zipcode')

    phone_number = "+18885558888" # TODO: Get Faker to generate US phone numbers
    phone_can_receive_sms = False

    emergency_contact_name = factory.Faker('name')
    emergency_contact_phone = "+18885558888"  # TODO: Get Faker to generate US phone numbers

    keyfob_code = factory.Faker('msisdn')
