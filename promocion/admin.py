from django.contrib import admin
import models
# Register your models here.


class PProductoAdmin(admin.ModelAdmin):
    filter_horizontal = ('producto',)
#end class


class PMarcaAdmin(admin.ModelAdmin):
    filter_horizontal = ('marcas',)
#end class


class PCategoriaAdmin(admin.ModelAdmin):
    filter_horizontal = ('categorias',)
#end class


class BProductoAdmin(admin.ModelAdmin):
    filter_horizontal = ('producto',)
#end class


class BMarcaAdmin(admin.ModelAdmin):
    filter_horizontal = ('marcas',)
#end class


class BCategoriaAdmin(admin.ModelAdmin):
    filter_horizontal = ('categorias',)
#end class


admin.site.register(models.Categoria)
admin.site.register(models.Marca)
admin.site.register(models.Producto)
admin.site.register(models.Oferta)
admin.site.register(models.Promocion)
admin.site.register(models.PProducto, PProductoAdmin)
admin.site.register(models.PMarca, PMarcaAdmin)
admin.site.register(models.PCategoria)
admin.site.register(models.Bono)
admin.site.register(models.BProducto, BProductoAdmin)
admin.site.register(models.BMarca, BMarcaAdmin)
admin.site.register(models.BCategoria, BCategoriaAdmin)
