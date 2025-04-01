import React from 'react'
import { SunIcon, MoonIcon } from '@heroicons/react/24/outline'
import { useChatStore } from '../store/chatStore'

const ThemeToggle: React.FC = () => {
  const { theme, toggleTheme } = useChatStore()

  return (
    <button
      onClick={toggleTheme}
      className="p-1 rounded-full hover:bg-white/20 transition-colors"
      aria-label="Toggle theme"
    >
      {theme === 'dark' ? (
        <SunIcon className="w-6 h-6" />
      ) : (
        <MoonIcon className="w-6 h-6" />
      )}
    </button>
  )
}

export default ThemeToggle
