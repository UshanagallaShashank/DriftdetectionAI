import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Vite configuration with React plugin and dev proxy to backend API
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': 'http://localhost:8000',
    },
  },
})
