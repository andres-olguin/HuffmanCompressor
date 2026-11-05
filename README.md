# Huffman Compression Lab — Compresión y análisis de eficiencia

Laboratorio académico en Python para estudiar **codificación de Huffman**, frecuencias de símbolos, construcción de árboles binarios y generación de secuencias de bits. Incluye pruebas automatizadas y una demostración web educativa separada.

> **Estado:** prototipo algorítmico. El código devuelve bits como texto y un árbol en memoria; **no genera un formato de archivo comprimido interoperable** ni incluye un descompresor de archivos de producción.

## Inicio rápido

**Requisitos:** Python 3.10 o superior, sin dependencias de terceros para ejecutar el módulo principal.

```bash
python huffman_compressor_analyzer.py
python -m unittest discover -s tests -v
```

El primer comando ejecuta el ejemplo integrado e imprime cantidad de bits calculados y un porcentaje teórico; el segundo ejecuta pruebas de casos generales y límites.

## Componentes

| Archivo | Responsabilidad |
|---|---|
| [`huffman_compressor_analyzer.py`](huffman_compressor_analyzer.py) | Frecuencias, árbol, códigos y estimación teórica |
| [`tests/`](tests/) | Pruebas de entradas vacías, símbolo único, estado compartido y propiedades de prefijos |
| [`.github/workflows/python-tests.yml`](.github/workflows/python-tests.yml) | Validación automatizada en GitHub Actions |
| [`docs/index.html`](docs/index.html) | Interfaz didáctica que puede servir de demostración mediante GitHub Pages |
| [`docs/CORRECTNESS_AND_LIMITATIONS.md`](docs/CORRECTNESS_AND_LIMITATIONS.md) | Correcciones y limitaciones técnicas |

## Cómo funciona

```mermaid
flowchart LR
    A[Texto] --> B[Frecuencias]
    B --> C[Cola de prioridad]
    C --> D[Árbol de Huffman]
    D --> E[Tabla de códigos]
    E --> F[Secuencia de bits como cadena]
```

El principio consiste en asignar códigos de longitud variable a símbolos según su frecuencia. **La métrica presentada es didáctica:** compara caracteres asumiendo 8 bits por símbolo frente a la longitud de la secuencia codificada, sin incluir el costo de serializar el árbol, cabeceras o empaquetado.

## Estado de calidad

Se corrigieron casos de entrada vacía, símbolo único y reutilización de un diccionario mutable entre llamadas. Las pruebas automatizadas verifican comportamientos específicos, pero no sustituyen una validación integral de compresión/descompresión sobre archivos.

## Próximos hitos

1. Implementar formato binario versionado y cabeceras.
2. Añadir descompresión y pruebas de ida/vuelta.
3. Manejar Unicode y archivos binarios con control de errores.
4. Comparar tamaño real, memoria y tiempo con corpus abiertos.
5. Documentar resultados replicables y evitar porcentajes de ahorro sin incluir overhead.

[Estudio de evolución](docs/ESTUDIO_DE_EVOLUCION_2026-10-30.md) · [Escalabilidad y pruebas](docs/ARCHITECTURE_SCALABILITY_2026-11-04.md).

**Contexto:** proyecto de aprendizaje de Análisis y Diseño de Algoritmos. Revisar licencia y autoría antes de reutilizar recursos externos.
