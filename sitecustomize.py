import numpy as np

# Fix para permitir cargar pickles creados con numpy antiguo
if not hasattr(np, "_core"):
    np._core = np.core