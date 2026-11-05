"""Generación de guías de estudio personalizadas en PDF."""

from .service import GUIDE_SUBJECTS, build_guide, guide_catalog

__all__ = ["GUIDE_SUBJECTS", "build_guide", "guide_catalog"]
