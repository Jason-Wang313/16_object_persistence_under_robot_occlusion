# Paper16 VLA Highlight Hardening Plan

Date: 2026-06-20

## Objective

Make `C:/Users/wangz/Downloads/16.pdf` explicitly match the visible VLA-v4
role model's boxed-link behavior while preserving the final 25-page object
persistence paper:

- citation links use green one-point boxes;
- internal figure/table/equation/section links use red one-point boxes;
- URL links use green one-point boxes;
- the final PDF is rebuilt, copied to Downloads, visually checked, and leaves
  no local `paper/main.pdf`.

## Plan-Start Evidence

Baseline artifact:

- Canonical PDF: `C:/Users/wangz/Downloads/16.pdf`
- Pages: 25
- Size: 382,537 bytes
- SHA256: `B74479204FE59A984915A9ECDD763BC796290AE7BE304C4B16CBDEE973C4F0A4`
- Local `paper/main.pdf`: absent
- Repository branch: `main`

Baseline link inventory from the current Downloads PDF:

- Link pages: `[(2, 40), (4, 3), (5, 3)]`
- Annotation colors: green = 40, red = 6, cyan = 0
- Border widths: `(0, 0, 1)` for all 46 link annotations

Source finding:

- `paper/main.tex` is the active manuscript source.
- The preamble loads plain `\usepackage{hyperref}` but does not explicitly
  lock `citebordercolor`, `linkbordercolor`, `urlbordercolor`, or
  `pdfborder`.
- The current PDF already has green citation/URL boxes, red internal-reference
  boxes, and no cyan, but the target is to make that behavior explicit and
  reproducible.
- There is no dedicated build script in `scripts/`; use the documented manual
  `pdflatex`, `bibtex`, and repeated `pdflatex` sequence from `paper/`, then
  copy `paper/main.pdf` to Downloads and remove the local PDF.

## Role-Model Target

Install the same explicit hyperref policy as the visible VLA-v4 role model:

```tex
\usepackage{hyperref}
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

## Execution Plan

1. Add the VLA `\hypersetup` block immediately after `\usepackage{hyperref}`
   in `paper/main.tex`.
2. Rebuild manually from `paper/` with `pdflatex`, `bibtex`, and repeated
   `pdflatex` passes.
3. If the log asks for another pass for cross-references, run the final
   canonical pass before recording metadata.
4. Copy the rebuilt `paper/main.pdf` to `C:/Users/wangz/Downloads/16.pdf`.
5. Remove local `paper/main.pdf` after export.
6. Recompute page count, byte size, SHA256, annotation colors, border widths,
   and link pages from the final Downloads PDF.
7. Render every page that contains link annotations into
   `tmp/pdfs/paper16_after`.
8. Visually inspect rendered affected pages:
   - green citation and URL boxes are crisp and aligned;
   - red internal-reference boxes are crisp and aligned;
   - no cyan boxes appear;
   - layout, figures, tables, headers, and page count remain stable.
9. Update README/status/audit/version/validation metadata with the new hash and
   VLA-style boxed-link inventory.
10. Validate build logs, diff hygiene, final PDF hash, and absence of local
    `paper/main.pdf`.
11. Remove Paper16 temp renders, leaving only the shared role-model render
    directory.
12. Stage only Paper16 source and metadata files, commit, push, and verify a
    clean repository before moving to Paper15.

## Non-Goals

- Do not alter experiment results, claims, figures, tables, bibliography
  content, or page count.
- Do not add or remove citations, references, or URLs merely to change link
  counts.
- Do not leave intermediate PDFs or render folders behind.

## Completion Evidence

- Added the explicit VLA `\hypersetup` block immediately after
  `\usepackage{hyperref}` in `paper/main.tex`.
- Rebuilt from `paper/` with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Exported canonical PDF: `C:/Users/wangz/Downloads/16.pdf`
- Pages: 25
- Size: 382,537 bytes
- SHA256: `654F284A02E2AD6E9D267AC07BE40F9ACD0CEDC0B61A1719A61064C62C776598`
- Link inventory: 46 annotations on pages `[(2, 40), (4, 3), (5, 3)]`; green = 40, red = 6, cyan = 0; all borders `(0, 0, 1)`.
- Visual audit: rendered pages 2, 4, and 5; green citation/URL boxes and red internal-reference boxes are crisp and aligned.
- Local `paper/main.pdf`: removed after export.
