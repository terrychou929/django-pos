# Generated by Django 4.2.7 on 2025-04-21 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='食材名稱')),
                ('quantity', models.FloatField(default=0, verbose_name='庫存數量')),
                ('unit', models.CharField(default='單位', max_length=20, verbose_name='單位')),
            ],
            options={
                'verbose_name': '食材',
                'verbose_name_plural': '食材管理',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='品項名稱')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='價格')),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu_images/', verbose_name='圖片')),
            ],
            options={
                'verbose_name': '菜單項目',
                'verbose_name_plural': '菜單管理',
            },
        ),
        migrations.CreateModel(
            name='MenuItemIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(verbose_name='耗費數量')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.ingredient')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem')),
            ],
            options={
                'verbose_name': '菜單食材關聯',
                'verbose_name_plural': '菜單食材關聯',
            },
        ),
        migrations.AddField(
            model_name='menuitem',
            name='ingredients',
            field=models.ManyToManyField(through='menu.MenuItemIngredient', to='menu.ingredient', verbose_name='所需食材'),
        ),
    ]
