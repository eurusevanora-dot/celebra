export function isMuroItem(p) {
  if (!p || typeof p !== "object") return false;
  if (typeof p.nombre !== "string" || !p.nombre.trim()) return false;
  if (p.para != null && typeof p.para !== "string") return false;
  if (p.texto != null && typeof p.texto !== "string") return false;
  if (p.archivo != null && typeof p.archivo !== "string") return false;
  return p.tipo === "image" || p.tipo === "video" || p.tipo === "texto";
}

export function isImagen(p) {
  return isMuroItem(p) && p.tipo === "image" && !!p.archivo;
}

export function isVideo(p) {
  return isMuroItem(p) && p.tipo === "video" && !!p.archivo;
}

export function isTexto(p) {
  return isMuroItem(p) && p.tipo === "texto" && typeof p.texto === "string" && p.texto.length > 0;
}

export function isMuro(data) {
  return Array.isArray(data) && data.every(isMuroItem);
}

export function mediaSrc(p) {
  if (!isImagen(p) && !isVideo(p)) return "";
  return "muro-media/" + p.archivo;
}
