import { useState } from "react"
import Sidebar from "../components/Sidebar"
import ChatWindow from "../components/ChatWindow"
import AdminWindow from "../components/AdminWindow"

export default function ChatPage() {
    const [currentView, setCurrentView] = useState('chat')
    const [messages, setMessages] = useState([])
    const [loading, setLoading] = useState(false)

    const handleViewChange = (view) => {
        setCurrentView(view)
    }

    const handleNewChat = () => {
        setMessages([])
        setLoading(false)
        setCurrentView('chat')
    }

    return (
        <div className="flex h-screen">
            <Sidebar
                onViewChange={handleViewChange}
                currentView={currentView}
                onNewChat={handleNewChat}
            />
            <div className="flex-1">
                {currentView === 'chat' && (
                    <ChatWindow
                        messages={messages}
                        setMessages={setMessages}
                        loading={loading}
                        setLoading={setLoading}
                    />
                )}
                {currentView === 'admin' && <AdminWindow />}
            </div>
        </div>
    )
}