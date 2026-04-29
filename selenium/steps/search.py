"""
Steps for Google search and university site search
using Selenium WebDriver with Behave.
"""

# pylint: disable=not-callable

import random
import time

from behave import given, then, when
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver

USER_AGENTS = [
    (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    ),
    (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    ),
    "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
]


def human_delay(min_sec=0.5, max_sec=2.5):
    """Delay aleatorio para simular comportamiento humano."""
    time.sleep(random.uniform(min_sec, max_sec))


def _click_link_and_verify(driver, link, domain, wait):
    """Helper para clickear link y verificar navegación."""
    wait.until(EC.element_to_be_clickable(link))
    driver.execute_script("arguments[0].scrollIntoView(true);", link)
    human_delay(0.3, 0.7)
    driver.execute_script("arguments[0].click();", link)
    human_delay(1, 2)
    wait.until(EC.url_contains(domain))


SELECTORS = {
    "iteso.mx": {"icon": (By.ID, "icon-search"), "input": (By.ID, "ipt-search")},
    "uag.mx": {"icon": (By.ID, "searchHead"), "input": (By.ID, "schm")},
    "up.edu.mx": {
        "icon": (By.CLASS_NAME, "icon-header-search"),
        "input": (By.NAME, "phrase"),
    },
}


@given("I open Google")
def step_open_google(context):
    """Abre Google en headless mode."""
    options = Options()

    # Stealth options agresivos
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-component-extensions-with-background-pages")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-prompt-on-repost")
    options.add_argument("--enable-automation=false")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-web-resources")

    # User-agent aleatorio
    user_agent = random.choice(USER_AGENTS)
    options.add_argument(f"user-agent={user_agent}")

    # Prefs
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_settings.popups": 0,
        "profile.managed_default_content_settings.images": 2,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation", "enable-logging"]
    )
    options.add_experimental_option("useAutomationExtension", False)

    # Argumentos CDP
    options.add_argument("--disable-client-side-phishing-detection")

    context.driver = webdriver.Chrome(options=options)
    context.driver.set_page_load_timeout(30)
    # Inyectar scripts anti-detección
    context.driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": """
            Object.defineProperty(navigator, 'webdriver', { get: () => false });
            Object.defineProperty(navigator, 'plugins', { get: () => [1,2,3,4,5] });
            Object.defineProperty(navigator, 'languages', { get: () => ['es-ES'] });
            window.chrome = { runtime: {} };
            Object.defineProperty(navigator, 'permissions', {
                get: () => ({
                    query: () => Promise.resolve({ state: 'granted' })
                })
            });
            """
        },
    )

    context.driver.get("https://www.google.com")
    human_delay(4, 7)


@when('I search for "{query}" on Google')
def step_search_google(context, query):
    """Realiza una búsqueda en Google."""
    wait = WebDriverWait(context.driver, 15)
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    human_delay(1, 2)
    search_box.clear()
    human_delay(0.5, 1)
    search_box.send_keys(query)
    human_delay(2, 4)
    search_box.send_keys(Keys.RETURN)
    wait.until(EC.url_contains("q="))
    human_delay(4, 7)

    # Check si Google detectó bot
    page_text = context.driver.page_source.lower()
    if "sorry" in page_text or "unusual traffic" in page_text:
        print("[ALERT] Google bloqueó acceso - detectó bot")
        raise TimeoutException("Google detectó actividad de bot")


@when('I click the first link matching "{domain}"')
def step_click_first_link(context, domain):
    """Hace clic en el primer enlace que coincide con el dominio."""
    wait = WebDriverWait(context.driver, 20)

    # Intentos múltiples por si Google bloquea
    for attempt in range(3):
        print(f"\n[DEBUG] Intento {attempt + 1}/3 buscando {domain}")

        # Check si Google detectó bot
        page_text = context.driver.page_source.lower()
        if "sorry" in page_text or "unusual traffic" in page_text:
            print("[ALERT] Google bloqueó acceso - detectó bot")
            human_delay(10, 15)
            if attempt < 2:
                context.driver.refresh()
                human_delay(5, 10)
                continue
            raise TimeoutException("Google detectó actividad de bot")

        # Scroll para cargar resultados
        for _ in range(5):
            context.driver.execute_script("window.scrollBy(0, 300);")
            human_delay(1, 2)

        # Espera links
        wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
        human_delay(3, 5)

        # Obtener todos los links
        all_links = context.driver.find_elements(By.TAG_NAME, "a")
        print(f"[DEBUG] Total links encontrados: {len(all_links)}")

        # Debug: mostrar primeros 30 links con href
        for i, link in enumerate(all_links[:30]):
            href = link.get_attribute("href") or ""
            if href.startswith("http"):
                print(f"  [{i}] {href[:100]}")
                if domain in href:
                    print(f"       ✓ MATCH ENCONTRADO para {domain}")

        for link in all_links:
            href = link.get_attribute("href") or ""
            if domain in href and href.startswith("http"):
                try:
                    print(f"[DEBUG] Click en: {href[:80]}")
                    _click_link_and_verify(context.driver, link, domain, wait)
                    context.current_domain = domain
                    return
                except TimeoutException as e:
                    print(f"[DEBUG] Click falló: {e}")
                    continue

        # Si no encontró en este intento y no es último, recarga y reintenta
        if attempt < 2:
            print("[DEBUG] No encontrado. Recargando y reintentando...")
            human_delay(5, 8)
            context.driver.refresh()
            human_delay(4, 6)

    raise TimeoutException(f"No encontrado: {domain}")


@then('I should be on the "{domain}" website')
def step_verify_domain(context, domain):
    """Verifica que la URL actual contenga el dominio esperado."""
    wait = WebDriverWait(context.driver, 15)
    wait.until(EC.url_contains(domain))
    assert domain in context.driver.current_url


@when('I search for "{search_term}" on the university site')
def step_search_on_site(context, search_term):
    """Realiza una búsqueda en el sitio universitario."""
    wait = WebDriverWait(context.driver, 20)
    domain = context.current_domain

    icon_selector = SELECTORS[domain]["icon"]
    input_selector = SELECTORS[domain]["input"]

    # Espera a que página cargue
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    human_delay(1, 2)

    # Espera icon
    try:
        icon = wait.until(EC.element_to_be_clickable(icon_selector))
    except TimeoutException:
        # Fallback: buscar elemento presente primero
        icon = wait.until(EC.presence_of_element_located(icon_selector))

    context.driver.execute_script("arguments[0].scrollIntoView(true);", icon)
    human_delay(0.5, 1)
    click_script = (
        "arguments[0].dispatchEvent(new MouseEvent('click', "
        "{bubbles: true, cancelable: true, view: window}));"
    )
    context.driver.execute_script(click_script, icon)
    human_delay(1, 2)

    search_input = wait.until(EC.element_to_be_clickable(input_selector))
    search_input.clear()
    search_input.send_keys(search_term)

    if domain != "uag.mx":
        search_input.send_keys(Keys.RETURN)
    human_delay(1, 2)


@then('the results should contain "{expected_keyword}"')
def step_verify_results(context, expected_keyword):
    """Verifica que el keyword esté en resultados."""
    wait = WebDriverWait(context.driver, 15)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    human_delay(1, 2)

    body_text = context.driver.execute_script("return document.body.innerText").lower()
    keyword_lower = expected_keyword.lower()

    assert keyword_lower in body_text, f"'{expected_keyword}' no encontrado"

    context.driver.quit()
