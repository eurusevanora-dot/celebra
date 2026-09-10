# Muro público Myrian’s Family

La web lee y escribe directamente en Supabase. El visitante no sale de la página:
su felicitación y su archivo opcional se publican automáticamente.

Contexto fijo: `myrians-family / celebra / production`.

## Publicación

Las nuevas filas nacen con `status = published` y `published_at` asignado por la base.
El muro vuelve a cargarse inmediatamente después de cada envío.

El navegador solo puede insertar filas publicadas y leer filas publicadas. No puede
editar ni borrar. La clave publicable del frontend está protegida por RLS;
nunca debe añadirse una clave secreta o `service_role` al repositorio.

`muro.json`, su esquema y sus validadores quedan como formato heredado y ya no son
la fuente del muro público.
