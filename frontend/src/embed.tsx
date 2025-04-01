import React from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'
import './index.css'

interface CopyCoderConfig {
  theme?: 'light' | 'dark'
  position?: 'bottom-right' | 'bottom-left'
  welcomeMessage?: string
}

class CopyCoder {
  private config: CopyCoderConfig = {}
  private container: HTMLElement | null = null

  init(config: CopyCoderConfig = {}) {
    this.config = config

    // Create container
    this.container = document.createElement('div')
    this.container.id = 'copycoder-container'
    document.body.appendChild(this.container)

    // Initialize React
    const root = createRoot(this.container)
    root.render(
      <React.StrictMode>
        <App />
      </React.StrictMode>
    )
  }
}

// Create global instance
declare global {
  interface Window {
    CopyCoder: CopyCoder
  }
}

window.CopyCoder = new CopyCoder()

export default CopyCoder 