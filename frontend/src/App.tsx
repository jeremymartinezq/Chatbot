import React from 'react'
import ChatWidget from './components/ChatWidget'
import { useChatStore } from './store/chatStore'

const App: React.FC = () => {
  const { theme } = useChatStore()

  return (
    <div className={theme}>
      <ChatWidget />
    </div>
  )
}

export default App 