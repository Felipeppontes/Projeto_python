# Projeto_python-Media_1periodo
#Criei uma calculadora de media ponderada, para me auxiliar no 1º periodo da faculdade de engenharia em saber meu CR - coeficiente de rendimento


print("__MEDIA PONDERADA DO 1º PERIODO - ABI (UFPE)__\n")

print("__SUAS NOTAS EM CALCULO DIFERENCIAL E INTEGRAL 1__\n")
c1 = float(input("digite a nota da 1ª unidade de calculo 1:"))
c2 = float(input("digite a nota da 2ª unidade de caluculo 1:"))
c3 = float(input("digite a nota da 3ª unidade de calculo 1:"))
media_c1 =  (c1+c2+c3)/3

print("\n___SUAS NOTAS EM GEOMETRIA ANALÍTICA___")
ga1 = float(input("\ndigite a nota da 1ª unidade de Geometria Analítica:"))
ga2= float(input("digite a nota da 2ª unidade de Geometria analítica:"))
ga3= float(input("digite a nota da 3ª unidade de Geometria Analitica:"))
media_ga1 =  (ga1+ga2+ga3)/3

print("\n___SUAS NOTAS EM FÍSICA 1___\n")
f1 = float(input("digite a nota da 1ª unidade de física 1:"))
f2= float(input("digite a nota da 2ª unidade de física 1:"))
f3= float(input("digite a nota da 3ª unidade de física 1:"))
media_f1 =  (f1+f2+f3)/3

print("\n___SUAS NOTAS EM GEOMETRIA GRÁFICA TRIDIMENSIONAL___")
ggt1 = float(input("\ndigite a nota da 1ª unidade de GGT:"))
ggt2= float(input("digite a nota da 2ª unidade de GGT:"))
ggt3 = float(input("digite a nota da 3ª unidade de GGT:"))
media_ggt =  (ggt1+ggt2+ggt3)/3

print("\n___SUAS NOTAS EM INTRODUÇÃO A ENGENHARIA___")
i1 = float(input("\ndigite a nota da 1ª unidade de Introdução  a engenharia:"))
i2= float(input("digite a nota da 2ª unidade de Introdução  a engenharia:"))
i3= float(input("digite a nota da 3ª unidade de Introdução  a engenharia:"))
media_ie =  (i1+i2+i3)/3

print("\n__ESSAS SÃO SUAS MEDIAS__")
print("\nA media em calculo 1--->", media_c1)
print("A media em Geometria Analítica--->", media_ga1)
print("A media em Física 1--->", media_f1)
print("A media em GGT--->", media_ggt)
print("A media em introd. a engenharia--->", media_ie)

media_CR = (media_c1*4+media_ga1*4+media_f1*4+media_ggt*3+media_ie*4)/19
print("\n*******ESSE É SEU COEFICIENTE DE RENDIMENTO******\n")
print("----------------------------\n",media_CR,"\n""------")
