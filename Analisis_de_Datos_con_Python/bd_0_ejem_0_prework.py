#Hay básicamente dos tipos de datos estructurados con los que podemos toparnos:

#Numéricos y Categóricos

#Numéricos
# a) Discretos: Datos que sólo pueden tomar el valor de un número entero, como conteos o edades de personas.
# b) Continuos: Datos que pueden tomar cualquier valor dentro de un intervalo.

#Categóricos: Datos que sólo pueden tomar un conjunto específico de valores que representan un conjunto de posibles categorías.
# a) Binarios: Datos categóricos que sólo tienen dos categorías posibles.
# b) Ordinales: Datos categóricos que tienen un orden explícito, como rankings de películas que van del 1 al 10.

#Estimados de locación
#Hay muchas maneras de obtener nuestro valor "típico", pero vamos a aprender solamente las 3 más comunes.

# Promedio
#El promedio (mean en inglés) se obtiene sumando todos los datos y
# luego dividiéndolos entre la cantidad de datos que tenemos.
# Este estimado toma en cuenta todos los datos de nuestro conjunto.
# Por ejemplo, si tenemos los valores 3, 7, 1, 4, primero los sumaremos para obtener 15 y después los dividiríamos entre 4 (la cantidad de valores que tenemos) para obtener 3.75. Este valor, 3.75 es nuestro valor típico que mejor describe nuestro conjunto.

#Mediana
#La mediana se obtiene ordenando de menor a mayor nuestros valores y luego obteniendo el valor que está justo a la mitad de la secuencia. Por ejemplo, si tenemos 3, 7, 1, 4, 5, primero tendríamos que ordenarlos: 1, 3, 4, 5, 7 y después obtener el valor que está justo en medio: 4. 4 sería nuestro valor típico.
#En el caso de que la cantidad de valores sea par, se toma el promedio de los valores que están en medio. Por ejemplo, si tenemos 3, 7, 1, 4, primero los ordenamos: 1, 3, 4, 7. Y después sacamos el promedio entre 3 y 4 para obtener 3.5 como valor típico.
#Si eres observador, te habrás percatado de que utilizando el mismo conjunto de datos (3, 7, 1, 4) obtuvimos valores típicos distintos utilizando el promedio y la mediana. ¿Cuál es el criterio entonces para elegir la una o la otra?

#Así como hay valores típicos que sirven
# para describir nuestro dataset usando un solo valor, también existen valores que son radicalmente distintos al valor típico. Estos valores se encuentran tan alejados del valor típico que pueden pensarse como anomalías en nuestro conjunto de datos.
#Podemos simplificar diciendo que el promedio es preferible cuando no tenemos tantos valores atípicos y la mediana es preferible cuando tenemos valores atípicos que podrían afectar nuestro análisis.


#Media Truncada
#La media truncada es un estimado que nos sirve para volver más robusto nuestro promedio. Funciona de la siguiente forma:

#Primero ordenamos nuestros datos de menor a mayor.
#Después truncamos un porcentaje de nuestros datos al inicio y al final. Por ejemplo, si elegimos eliminar el 5% de los datos, eliminaríamos 2.5% de los datos al inicio de la secuencia y 2.5% al final.
#Con los datos restantes, obtenemos nuestro promedio usando el algoritmo original.

#La media truncada, al eliminar cierto porcentaje de datos al inicio y al final de nuestra secuencia, intenta disminuir el impacto de los valores atípicos sobre nuestro estimado. Es común eliminar entre el 5% y el 25% de nuestros datos al calcular una media truncada. Obviamente si tenemos un dataset pequeño va a ser preferible tomar la mediana a la media truncada, ya que esta última implica la eliminación de algunas de nuestras muestras.

#Estimados de variabilidad
#Ya que tenemos nuestro estimado de locación (el valor "típico") de nuestro dataset, el siguiente paso es saber qué tan lejanos o cercanos a este valor típico se encuentran los demás datos. Para esto utilizamos los estimados de variabilidad. Uno de los estimados más comunes es la desviación estándar.

#Desviación estándar

