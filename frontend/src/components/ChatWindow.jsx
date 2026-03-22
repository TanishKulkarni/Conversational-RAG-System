import { useState } from "react"
import MessageBubble from "./MessageBubble"
import TypingIndicator from "./TypingIndicator"
import SourceViewer from "./SourceViewer"
import { sendMessage } from "../services/api"

export default function ChatWindow({ messages, setMessages, loading, setLoading }) {
  const [input, setInput] = useState("")

  const sessionId = "student_demo"

  const handleSend = async () => {
    if (!input) return

    const userMsg = { role: "user", text: input }
    setMessages(prev => [...prev, userMsg])

    setLoading(true)

    try {
      const res = await sendMessage(sessionId, input)

      const botMsg = {
        role: "assistant",
        text: res.answer,
        sources: res.citations,
      }

      setMessages(prev => [...prev, botMsg])
    } catch (error) {
      console.error("Error sending message:", error)
      const errorMsg = {
        role: "assistant",
        text: "Sorry, I encountered an error. Please try again.",
      }
      setMessages(prev => [...prev, errorMsg])
    } finally {
      setInput("")
      setLoading(false)
    }
  }

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto p-4">
        {messages.length === 0 && (
          <div className="text-center text-gray-500 mt-8">
            <h3 className="text-lg font-medium mb-2">Welcome to Policy Assistant</h3>
            <p>Ask me anything about university policies, regulations, and procedures.</p>
          </div>
        )}
        {messages.map((m, i) => (
          <div key={i}>
            <MessageBubble role={m.role} text={m.text} />
            {m.sources && <SourceViewer sources={m.sources} />}
          </div>
        ))}
        {loading && <TypingIndicator />}
      </div>

      <div className="p-3 border-t flex">
        <input
          className="flex-1 border rounded p-2"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Ask about university policies..."
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
        />
        <button
          onClick={handleSend}
          disabled={loading || !input.trim()}
          className="ml-2 bg-blue-600 text-white px-4 rounded disabled:bg-gray-400"
        >
          Send
        </button>
      </div>
    </div>
  )
}