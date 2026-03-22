export default function Sidebar({ onViewChange, currentView, onNewChat }) {
    return (
        <div className="w-64 bg-gray-900 text-white p-4">
            <h2 className="text-lg font-bold mb-4">
                Policy Assistant
            </h2>

            <div className="space-y-2">
                <button
                    onClick={onNewChat}
                    className="w-full p-2 rounded bg-green-600 hover:bg-green-700 text-left"
                >
                    + New Chat
                </button>

                <button
                    onClick={() => onViewChange('chat')}
                    className={`w-full p-2 rounded text-left ${
                        currentView === 'chat' ? 'bg-blue-600' : 'bg-gray-700 hover:bg-gray-600'
                    }`}
                >
                    💬 Chat
                </button>

                <button
                    onClick={() => onViewChange('admin')}
                    className={`w-full p-2 rounded text-left ${
                        currentView === 'admin' ? 'bg-blue-600' : 'bg-gray-700 hover:bg-gray-600'
                    }`}
                >
                    ⚙️ Admin
                </button>
            </div>
        </div>
    )
}