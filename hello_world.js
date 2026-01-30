/**
 * Módulo de ejemplo: función de bienvenida.
 *
 * Proporciona una función simple que construye un mensaje de bienvenida
 * usando plantillas literales y sigue el formato JSDoc para documentación.
 *
 * @module hello_world
 */

/* eslint-env node */

/**
 * Devuelve un mensaje de bienvenida personalizado.
 *
 * @param {string} name - Nombre de la persona a saludar.
 * @returns {string} Mensaje de bienvenida formateado.
 *
 * Ejemplo de uso:
 * console.log(welcome("Clemente"));
 *
 * @since 2026-01-29
 */
function welcome(name) {
  return `Bienvenido, ${name}, al curso de Pruebas de Software Primavera 2026`;
}

console.log(welcome("Clemente"));
