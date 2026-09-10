# Muro público MIRYAM 25

Hay un solo muro: `muro.json` + `muro-media/` en GitHub Pages.
Todo el mundo ve lo mismo. No hay muro por navegador.

La web abre una solicitud moderada en GitHub. Nada se publica automáticamente.

1. Revisar que no incluya datos privados ni contenido inadecuado.
2. Añadir la etiqueta `publicar` a la Issue aprobada.
3. La Action `Publicar recuerdo aprobado` descarga un adjunto permitido, actualiza
   `muro.json`, valida el resultado, crea el commit y cierra la Issue.
4. GitHub Pages despliega el nuevo muro.

Rollback: revertir el commit `Publicar recuerdo aprobado #N`; el medio usa un nombre
determinista y cada entrada conserva `id: github-issue-N` para evitar duplicados.
