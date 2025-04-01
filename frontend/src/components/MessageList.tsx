import React, { useEffect, useRef } from 'react'
import { motion } from 'framer-motion'
import { useChatStore } from '../store/chatStore'

const MessageList: React.FC = () => {
  const { messages, theme } = useChatStore()
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  return (
    <div className={`
      flex-1 overflow-y-auto p-4 space-y-4
      ${theme === 'dark' ? 'bg-gray-800' : 'bg-gray-50'}
    `}>
      {messages.map((message) => (
        <motion.div
          key={message.id}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className={`
            flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}
          `}
        >
          <div
            className={`
              max-w-[80%] p-3 rounded-lg
              ${message.role === 'user'
                ? theme === 'dark'
                  ? 'bg-primary-600 text-white'
                  : 'bg-primary-500 text-white'
                : theme === 'dark'
                ? 'bg-gray-700 text-white'
                : 'bg-white text-gray-900'
              }
              ${message.role === 'user' ? 'rounded-br-none' : 'rounded-bl-none'}
            `}
          >
            <p className="text-sm">{message.content}</p>
            <span className={`
              text-xs mt-1 block
              ${message.role === 'user'
                ? 'text-primary-100'
                : theme === 'dark'
                ? 'text-gray-400'
                : 'text-gray-500'
              }
            `}>
              {new Date(message.timestamp).toLocaleTimeString()}
            </span>
          </div>
        </motion.div>
      ))}
      <div ref={messagesEndRef} />
    </div>
  )
}

export default MessageList 