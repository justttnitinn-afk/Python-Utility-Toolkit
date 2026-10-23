export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        midnight: '#07111f',
        navy: '#0d1b2a',
        slateblue: '#6d7cff',
        electric: '#58a6ff',
        violet: '#8b5cf6',
        pearl: '#edf4ff'
      },
      boxShadow: {
        soft: '0 24px 60px rgba(15, 23, 42, 0.16)',
        glow: '0 0 0 1px rgba(120, 140, 255, 0.25), 0 30px 60px rgba(88, 166, 255, 0.2)'
      },
      borderRadius: {
        '4xl': '2rem'
      }
    }
  },
  plugins: []
}
