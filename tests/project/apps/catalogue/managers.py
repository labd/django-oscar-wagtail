from oscar.apps.catalogue import managers as _managers


class ProductQuerySet(_managers.ProductQuerySet):

    def available_in_cms(self):
        return self


class ProductManager(_managers.ProductManager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
