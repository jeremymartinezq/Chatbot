import React, { useEffect, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { ChatBubbleLeftRightIcon, XMarkIcon } from '@heroicons/react/24/outline'
import { useChatStore } from '../store/chatStore'
import MessageList from './MessageList'
import MessageInput from './MessageInput'
import ThemeToggle from './ThemeToggle'

const ChatWidget: React.FC = () => {
  const { isOpen, toggleChat, theme } = useChatStore()
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
        toggleChat()
      }
    }

    if (isOpen) {
      document.addEventListener('mousedown', handleClickOutside)
    }

    return () => {
      document.removeEventListener('mousedown', handleClickOutside)
    }
  }, [isOpen, toggleChat])

  return (
    <div className="fixed bottom-4 right-4 z-50">
      <AnimatePresence>
        {isOpen && (
          <motion.div
            ref={containerRef}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 20 }}
            className={`
              mb-4 w-96 rounded-lg shadow-xl
              ${theme === 'dark' ? 'bg-gray-800' : 'bg-white'}
              overflow-hidden
            `}
          >
            {/* Header */}
            <div className={`
              p-4 flex items-center justify-between
              ${theme === 'dark' ? 'bg-gray-900' : 'bg-primary-600'}
              text-white
            `}>
              <h3 className="text-lg font-semibold">CopyCoder Chat</h3>
              <div className="flex items-center space-x-2">
                <ThemeToggle />
                <button
                  onClick={toggleChat}
                  className="p-1 rounded-full hover:bg-white/20 transition-colors"
                >
                  <XMarkIcon className="w-6 h-6" />
                </button>
              </div>
            </div>

            {/* Chat Container */}
            <div className="h-96 flex flex-col">
              <MessageList />
              <MessageInput />
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Toggle Button */}
      <motion.button
        onClick={toggleChat}
        className={`
          p-4 rounded-full shadow-lg
          ${theme === 'dark' ? 'bg-gray-800 text-white' : 'bg-primary-600 text-white'}
          hover:shadow-xl transition-shadow
        `}
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
      >
        <ChatBubbleLeftRightIcon className="w-6 h-6" />
      </motion.button>
    </div>
  )
}

export default ChatWidget 