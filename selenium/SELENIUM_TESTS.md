# Instrucciones para ejecutar pruebas Selenium

## Descripción

Suite de pruebas de sistema nivel BDD (Behavior Driven Development) usando Behave + Selenium. Prueba búsquedas en Google y validación de sitios universitarios. Se ejecuta en modo **headless** para CI/CD.

## Requisitos previos

### Dependencias instaladas

- `behave==1.3.3` - Framework BDD
- `selenium==4.36.0` - Automatización del navegador

### Otras dependencias

- **Google Chrome** instalado en el sistema
- **ChromeDriver** - Se descarga automáticamente con `selenium-manager` en Selenium 4.36+

## Estructura del proyecto

```
selenium/
├── features/
│   └── search.feature          # Definición de escenarios (Gherkin)
├── steps/
│   └── search.py               # Implementación de pasos (Python)
└── behave.ini                  # Configuración de Behave
```

## Ejecutar todas las pruebas

```bash
cd /Users/oz/Documents/ITESO-Local/pruebas-software/static-testing
behave selenium/
```

## Ejecutar una feature específica

```bash
behave selenium/features/search.feature
```

## Opciones útiles de Behave

### Ver más detalles de ejecución

```bash
behave selenium/ -v
```

### Incluir detalles de cada paso

```bash
behave selenium/ --steps
```

### Ejecutar con formato JSON (para parsear resultados)

```bash
behave selenium/ -f json --outfile results.json
```

### Ejecutar un escenario específico por nombre

```bash
behave selenium/ -n "Search university on Google and verify related programs"
```

## Configuración en behave.ini

```ini
[behave]
stdout_capture = false    # Muestra print() en tiempo real
stderr_capture = false    # Muestra stderr en tiempo real
```

## Qué hacen las pruebas

Las pruebas en `search.feature` validan:

1. **Búsqueda en Google** - Abre Google y busca universidades (ITESO, UAG, UP)
2. **Navegación a sitio universitario** - Hace clic en el primer resultado que coincida con el dominio
3. **Búsqueda interna** - Realiza búsqueda en el sitio de la universidad
4. **Validación de resultados** - Verifica que los resultados contienen la palabra clave esperada (≥2 veces)

### Casos de prueba (Data-Driven Testing)

| Universidad | Dominio   | Búsqueda   | Palabra esperada |
| ----------- | --------- | ---------- | ---------------- |
| ITESO       | iteso.mx  | carreras   | carrera          |
| ITESO       | iteso.mx  | posgrados  | posgrado         |
| UAG         | uag.mx    | ingeniería | ingeniería       |
| UAG         | uag.mx    | posgrado   | posgrado         |
| UP          | up.edu.mx | campus     | campus           |
| UP          | up.edu.mx | posgrados  | posgrado         |

## Verificar entorno

```bash
# Activar venv (si es necesario)
source venv/bin/activate

# Verificar instalación de behave
behave --version

# Verificar instalación de Selenium
python -c "import selenium; print(f'Selenium {selenium.__version__}')"
```

## Solución de problemas

### Chromedriver no encontrado

Selenium 4.36+ incluye `selenium-manager` que descarga automáticamente ChromeDriver. Si falla:

```bash
python -m pip install --upgrade selenium
```

### Timeout en selectors

Timeouts configurados en `search.py`:

- Google search: 15 segundos (línea 70)
- Click link: 20 segundos (línea 82)
- Verify domain: 15 segundos (línea 123)
- Search on site: 20 segundos (línea 131)
- Verify results: 15 segundos (línea 169)

Para aumentar globalmente:

```python
# Editar en search.py
wait = WebDriverWait(context.driver, 30)  # Cambiar número según sea necesario
```

### Tests cierran el navegador muy rápido

Por diseño, el navegador se cierra tras cada escenario en el paso `step_verify_results()`. Para debugging, comentar la línea `context.driver.quit()`

## Selectores por sitio

Cada universidad tiene selectores específicos definidos en `SELECTORS` dict (línea 37-44):

| Sitio     | Icon selector               | Input selector   |
| --------- | --------------------------- | ---------------- |
| iteso.mx  | ID: `icon-search`           | ID: `ipt-search` |
| uag.mx    | ID: `searchHead`            | ID: `schm`       |
| up.edu.mx | CLASS: `icon-header-search` | NAME: `phrase`   |

Si los selectores cambian en los sitios, actualizar el dict `SELECTORS` en `search.py`.

## Notas importantes

- Pruebas corren en **modo headless** (`--headless=new`) — sin ventana visible
- Abre/cierra navegador **por cada escenario**
- Implementa `human_delay()` para simular comportamiento humano (evita detección de bots)
- Intenta múltiples selectores CSS/XPATH para mayor robustez (líneas 89-113)
- Timeout page load global: 30 segundos (línea 62)
