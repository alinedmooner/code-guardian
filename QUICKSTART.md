# CodeGuardian - Guía Rápida de Inicio 🚀

## Instalación Rápida

```bash
# 1. Clonar el repositorio
git clone https://github.com/code-guardian/code-guardian.git
cd code-guardian

# 2. Crear entorno virtual (usando pyenv)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar el paquete en modo desarrollo
pip install -e ".[dev]"

# 4. Verificar instalación
pytest -v
```

## Uso Básico en 3 Pasos

### Paso 1: Inicializar Configuración

```bash
# Crear configuración para Clean Architecture
codeguardian init clean

# Esto crea un archivo codeguardian.yaml con plantilla predefinida
```

### Paso 2: Personalizar el YAML

Edita `codeguardian.yaml` para que coincida con tu proyecto:

```yaml
version: "1.0"
project_name: "mi-proyecto"
architecture: "clean"

modules:
  - name: "domain"
    path: "src/domain"      # ← Cambia esto a tu ruta
    layer: "domain"

  - name: "application"
    path: "src/application" # ← Y esto también
    layer: "application"

rules:
  - type: "no_import"
    from: "domain"
    to: ["application"]
    message: "Domain no puede importar de Application"
    severity: "error"
```

### Paso 3: Ejecutar Análisis

```bash
# Analizar tu proyecto
codeguardian analyze

# O con opciones
codeguardian analyze --path ./src --format json
```

## Ejemplo Completo

Supongamos que tienes este proyecto:

```
mi-proyecto/
├── src/
│   ├── domain/
│   │   └── entities.py
│   ├── application/
│   │   └── services.py
│   └── infrastructure/
│       └── repositories.py
└── codeguardian.yaml
```

### 1. Crear configuración

```bash
codeguardian init clean
```

### 2. Ajustar rutas en codeguardian.yaml

```yaml
modules:
  - name: "domain"
    path: "src/domain"
    layer: "domain"
  
  - name: "application"
    path: "src/application"
    layer: "application"
  
  - name: "infrastructure"
    path: "src/infrastructure"
    layer: "infrastructure"

rules:
  # Domain no puede depender de nada
  - type: "no_import"
    from: "domain"
    to: ["application", "infrastructure"]
    message: "Domain debe ser independiente"
    severity: "error"
  
  # Application solo puede depender de domain
  - type: "no_import"
    from: "application"
    to: ["infrastructure"]
    message: "Application no debe conocer infrastructure"
    severity: "error"
```

### 3. Validar configuración

```bash
codeguardian validate-config
```

### 4. Analizar

```bash
codeguardian analyze --path ./src
```

## Integración con GitHub Actions

Crea `.github/workflows/architecture.yml`:

```yaml
name: Architecture Check

on:
  pull_request:
    branches: [main]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install CodeGuardian
        run: pip install codeguardian
      
      - name: Run Analysis
        run: codeguardian analyze --fail-on-violation
```

## Comandos Útiles

```bash
# Ver ayuda
codeguardian --help

# Inicializar diferentes arquitecturas
codeguardian init clean       # Clean Architecture
codeguardian init ddd         # Domain-Driven Design
codeguardian init mvc         # Model-View-Controller
codeguardian init hexagonal   # Hexagonal Architecture
codeguardian init layered     # Layered Architecture

# Análisis con diferentes formatos
codeguardian analyze --format console  # Salida en consola (default)
codeguardian analyze --format json     # Salida JSON

# Guardar reporte en archivo
codeguardian analyze --format json --output report.json

# No fallar si hay violaciones (útil para ver todo)
codeguardian analyze --no-fail
```

## Desarrollo

```bash
# Instalar dependencias de desarrollo
pip install -e ".[dev]"

# Ejecutar tests
pytest -v

# Tests con cobertura
pytest --cov=codeguardian --cov-report=html

# Formatear código
make format

# Linters
make lint

# Ver todos los comandos disponibles
make help
```

## Arquitecturas Disponibles

| Arquitectura | Comando | Descripción |
|-------------|---------|-------------|
| Clean Architecture | `init clean` | Domain → Application → Infrastructure → Presentation |
| DDD | `init ddd` | Bounded contexts separados |
| MVC | `init mvc` | Model-View-Controller clásico |
| Hexagonal | `init hexagonal` | Ports & Adapters |
| Layered | `init layered` | N-tier tradicional |

## Ejemplos de Uso

### Ver ejemplo de Clean Architecture

```bash
cd examples/clean-architecture
codeguardian analyze
```

### Crear regla personalizada

```yaml
rules:
  # Prevenir imports circulares
  - type: "no_import"
    from: "users"
    to: ["orders"]
    message: "Users no debe importar Orders directamente"
    severity: "warning"
```

## Troubleshooting

### Error: "Configuration file not found"

```bash
# Verifica que exists codeguardian.yaml
ls codeguardian.yaml

# O especifica la ruta
codeguardian analyze --config path/to/config.yaml
```

### Error: "Module not found"

Asegúrate de que las rutas en `modules` coincidan con tu estructura:

```yaml
modules:
  - name: "domain"
    path: "src/domain"  # ← Debe existir este directorio
```

### No detecta violaciones

1. Verifica que las reglas estén bien configuradas
2. Revisa que los paths de módulos sean correctos
3. Usa `--no-fail` para ver todos los archivos analizados

## Próximos Pasos

1. ✅ Instalar y probar localmente
2. ✅ Crear configuración para tu proyecto
3. ✅ Ejecutar primer análisis
4. 🔄 Integrar en GitHub Actions
5. 🔄 Ajustar reglas según necesidad
6. 🔄 Documentar arquitectura del equipo

## Recursos

- 📖 [Documentación Completa](docs/USER_GUIDE.md)
- 🌟 [Ejemplos](examples/)
- 🐛 [Reportar Issues](https://github.com/code-guardian/code-guardian/issues)
- 💬 [Discusiones](https://github.com/code-guardian/code-guardian/discussions)

---

**¿Listo para proteger tu arquitectura?** 🛡️

```bash
codeguardian init clean && codeguardian analyze
```

