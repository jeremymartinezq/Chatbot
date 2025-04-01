import { create } from 'zustand'

export interface Message {
  id: string
  content: string
  role: 'user' | 'assistant'
  timestamp: Date
}

interface ChatState {
  messages: Message[]
  isOpen: boolean
  isLoading: boolean
  theme: 'light' | 'dark'
  addMessage: (content: string, role: 'user' | 'assistant') => void
  toggleChat: () => void
  setLoading: (loading: boolean) => void
  toggleTheme: () => void
  clearMessages: () => void
}

export const useChatStore = create<ChatState>((set) => ({
  messages: [],
  isOpen: false,
  isLoading: false,
  theme: 'light',
  addMessage: (content, role) =>
    set((state) => ({
      messages: [
        ...state.messages,
        {
          id: Math.random().toString(36).substring(7),
          content,
          role,
          timestamp: new Date(),
        },
      ],
    })),
  toggleChat: () => set((state) => ({ isOpen: !state.isOpen })),
  setLoading: (loading) => set({ isLoading: loading }),
  toggleTheme: () =>
    set((state) => ({ theme: state.theme === 'light' ? 'dark' : 'light' })),
  clearMessages: () => set({ messages: [] }),
})) 