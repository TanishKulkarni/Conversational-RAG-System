import { useState } from "react"
import MessageBubble from "./MessageBubble"
import TypingIndicator from "./TypingIndicator"
import SourceViewer from "./SourceViewer"
import { sendMessage } from "../services/api"

export default function ChatWindow() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState("")
  const [loading, setLoading] = useState(false)

  const sessionId = "student_demo"

  const handleSend = async () => {
    if (!input) return

    const userMsg = { role: "user", text: input }
    setMessages(prev => [...prev, userMsg])

    setLoading(true)

    const res = await sendMessage(sessionId, input)

    const botMsg = {
      role: "assistant",
      text: res.answer,
      sources: res.citations,
    }

    setMessages(prev => [...prev, botMsg])
    setInput("")
    setLoading(false)
  }

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto p-4">
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
        />
        <button
          onClick={handleSend}
          className="ml-2 bg-blue-600 text-white px-4 rounded"
        >
          Send
        </button>
      </div>
    </div>
  )
}