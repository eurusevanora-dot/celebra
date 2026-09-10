#!/usr/bin/env python3
"""Convierte una Issue moderada en una entrada validada del muro."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WALL = ROOT / "muro.json"
MEDIA = ROOT / "muro-media"
MAX_MEDIA = 20 * 1024 * 1024
ALLOWED_FOR = {"Miryam", "Gloria", "Joaquín", "Toda la familia"}
CONTENT_TYPES = {
    "image/jpeg": ("image", ".jpg"),
    "image/png": ("image", ".png"),
    "image/webp": ("image", ".webp"),
    "image/gif": ("image", ".gif"),
    "video/mp4": ("video", ".mp4"),
    "video/webm": ("video", ".webm"),
}


def field(body: str, heading: str) -> str:
    match = re.search(
        rf"^### {re.escape(heading)}\s*$\n(.*?)(?=\n### |\n<!--|\Z)",
        body,
        re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def clean(value: str, maximum: int, label: str) -> str:
    value = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", value).strip()
    if not value or len(value) > maximum:
        raise ValueError(f"{label} vacío o demasiado largo")
    return value


def attachment_url(section: str) -> str | None:
    matches = re.findall(r"https://github\.com/user-attachments/assets/[A-Za-z0-9-]+", section)
    return matches[0] if matches else None


def download_media(url: str, issue_number: int) -> tuple[str, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "celebra-publisher/1"})
    with urllib.request.urlopen(request, timeout=30) as response:
        content_type = response.headers.get_content_type().lower()
        if content_type not in CONTENT_TYPES:
            raise ValueError(f"tipo de adjunto no permitido: {content_type}")
        data = response.read(MAX_MEDIA + 1)
    if len(data) > MAX_MEDIA:
        raise ValueError("el adjunto supera 20 MB")
    kind, extension = CONTENT_TYPES[content_type]
    digest = hashlib.sha256(data).hexdigest()[:12]
    filename = f"issue-{issue_number}-{digest}{extension}"
    MEDIA.mkdir(exist_ok=True)
    (MEDIA / filename).write_bytes(data)
    return kind, filename


def main() -> int:
    number = int(os.environ["ISSUE_NUMBER"])
    body = os.environ["ISSUE_BODY"]
    item_id = f"github-issue-{number}"
    data = json.loads(WALL.read_text(encoding="utf-8"))
    if any(item.get("id") == item_id for item in data):
        print(f"SKIP: {item_id} ya estaba publicado")
        return 0

    nombre = clean(field(body, "Tu nombre"), 80, "nombre")
    para = clean(field(body, "Se lo dedicas a"), 80, "dedicatoria")
    if para not in ALLOWED_FOR:
        raise ValueError("destinatario no permitido")
    texto = clean(field(body, "Felicitación"), 2000, "felicitación")
    media_section = field(body, "Foto o vídeo (opcional)")
    url = attachment_url(media_section)
    item = {"id": item_id, "nombre": nombre, "para": para, "texto": texto, "tipo": "texto"}
    if url:
        kind, filename = download_media(url, number)
        item.update({"tipo": kind, "archivo": filename})
    data.append(item)
    WALL.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PUBLICADO: {item_id}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
