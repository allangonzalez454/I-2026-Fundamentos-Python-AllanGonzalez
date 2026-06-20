import pandas

datos = pandas.read_csv('Clase_08/Estudiantes.csv')

print(datos[["nombre", "nota"]].head())

print(datos.describe())

print(datos['edad'].max())

print(datos['edad'].min())

estudiantes_alta_nota = datos[datos['nota'] > 85]
print(estudiantes_alta_nota)

media_por_sexo = datos.groupby('sexo')['nota'].mean()
print(media_por_sexo)