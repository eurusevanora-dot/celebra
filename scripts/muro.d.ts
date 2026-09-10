export type MuroTipo = "image" | "video" | "texto";

interface MuroBase {
  nombre: string;
  para?: string;
}

export interface MuroImagen extends MuroBase {
  tipo: "image";
  archivo: string;
  texto?: string;
}

export interface MuroVideo extends MuroBase {
  tipo: "video";
  archivo: string;
  texto?: string;
}

export interface MuroTexto extends MuroBase {
  tipo: "texto";
  texto: string;
  archivo?: string;
}

export type MuroItem = MuroImagen | MuroVideo | MuroTexto;
export type Muro = MuroItem[];

export function isImagen(p: MuroItem): p is MuroImagen {
  return p.tipo === "image";
}
export function isVideo(p: MuroItem): p is MuroVideo {
  return p.tipo === "video";
}
export function isTexto(p: MuroItem): p is MuroTexto {
  return p.tipo === "texto";
}

export function mediaSrc(p: MuroItem): string {
  if (p.tipo === "texto") return "";
  return p.archivo ? "muro-media/" + p.archivo : "";
}
