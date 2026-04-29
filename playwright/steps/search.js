const { Given, When, Then, Before, After, setDefaultTimeout } = require('@cucumber/cucumber');
const { chromium } = require('playwright');
const assert = require('assert');

setDefaultTimeout(30000);

let browser;
let context;
let page;

Before(async function () {
  const isCI = process.env.CI === 'true' || process.env.GITHUB_ACTIONS === 'true';

  browser = await chromium.launch({
    headless: isCI || !process.env.DEBUG_BROWSER,
    args: [
      '--disable-blink-features=AutomationControlled',
    ],
  });

  context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    viewport: { width: 1920, height: 1080 },
    locale: 'es-MX',
    timezoneId: 'America/Mexico_City',
  });

  page = await context.newPage();

  // Oculta que es automatizado
  await page.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined,
    });
    Object.defineProperty(navigator, 'plugins', {
      get: () => [1, 2, 3],
    });
  });

  // Delay inicial para evitar bloqueo en primera búsqueda
  await page.waitForTimeout(5000);
});

After(async function () {
  if (page) await page.close();
  if (context) await context.close();
  if (browser) await browser.close();
});

Given('I am on the Google homepage', async function () {
  await page.goto('https://www.google.com');
  // Espera a que el input se genere (JS dinámico)
  await page.waitForSelector('#APjFqb', { timeout: 10000 });
});

When('I search for {string}', async function (query) {
  const searchBox = page.locator('#APjFqb');
  await searchBox.click();
  await page.waitForTimeout(800);
  await searchBox.type(query, { delay: 80 });
  await page.waitForTimeout(800);
  await searchBox.press('Enter');
  await page.waitForNavigation({ waitUntil: 'networkidle' });
});

Then('the results page title should start with {string}', async function (query) {
  // Verifica que NO redirigió a /sorry (bloqueo de Google)
  if (page.url().includes('/sorry')) {
    throw new Error('Google bloqueó la búsqueda (página /sorry). Intenta de nuevo.');
  }

  const title = await page.title();
  assert.strictEqual(title.startsWith(query), true, `Title "${title}" doesn't start with "${query}"`);
});
