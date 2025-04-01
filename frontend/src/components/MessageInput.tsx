import React, { useState, useRef, useEffect } from 'react'
import { PaperAirplaneIcon } from '@heroicons/react/24/solid'
import { useChatStore } from '../store/chatStore'

const MessageInput: React.FC = () => {
  const [message, setMessage] = useState('')
  const { addMessage, setLoading, isLoading, theme } = useChatStore()
  const inputRef = useRef<HTMLTextAreaElement>(null)

  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.style.height = 'auto'
      inputRef.current.style.height = `${inputRef.current.scrollHeight}px`
    }
  }, [message])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!message.trim() || isLoading) return

    try {
      setLoading(true)
      addMessage(message, 'user')

      // Send message to backend
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: message }),
      })

      const data = await response.json()
      addMessage(data.response, 'assistant')
    } catch (error) {
      addMessage('Sorry, I encountered an error. Please try again.', 'assistant')
    } finally {
      setLoading(false)
      setMessage('')
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSubmit(e)
    }
  }

  return (
    <form
      onSubmit={handleSubmit}
      className={`
        p-4 border-t
        ${theme === 'dark'
          ? 'bg-gray-800 border-gray-700'
          : 'bg-white border-gray-200'
        }
      `}
    >
      <div className="flex items-end space-x-2">
        <textarea
          ref={inputRef}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
          rows={1}
          className={`
            flex-1 p-2 rounded-lg resize-none
            focus:outline-none focus:ring-2 focus:ring-primary-500
            ${theme === 'dark'
              ? 'bg-gray-700 text-white placeholder-gray-400 border-gray-600'
              : 'bg-gray-100 text-gray-900 placeholder-gray-500 border-gray-300'
            }
          `}
          style={{
            minHeight: '40px',
            maxHeight: '120px',
          }}
        />
        <button
          type="submit"
          disabled={!message.trim() || isLoading}
          className={`
            p-2 rounded-lg transition-colors
            ${!message.trim() || isLoading
              ? 'opacity-50 cursor-not-allowed'
              : 'hover:bg-primary-600'
            }
            ${theme === 'dark'
              ? 'bg-primary-500 text-white'
              : 'bg-primary-500 text-white'
            }
          `}
        >
          <PaperAirplaneIcon className="w-5 h-5" />
        </button>
      </div>
    </form>
  )
}

export default MessageInput 