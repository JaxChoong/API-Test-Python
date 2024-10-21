import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // Catch-all proxy rule to forward all unknown routes to the Flask backend
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        secure: false,
        // Rewrite the URL to remove the leading /api prefix
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
})
