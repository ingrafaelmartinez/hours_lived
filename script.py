#Un pequeño script para saber las horas que has vivido 

age = int(input("Hola, para saber cuántas horas has vivido por favor introduce tu edad en años: "))
hours_year = 24 * 365
hours_lived = round(age * hours_year)  #La función round omite los decimales

print(f"Has vivido alrededor de {hours_lived} horas en tus {age} años")
