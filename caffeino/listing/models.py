from mongoengine import Document, StringField, BooleanField


class Pod(Document):
    COFFEE_POD_LARGE = 'COFFEE_POD_LARGE' 
    COFFEE_POD_SMALL = 'COFFEE_POD_SMALL'
    ESPRESSO_POD = 'ESPRESSO_POD'

    TYPE = (COFFEE_POD_LARGE, COFFEE_POD_SMALL, ESPRESSO_POD)

    COFFEE_FLAVOR_VANILLA = 'COFFEE_FLAVOR_VANILLA'
    COFFEE_FLAVOR_CARAMEL = 'COFFEE_FLAVOR_CARAMEL'
    COFFEE_FLAVOR_PSL = 'COFFEE_FLAVOR_PSL'
    COFFEE_FLAVOR_MOCHA = 'COFFEE_FLAVOR_MOCHA'
    COFFEE_FLAVOR_HAZELNUT = 'COFFEE_FLAVOR_HAZELNUT'

    FLAVOR = (COFFEE_FLAVOR_VANILLA, COFFEE_FLAVOR_CARAMEL, COFFEE_FLAVOR_PSL,
     COFFEE_FLAVOR_MOCHA, COFFEE_FLAVOR_HAZELNUT)

    ONE_DOZEN = '12'
    THREE_DOZEN = '36'
    FIVE_DOZEN = '60'
    SEVEN_DOZEN = '84'

    SIZE = (ONE_DOZEN, THREE_DOZEN, FIVE_DOZEN, SEVEN_DOZEN)

    sku = StringField(max_length=5)
    product_type = StringField(max_length=20, choices=TYPE)
    coffee_flavor = StringField(max_length=25, choices=FLAVOR)
    pack_size = StringField(max_length=2, choices=SIZE)

    meta = {'collection': 'pods'}


class Machine(Document):
    COFFEE_MACHINE_LARGE = 'COFFEE_MACHINE_LARGE' 
    COFFEE_MACHINE_SMALL = 'COFFEE_MACHINE_SMALL'
    ESPRESSO_MACHINE = 'ESPRESSO_MACHINE'

    TYPE = (COFFEE_MACHINE_LARGE, COFFEE_MACHINE_SMALL, ESPRESSO_MACHINE)

    sku = StringField(max_length=5)
    product_type = StringField(max_length=20, choices=TYPE)
    water_line_compatible = BooleanField()

    meta = {'collection': 'machines'}
