from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from app.api.routes.tables import router as routers_tables
from app.api.routes.queries import router as routers_queries

app = FastAPI()

templates = Jinja2Templates(directory="src/templates")



app.include_router(routers_queries,prefix="/api/v1")
app.include_router(routers_tables,prefix="/api/v1")











# query_execute = ''
# is_loading = False
# inserted_count = 0

# @app.get("/main",response_class=HT)
# async def read_main(req:Request):
#   return templates.TemplateResponse("index.html",{"request": req})


# def get_query_execute():
#   global query_execute, is_loading,inserted_count
#   query_execute = ''
#   is_loading = True
#   inserted_count = 0
#   db_instance = None
#   cursor = None
#   try:
#     db_instance = get_db()
#     cursor = db_instance.cursor()
#     create_tables_query = """
#       create table clientes(
#         cve_clientes int identity(1,1) primary key,
#         cve_municipios int,
#         nombre varchar(50),
#         paterno varchar(50),
#         materno varchar(50),
#         fecha_nacimiento date
#       );
#       create table detalle_vuelos(
#         cve_detalle_vuelos int identity(1,1) primary key,
#         cve_vuelos int,
#         fecha_hora_salida datetime,
#         capacidad int,
#       );
#       create table ocupaciones(
#         cve_ocupaciones int identity(1,1) primary key,
#         cve_detalle_vuelos int,
#         cve_clientes int,
#       );
#       create table municipios(
#         cve_municipios int primary key,
#         cve_estados int,
#         nombre varchar(50)
#       );
#       create table estados(
#         cve_estados int primary key,
#         nombre varchar(50),
#         abreviatura varchar(50)
#       );
#       alter table clientes
#       add constraint fk_clientes_municipios
#       foreign key(cve_municipios) references municipios(cve_municipios);
      
#       alter table detalle_vuelos
#       add constraint fk_detalle_vuelo
#       foreign key(cve_vuelos) references vuelos(cve_vuelos);

#       alter table ocupaciones
#       add constraint fk_ocupacion_detalle_vuelo
#       foreign key(cve_detalle_vuelos) references detalle_vuelos(cve_detalle_vuelos);

#       alter table municipios
#       add constraint fk_municipio_estado
#       foreign key(cve_estados) references estados(cve_estados)
#       """
#     cursor.execute(create_tables_query)
#     db_instance.commit()
#     print("Tables created successfully.")
    
#     get_estados_query = " SELECT cve_estado,nombre,abreviatura FROM datos.dbo.estados"
#     estados= cursor.execute(get_estados_query).fetchall()
#     if not estados:
#       print("No states found in the database.")
#       return
#     cursor.executemany("""
#       INSERT INTO estados (cve_estados, nombre, abreviatura)
#       VALUES (?, ?, ?)
#     """, [(e.cve_estado, e.nombre, e.abreviatura) for e in estados])
#     db_instance.commit()

#     get_municipios_query = "SELECT cve_municipios, nombre, cve_estados FROM datos.dbo.municipios"
#     municipios = cursor.execute(get_municipios_query).fetchall()
#     if not municipios:
#       print("No municipalities found in the database.")
#       return
#     cursor.executemany("""
#       INSERT INTO municipios (cve_municipios, nombre, cve_estados)
#       VALUES (?, ?, ?)
#     """, [(m.cve_municipios, m.nombre, m.cve_estados) for m in municipios])
#     db_instance.commit()
    
#     print("Municipalities created successfully.")
    
#     nombres = [n.nombre for n in cursor.execute("SELECT nombre FROM datos.dbo.nombres").fetchall()]
#     apellidos = [a.apellido for a in cursor.execute("SELECT apellido FROM datos.dbo.apellidos").fetchall()]
#     municipios_ids = [m.cve_municipios for m in municipios]
#     clientes_data = []
#     hoy = datetime.date.today()
#     age_min = 5
#     age_max = 90
#     year_max = hoy.year - age_min   
#     year_min = hoy.year - age_max 
#     for _ in range(100_000):
#       nombre = random.choice(nombres)
#       paterno = random.choice(apellidos)
#       materno = random.choice(apellidos)
#       anio = random.randint(year_min, year_max)
#       mes = random.randint(1, 12)
#       dia = random.randint(1, 28)
#       fecha = datetime.date(anio, mes, dia)
#       municipio_id = random.choice(municipios_ids)
#       clientes_data.append((municipio_id, nombre, paterno, materno, fecha))
#       if len(clientes_data) >= 1000:
#         cursor.executemany("""
#             INSERT INTO clientes (cve_municipios, nombre, paterno, materno, fecha_nacimiento)
#             VALUES (?, ?, ?, ?, ?)
#         """, clientes_data)
#         db_instance.commit()
#         clientes_data.clear()
#       # Insertar últimos clientes si quedan
#     if clientes_data:
#       cursor.executemany("""
#           INSERT INTO clientes (cve_municipios, nombre, paterno, materno, fecha_nacimiento)
#           VALUES (?, ?, ?, ?, ?)
#       """, clientes_data)
#       db_instance.commit()
#     print("Customers created successfully.")
  
