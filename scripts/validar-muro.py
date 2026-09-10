#!/usr/bin/env python3
import json, sys, re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
data = json.loads((root/"muro.json").read_text(encoding="utf-8"))
errs=[]
if not isinstance(data, list):
    errs.append("muro.json debe ser un array")
for i,p in enumerate(data if isinstance(data,list) else []):
    if not isinstance(p, dict):
        errs.append(f"[{i}] no es objeto"); continue
    extra=set(p)-{"id","archivo","nombre","tipo","texto","para"}
    if extra: errs.append(f"[{i}] campos extra: {extra}")
    nombre=str(p.get("nombre") or "")
    item_id=str(p.get("id") or "")
    tipo=p.get("tipo")
    texto=str(p.get("texto") or "")
    archivo=str(p.get("archivo") or "")
    para=str(p.get("para") or "")
    if not re.match(r"^github-issue-[1-9][0-9]*$", item_id): errs.append(f"[{i}] id inválido")
    if not nombre or len(nombre)>80: errs.append(f"[{i}] nombre inválido")
    if tipo not in ("image","video","texto"): errs.append(f"[{i}] tipo inválido")
    if len(texto)>2000: errs.append(f"[{i}] texto demasiado largo")
    if len(para)>80: errs.append(f"[{i}] para demasiado largo")
    if tipo=="texto" and not texto: errs.append(f"[{i}] texto obligatorio")
    if tipo in ("image","video") and not archivo: errs.append(f"[{i}] archivo obligatorio")
    if archivo and not re.match(r"^[^/\\]+\.(jpg|jpeg|png|webp|gif|mp4|webm)$", archivo, re.I):
        errs.append(f"[{i}] archivo inválido: {archivo}")
    if archivo and not (root/"muro-media"/archivo).exists():
        errs.append(f"[{i}] falta muro-media/{archivo}")
if errs:
    print("INVALIDO"); print("\n".join(errs)); sys.exit(1)
print("VALIDO", len(data), "entradas")
