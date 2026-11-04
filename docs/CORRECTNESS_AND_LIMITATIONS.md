# Correcciones y límites del prototipo Huffman

## Defectos corregidos en esta propuesta

- Eliminación del argumento mutable `codigos={}`, que podía contaminar llamadas posteriores.
- Una entrada de símbolo único recibe código `0` en lugar de una cadena vacía.
- Una cadena vacía no provoca división por cero al mostrar el cálculo de ahorro.

## Limitaciones todavía vigentes

`huffman_compressor_analyzer.py` devuelve una secuencia de bits en forma de texto y un árbol en memoria; **no es aún un formato de archivo comprimido interoperable**. Los porcentajes mostrados no incluyen cabeceras, estructura de árbol ni codificación real del texto Unicode, por lo que **no son mediciones completas de compresión de archivos**.

Para una siguiente versión: serializar tabla o árbol con formato versionado, añadir descompresión comprobable, tests con Unicode/archivos binarios y benchmarks con datasets abiertos y licencias verificadas.

Ejecutar `python -m unittest discover -s tests -v`.