#La desviación estándar nos da la "desviación típica" de nuestros datos alrededor del valor típico. Es decir, qué tan dispersos podemos esperar que estén nuestros datos alrededor de nuestro estimado de locación.
#Para obtener la desviación estándar, se obtienen primero todas las diferencias entre cada valor y nuestro valor típico. Después se eleva cada valor al cuadrado, se suman todos estos valores, se dividen entre la cantidad de valores - 1, y finalmente se saca la raíz cuadrada del valor resultante.
#Si quieres entender paso a paso el algoritmo para calcular la desviación estándar, puedes revisar este link
#Los valores que se encuentren dentro de 1 desviación estándar del promedio pueden ser considerados comunes y esperados. El único problema es que la desviación estándar también es bastante sensible a valores atípicos. Si tenemos muchos valores atípicos muy extremos, nuestro cálculo podría no ser muy representativo de la población.
#Un estimado de variabilidad más robusto es la desviación absoluta de la mediana. No vamos a entrar en detalle, pero si quieres aprender cómo funciona, puedes leerlo

#Estadísticos de Orden
#Otra manera de estimar la dispersión de nuestros datos es analizando los datos ordenándolos de menor a mayor. Este tipo de análisis se llaman estadísticos de orden porque dependen de que nuestros datos estén ordenados de forma ascendente.

#Rango
#El rango es la diferencia entre el valor mínimo y el valor máximo de nuestro datos. El valor mínimo y el máximo nos pueden dar un buen indicador de la presencia de valores atípicos (sobre todo si los comparamos contra el estimado de locación). El rango es útil pero no es una estadística robusta, ya que si tenemos tan sólo 1 valor atípico demasiado extremo, nuestro rango cambia muy radicalmente.

#Para hacer esta estadística más robusta, podemos aplicar la misma técnica que utilizamos en la media truncada y eliminar una porción de los datos al inicio y al final de nuestro conjunto.


#Percentiles
#En un conjunto de datos, el percentil P es un valor que indica que por lo menos P% de los valores en el conjunto tienen este valor o un valor menor; mientras que (100-P)% de los valores tienen este valor o un valor mayor. Por ejemplo, para obtener el percentil 80 primero ordenamos nuestro conjunto de manera ascendente y después elegimos un valor de manera que el 80% de los valores en nuestro conjunto sean iguales o menores a ese valor.

#Digamos que tenemos este dataset: 1, 2, 3, 4, 5, 6, 7, 8, 9. El percentil 75 sería 7, ya que el 75% de los datos son menores a 8. El percentil 25 sería 3, mientras que el percentil 50 sería 5.

#El percentil 0 es el valor mínimo (1), mientras que el percentil 100 sería el valor máximo (9). Por lo tanto el rango podría pensarse como la diferencia entre el percentil 100 y el percentil 0.

#Rango Intecuartílico

#Otra estadística que es utilizada comúnmente es el rango intercuartílico, que está definido como la diferencia entre el percentil 75 y el percentil 50. Es decir, en nuestro dataset 1, 2, 3, 4, 5, 6, 7, 8, 9 el rango intercuartílico sería 7 - 3 = 4.

#Sabiendo los percentiles y el rango intercuartílico, podemos darnos una idea bastante precisa de la dispersión de nuestros datos. Por ejemplo, si tenemos un conjunto de datos que cumpla con las siguientes características:

#El valor mínimo es 0
#El valor máximo es 100
#El percentil 25 es 15
#El percentil 75 es 40
#El rango intercuartílico es 25
#La mediana es 25
#Podemos deducir viendo estos números que la mayoría de los datos están mucho más cercanos al valor mínimo que al valor máximo. Esto significa que hay un "sesgo" hacia los valores pequeños (pequeños en este contexto, claro) y que parece ser que hay valores muy grandes que están tan distantes de la mediana y de la mayoría de los valores que pueden ser considerados valores atípicos.

#Desarrollaremos nuestra intuición acerca de estas estadísticas usando visualizaciones en la siguiente sesión, pero por lo pronto, en la sesión aprenderás a calcular todas estas medidas usando Python y pandas.

folium

