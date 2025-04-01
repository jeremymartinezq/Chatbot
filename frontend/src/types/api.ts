export interface Message {
  content: string;
  role: 'user' | 'assistant';
  id?: string;
  timestamp?: string;
}

export interface ChatResponse {
  response: string;
  error?: string;
}

export interface FeedbackRequest {
  message_id: string;
  rating: number;
  comment?: string;
}

export interface Config {
  theme: 'light' | 'dark';
  welcome_message: string;
  chatbot_name: string;
}

export interface ApiError {
  detail: string;
  status_code: number;
}

export interface ChatState {
  messages: Message[];
  isLoading: boolean;
  error: string | null;
  config: Config | null;
} 