import { defineConfig } from 'vite';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('.', import.meta.url));

// Project site is served at https://<user>.github.io/computer-architecture-lab/
// In CI we set VITE_BASE=/computer-architecture-lab/ ; local dev uses '/'.
export default defineConfig({
  base: process.env.VITE_BASE ?? '/',
  build: {
    target: 'es2020',
    outDir: 'dist',
    rollupOptions: {
      input: {
        home: resolve(root, 'index.html'),
        tomasulo: resolve(root, 'tomasulo.html'),
        predictores: resolve(root, 'predictores.html'),
        cache: resolve(root, 'cache.html'),
      },
    },
  },
});
