from fastapi import FastAPI
# TABLAS SIN RELACIÓN 
from routes.person import person
from routes.rol import rol


# TABLAS CON RELACIÓN 
from routes.user import user
from routes.usersrols import userrol


from routes.rutinas import rutina

from routes.ejercicios_rutinas import ejcrtn
from routes.progra_salud import progra_salud
from routes.instructors import instructor
from routes.ejercicio import ejercicio
from routes.evaluacion_serv import evaluaciones_serv_router
from routes.pedidos import pedidos
from routes.promociones import promocion_router
from routes.Pregunta import pregunta_router
from routes.opinion_cliente import opinion_cliente_router
from routes.productos import producto
from routes.membresias import membresia
from routes.miembros import miembros
from routes.transacciones import  transacciones
from routes.sucursales import sucursales
from routes.schedule import schedule
from routes.equipamiento import equipamiento
from routes.adeudos import adeudo
from routes.dietas import dieta
from routes.indicadores_nutricionales import indicador_nutricional
from routes.area import area
from routes.puestos import puesto
from routes.empleados import empleado
from routes.servicios_clientes import servicio_cliente
from routes.instalacion import instalacion
from routes.mantenimiento import mantenimiento
from routes.p_nutricional import p_nutricional
from routes.valoracion import valoracion
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# TABLAS SIN RELACIÓN 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TABLAS CON RELACIÓN 
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(rutina)
app.include_router(ejcrtn)
app.include_router(progra_salud)
app.include_router(instructor)
app.include_router(ejercicio)
app.include_router(evaluaciones_serv_router)
app.include_router(pedidos)
app.include_router(promocion_router)
app.include_router(pregunta_router)
app.include_router(opinion_cliente_router)
app.include_router(producto)
app.include_router(membresia)
app.include_router(miembros)
app.include_router(transacciones)
app.include_router(sucursales)
app.include_router(equipamiento)
app.include_router(adeudo)
app.include_router(dieta)
app.include_router(indicador_nutricional)
app.include_router(schedule)
app.include_router(area)
app.include_router(puesto)
app.include_router(empleado)
app.include_router(servicio_cliente)
app.include_router(instalacion)
app.include_router(mantenimiento)
app.include_router(p_nutricional)
app.include_router(valoracion)