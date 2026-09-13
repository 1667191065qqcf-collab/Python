def poligono(base, altura):
    
    triangulo= (base * altura)/2
    
    cuadrado= base*2
    
    rectangulo= base*altura
    
    return triangulo, cuadrado, rectangulo
    
resultado=list(poligono(2,3))

print("El area del triangulo es:", resultado[0],"m²")
print("El area del cuadrado es:", resultado[1],"m²")
print("El area del rectangulo es:", resultado[2],"m²")


print("El area de un triangulo es:", poligono(2,3)[0],"m²")