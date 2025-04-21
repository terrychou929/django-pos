from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name="食材名稱")
    quantity = models.FloatField(default=0, verbose_name="庫存數量")
    unit = models.CharField(max_length=20, verbose_name="單位", default="單位")

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"

    class Meta:
        verbose_name = "食材"
        verbose_name_plural = "食材管理"

class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="品項名稱")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="價格")
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True, verbose_name="圖片")
    ingredients = models.ManyToManyField(Ingredient, through='MenuItemIngredient', verbose_name="所需食材")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "菜單項目"
        verbose_name_plural = "菜單管理"

class MenuItemIngredient(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(verbose_name="耗費數量")

    def __str__(self):
        return f"{self.menu_item.name} - {self.ingredient.name}"

    class Meta:
        verbose_name = "菜單食材關聯"
        verbose_name_plural = "菜單食材關聯"