from django.shortcuts import render
from .models import Tarifa
from .models import Vehiculo

# Create your views here.
def index(request):
    return render(request, 'index.html')

def consultarTarifa(request):
    return render(request, 'consultar_tarifa.html')

def verTarifa(request):
    print(request.POST)

    try:
        vehiculo = Vehiculo.objects.filter(marca=request.POST['marca']).get(modelo=request.POST['modelo'])
        tarifa = Tarifa.objects.get(id=vehiculo.tarifa_id_id)
        print(vehiculo)
        print(tarifa)
        return render(request, 'ver_tarifa.html', {'tarifa':tarifa, 'vehiculo':vehiculo})
    except:
        return render(request, 'consultar_tarifa.html', {'error': 'No se encontró ninguna tarifa para ese vehiculo. Puede ver la lista completa de tarifas en el apartado "Ver tarifas", sino puede comunicarse con nosotros #333 444555'})
    
def verTodasTarifas(request):
    vehiculos = Vehiculo.objects.all()
    conjunto = []
    
    for v in vehiculos:
        tarifa = Tarifa.objects.get(id=v.tarifa_id_id)
        conjunto.append({'marca':v.marca, 'modelo':v.modelo, 'frecuencia':tarifa.frecuencia, 'categoria':tarifa.categoria, 'precio': tarifa.precio})
    
    return render(request, 'todas_las_tarifas.html', {'vehiculos':conjunto})
