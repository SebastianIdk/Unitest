# 🧪 Ejemplo de Testing con Pytest

Un repositorio pequeño para demostrar pruebas unitarias en Python usando **pytest** y **coverage**.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)  
[![Pytest](https://img.shields.io/badge/pytest-%3E%3D6.0-green)](https://docs.pytest.org/)  
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://coverage.readthedocs.io/)

---

## 🚀 Comenzar

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
   ```

2. **Crear y activar entorno virtual**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # en macOS/Linux
   venv\Scripts\activate     # en Windows
   ```

3. **Instalar dependencias**  
   ```bash
   pip install pytest coverage
   ```

4. **Ejecutar pruebas**  
   ```bash
   pytest
   ```

5. **Reporte de cobertura**  
   ```bash
   coverage run -m pytest
   coverage report -m
   ```

---

## 📂 Estructura

- `math_ops.py` – Funciones matemáticas.  
- `test_math_ops.py` – Pruebas unitarias con pytest.