#     get_flight_query = """ 
#       SELECT  
#         v.cve_vuelos AS cve_vuelos,
#         ao.nombre AS aeropuerto_origen,
#         ad.nombre AS aeropuerto_destino,
#         co.nombre AS ciudad_origen,
#         po.nombre AS pais_origen,
#         cd.nombre AS ciudad_destino,
#         pd.nombre AS pais_destino
#         FROM vuelos v
#         INNER JOIN aeropuertos ao ON ao.cve_aeropuertos = v.cve_aeropuertos__origen
#         INNER JOIN aeropuertos ad ON ad.cve_aeropuertos = v.cve_aeropuertos__destino
#         INNER JOIN ciudades co ON co.cve_ciudades = ao.cve_ciudades
#         INNER JOIN paises po ON po.cve_paises = co.cve_paises
#         INNER JOIN ciudades cd ON cd.cve_ciudades = ad.cve_ciudades
#         INNER JOIN paises pd ON pd.cve_paises = cd.cve_paises
#         WHERE po.nombre = 'México' or pd.nombre = 'México' 
#     """
#     total_flight = cursor.execute(get_flight_query).fetchall()
#     if not total_flight:
#       print("No flights found in the database.")
#       return
    
#     arrar_flight = [x.cve_vuelos for x in total_flight]
#     detalles_vuelos_data = []
#     for _ in range(2000):
#       vuelo_id = random.choice(arrar_flight)
#       fecha = datetime.datetime(2023, random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), 0, 0)
#       detalles_vuelos_data.append((vuelo_id, fecha, 500))
#     cursor.executemany("""
#       INSERT INTO detalle_vuelos (cve_vuelos, fecha_hora_salida, capacidad)
#       VALUES (?, ?, ?)
#     """, detalles_vuelos_data)
#     db_instance.commit()
#     print("Flight details created successfully.")

#     clientes = [c[0] for c in cursor.execute("SELECT cve_clientes FROM clientes").fetchall()]
#     vuelos = cursor.execute("SELECT cve_detalle_vuelos, capacidad FROM detalle_vuelos").fetchall()
#     vuelos_disponibles = {
#       vuelo[0]: {
#         "capacidad": vuelo[1],
#         "ocupados": 0 
#       } for vuelo in vuelos
#     }
#     ocupaciones_data = []
#     data_added = 0
#     data_total = 1_000_000
#     while data_added < data_total:
#       # Seleccionar aleatoriamente un vuelo y un cliente
#       cve_detalle_vuelos = random.choice(list(vuelos_disponibles.keys()))
#       client_id = random.choice(clientes)
#       # Verificar si el vuelo aún tiene capacidad
#       if vuelos_disponibles[cve_detalle_vuelos]["ocupados"] < vuelos_disponibles[cve_detalle_vuelos]["capacidad"]:
#         ocupaciones_data.append((cve_detalle_vuelos, client_id))
#         vuelos_disponibles[cve_detalle_vuelos]["ocupados"] += 1
#         data_added += 1
#         if len(ocupaciones_data) >= 1000:
#           cursor.executemany("""
#             INSERT INTO ocupaciones (cve_detalle_vuelos, cve_clientes)
#             VALUES (?, ?)
#             """, ocupaciones_data
#           )
#           db_instance.commit()
#           ocupaciones_data.clear()
#     if ocupaciones_data:
#       cursor.executemany("""
#         INSERT INTO ocupaciones (cve_detalle_vuelos, cve_clientes)
#         VALUES (?, ?)
#         """, ocupaciones_data
#       )
#       db_instance.commit()
#     print("All queries executed successfully.")
#     is_loading = False
#   except Exception as e:
#     print(f"Error connecting to the database: {e}")
#     raise e
#   finally:
#     if cursor:
#       cursor.close()
#     if db_instance:
#       db_instance.close()


      
# @app.post('/start')
# def start(): 
#   global is_loading, inserted_count
#   thread = Thread(target=get_query_execute)
#   thread.start()
#   return {"message": "Query execution started"}

      
# def event_generator()->Generator[str,None,None]:
#   while is_loading: 
#     yield f"data: {is_loading}\n\n"
#     time.sleep(1)
#   yield f"data: done\n\n"

# @app.get("/progress")
# def progress():
#   return SR(event_generator(), media_type="text/event-stream")

