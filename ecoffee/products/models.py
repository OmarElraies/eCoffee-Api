from djongo import models


MACHINE_TYPE = [
    ('CM00', 'small machine,'),
    ('CM10', 'large machine,'),
    ('EM00', 'espresso machine,')
]

MACHINE_MODEL_TYPE = [
    ('1', 'base model'),
    ('2', 'premium model'),
    ('3', 'deluxe model')
]


POD_TYPE = [
    ('CP0', 'small coffee pod'),
    ('CP1', 'large coffee pod'),
    ('EP0', 'espresso pod')
]


FLAVORS = [
    ('0', 'vanilla'),
    ('1', 'caramel'),
    ('2', 'psl'),
    ('3', 'mocha'),
    ('4', 'hazelnut'),
]

PACKS = [
    ('1', '1 dozen'),
    ('3', '3 dozen'),
    ('5', '5 dozen'),
    ('7', '7 dozen')
]


class CoffeeMachine(models.Model):
    product_type = models.CharField(
        max_length=4,
        choices=MACHINE_TYPE,
    )
    model_type = models.CharField(
        max_length=1,
        choices=MACHINE_MODEL_TYPE,
    )
    water_line_compatible = models.BooleanField()

    @property
    def product_code(self):
         return "%s%s" % ( self.product_type, self.model_type )

    @property
    def product_label(self):
        return "%s%s" % (self.get_product_type_display(), 
                        self.get_model_type_display())
    def __str__(self):
        return "%s - %s" % ( self.product_code, self.product_label)
 

class CoffeePod(models.Model):
    product_type = models.CharField(
        max_length=3,
        choices=POD_TYPE,
    )
    flavor_type = models.CharField(
        max_length=1,
        choices=FLAVORS,
    )
    pack_size = models.CharField(
        max_length=1,
        choices=PACKS,
    )

    @property
    def product_code(self):
         return "%s%s%s" % ( self.product_type, self.flavor_type , self.pack_size)


    @property
    def product_label(self):
        return "%s, %s, %s" % (self.get_product_type_display(),
                                    self.get_pack_size_display(), 
                                    self.get_flavor_type_display())

    def __str__(self):
        return "%s - %s" % ( self.product_code,self.product_label)
 




