# huffman-compression-lab — Ingeniería, pruebas y escalabilidad realista

**Estado:** plan técnico documentado el 04-11-2026. No constituye resultado experimental ejecutado.

## Evidencia de partida

Ejercicio Python de Huffman; se corrigió diccionario mutable y tratamiento de cadenas vacías/símbolo único con tests.

## Incrementos de ingeniería

Definir serialización binaria con tabla o árbol explícito, descompresor inverso y verificación bit a bit. Probar Unicode UTF-8, archivos binarios, truncamientos y formato versionado.

## Estrategia de escalabilidad

Benchmarks de tamaño antes/después incluyendo overhead, tiempo CPU y memoria, distintos tipos de datos y tasas de entropía. Medir con datos abiertos con licencia verificada.

## Riesgos y condición de aprobación

Un bitstring Python no es automáticamente archivo comprimido; porcentajes del prototipo no incluyen encabezados ni bit packing.

## Protocolo de experimentación y calidad

Cada comparativa debe incluir referencia de código/commit, entorno, versiones, semilla cuando corresponda, entrada reproducible, comando de ejecución, datos brutos, repetición y límites. Separar datos de ejemplo de resultados realmente ejecutados. Mantener código histórico y coautoría intactos; publicar evidencias de tests de CI y pruebas manuales en su contexto, sin inventar métricas.

## Referencias consultadas (2026-11-04)

- [AWS Well-Architected — rendimiento y costo](https://docs.aws.amazon.com/wellarchitected/).
- [NIST SSDF — prácticas seguras de software](https://csrc.nist.gov/pubs/sp/800/218/final).
- [Google SRE — medición y objetivos](https://sre.google/workbook/implementing-slos/).

Las referencias son metodológicas; no corroboran los benchmarks particulares de este repositorio.
