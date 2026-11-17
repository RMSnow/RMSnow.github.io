"""Preserve embedded Adobe CJK glyphs while making PDFs self-contained.

Usage: python fix_chinese_pdf.py input.pdf output.pdf
Requires pypdf and fonttools. Run after XeLaTeX when using the Adobe fonts.
"""

import sys
from pathlib import Path

from fontTools.ttLib import TTFont
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    DecodedStreamObject,
    NameObject,
    NumberObject,
    TextStringObject,
)


def fix_pdf(source, destination):
    writer = PdfWriter()
    writer.clone_document_from_reader(PdfReader(source))
    fonts_dir = Path(__file__).resolve().parents[1] / "fonts" / "zh_CN-Adobe"
    processed = set()
    for page in writer.pages:
        for reference in page["/Resources"]["/Font"].values():
            font = reference.get_object()
            if id(font) in processed or "/DescendantFonts" not in font:
                continue
            processed.add(id(font))
            descendant = font["/DescendantFonts"][0].get_object()
            collection = descendant["/CIDSystemInfo"]
            if collection.get("/Ordering") != "GB1":
                continue
            if font.get("/Encoding") != "/Identity-H":
                raise ValueError("Expected horizontal identity encoding")
            name = str(font["/BaseFont"]).split("+")[-1].removesuffix("-Identity-H")
            original = TTFont(fonts_dir / f"{name}.otf")
            mappings = {}
            for codepoint, glyph in original.getBestCmap().items():
                if glyph.startswith("cid"):
                    mappings.setdefault(int(glyph[3:]), codepoint)
            original.close()
            # Identity-H already addresses the embedded glyphs by CID. Declare
            # that explicitly so readers do not need external Adobe-GB1 data.
            collection[NameObject("/Ordering")] = TextStringObject("Identity")
            collection[NameObject("/Supplement")] = NumberObject(0)
            # Older XeTeX omits ToUnicode for Adobe collection fonts. Include
            # the mapping so selection, search and copy work independently.
            lines = [
                "/CIDInit /ProcSet findresource begin", "12 dict begin", "begincmap",
                "/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def",
                "/CMapName /Adobe-UCS def", "/CMapType 2 def",
                "1 begincodespacerange", "<0000> <FFFF>", "endcodespacerange",
            ]
            pairs = sorted(mappings.items())
            for start in range(0, len(pairs), 100):
                chunk = pairs[start:start + 100]
                lines.append(f"{len(chunk)} beginbfchar")
                for cid, codepoint in chunk:
                    unicode_hex = chr(codepoint).encode("utf-16-be").hex()
                    lines.append(f"<{cid:04X}> <{unicode_hex}>")
                lines.append("endbfchar")
            lines.extend(["endcmap", "CMapName currentdict /CMap defineresource pop", "end", "end"])
            stream = DecodedStreamObject()
            stream.set_data("\n".join(lines).encode("ascii"))
            font[NameObject("/ToUnicode")] = writer._add_object(stream.flate_encode())
    writer.write(destination)


if __name__ == "__main__":
    fix_pdf(*sys.argv[1:])
