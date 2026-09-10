export type MuroTipo = "image" | "video" | "texto";
export type MuroPara = "Miryam" | "Gloria" | "Joaquín" | "Toda la familia" | string;

export interface MuroItemBase {
  nombre: string;
  para?: MuroPara;
  texto?: string;
}

export interface MuroImagen extends MuroItemBase {
  tipo: "image";
  archivo: `${string}.${"jpg" | "jpeg" | "png" | "webp" | "gif"}`;
}

export interface MuroVideo extends MuroItemBase {
  tipo: "video";
  archivo: `${string}.${"mp4" | "webm"}`;
}

export interface MuroTexto extends MuroItemBase {
  tipo: "texto";
  texto: string;
  archivo?: "" | string;
}

export type MuroItem = MuroImagen | MuroVideo | MuroTexto;
export type Muro = MuroItem[];
