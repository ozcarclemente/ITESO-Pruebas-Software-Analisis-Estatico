# Google Search Tests - Playwright + Cucumber (JavaScript)
## Oscar Clemente López Labrador & Sofía Mercado Moreno

Tests BDD con Playwright (Chrome) + Cucumber. Simula búsquedas en Google evitando detección de bots.

## Estructura

```
playwright/
├── features/
│   └── search.feature        # Scenarios BDD (igual que Selenium)
├── steps/
│   └── search.js             # Step definitions con Playwright
├── cucumber.js               # Configuración Cucumber
├── package.json
└── README.md
```

## Instalación

```bash
cd playwright
npm install
npx playwright install chromium
```

## Ejecutar tests

```bash
# Local (navegador visible)
npm test

# CI (headless)
CI=true npm test

# Debug (abre navegador)
DEBUG_BROWSER=true npm test
```

## Diferencias Selenium vs Playwright

| Aspecto | Selenium (Python) | Playwright (JS) |
|--------|-------------------|-----------------|
| Iniciar | `webdriver.Chrome()` | `chromium.launch()` |
| Buscar elemento | `find_element("id", "...")` | `page.locator('#...')` |
| Llenar input | `send_keys()` | `fill()` |
| Presionar tecla | `send_keys(Keys.RETURN)` | `press('Enter')` |
| Esperar elemento | `WebDriverWait` + `EC` | `page.waitForSelector()` |
| Cerrar | `driver.quit()` | `page.close()` + `browser.close()` |

## Anti-detección de bots

Para evitar que Google bloquee las búsquedas:

- **User-Agent realista**: Chrome 120 en Windows
- **navigator.webdriver override**: Oculta `navigator.webdriver` (detección común)
- **Delays**: 2s inicial + 50ms entre caracteres + 200ms antes de Enter
- **Tipo humano**: usa `type()` con delay en lugar de `fill()`

## Hooks

- `Before`: Lanza Chromium, configura contexto, agrega 2s delay inicial
- `After`: Cierra página, contexto y navegador
