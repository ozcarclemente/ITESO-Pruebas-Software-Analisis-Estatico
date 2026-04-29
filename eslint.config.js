const js = require("@eslint/js");

module.exports = [
  {
    ignores: ["node_modules/", "venv/", "htmlcov/", ".venv/", "dist/", "build/", "coverage/"],
  },
  js.configs.recommended,
  {
    languageOptions: {
      globals: {
        console: "readonly",
        module: "readonly",
        exports: "readonly",
        require: "readonly",
        __dirname: "readonly",
        __filename: "readonly",
        process: "readonly",
        Buffer: "readonly",
        global: "readonly",
        setTimeout: "readonly",
        setInterval: "readonly",
        clearTimeout: "readonly",
        clearInterval: "readonly",
        navigator: "readonly",
      },
    },
  },
];
