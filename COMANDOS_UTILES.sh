#!/bin/bash
# CodeGuardian - Comandos Útiles de Desarrollo
echo "🛡️  CodeGuardian - Comandos Útiles"
echo "=================================="
echo ""
# Activar entorno virtual
echo "📦 Para activar el entorno virtual:"
echo "   source venv/bin/activate"
echo ""
# Tests
echo "🧪 Tests:"
echo "   pytest -v                    # Ejecutar todos los tests"
echo "   pytest --cov                 # Tests con cobertura"
echo "   pytest tests/test_analyzer.py -v  # Test específico"
echo ""
# Uso del CLI
echo "💻 Uso del CLI:"
echo "   codeguardian init clean      # Crear config Clean Architecture"
echo "   codeguardian analyze         # Analizar proyecto actual"
echo "   codeguardian validate-config # Validar configuración"
echo ""
# Desarrollo
echo "🔧 Desarrollo:"
echo "   make test                    # Ejecutar tests"
echo "   make coverage                # Cobertura completa"
echo "   make format                  # Formatear código"
echo "   make lint                    # Linters"
echo ""
# Análisis avanzado
echo "🔍 Análisis avanzado:"
echo "   codeguardian analyze --path ./src --format json"
echo "   codeguardian analyze --no-fail  # No fallar en violaciones"
echo "   codeguardian analyze --format json --output report.json"
echo ""
# Ejemplo práctico
echo "🎯 Ejemplo práctico completo:"
echo "   cd examples/clean-architecture"
echo "   codeguardian analyze"
echo ""
# Ver estructura del proyecto
echo "📂 Ver estructura:"
echo "   tree -L 3 -I 'venv|__pycache__|*.pyc'"
echo ""
# Reinstalar el paquete
echo "🔄 Reinstalar:"
echo "   pip install -e '.[dev]'"
echo ""
echo "=================================="
echo "Para más información: cat README.md"
