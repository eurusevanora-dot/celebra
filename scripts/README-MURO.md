# Muro público Myrian’s Family

La web lee y escribe directamente en Supabase. El visitante no sale de la página:
su felicitación y su archivo opcional quedan con estado `pending`.

Contexto fijo: `myrians-family / celebra / production`.

## Moderación

1. Abrir `public.celebra_entries` en el proyecto Supabase `NEXUS-0NE-7`.
2. Revisar que el texto y el archivo no incluyan datos privados ni contenido inadecuado.
3. Para aprobar, cambiar `status` a `published` y establecer `published_at`.
4. Para rechazar, cambiar `status` a `rejected` y borrar el archivo correspondiente si existe.

El navegador solo puede insertar filas pendientes y leer filas publicadas. No puede
aprobar, editar ni borrar. La clave publicable del frontend está protegida por RLS;
nunca debe añadirse una clave secreta o `service_role` al repositorio.

`muro.json`, su esquema y sus validadores quedan como formato heredado y ya no son
la fuente del muro público.
