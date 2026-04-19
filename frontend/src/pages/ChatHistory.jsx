import { useState, useEffect } from 'react';
import axios from 'axios';
import { History, MessageCircle } from 'lucide-react';

const API_BASE = 'http://localhost:8000';

const ChatHistory = () => {
  const [sessions, setSessions] = useState([]);
  const [selectedSession, setSelectedSession] = useState(null);
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const storedSessions = JSON.parse(localStorage.getItem('sessions') || '[]');
    setSessions(storedSessions);
  }, []);

  const loadHistory = async (sessionId) => {
    try {
      const response = await axios.get(`${API_BASE}/session/${sessionId}`);
      const sessionHistory = Array.isArray(response.data.history)
        ? response.data.history
        : response.data.history || [];
      setHistory(sessionHistory);
      setSelectedSession(sessionId);
    } catch (error) {
      console.error('Error loading history:', error);
      setHistory([]);
    }
  };

  return (
    <div className="h-full flex flex-col lg:flex-row">
      <div className="lg:w-1/3 border-r border-gray-200 p-4 bg-slate-50">
        <h2 className="text-xl font-semibold mb-4 flex items-center">
          <History className="w-5 h-5 mr-2" />
          Chat Sessions
        </h2>
        <div className="space-y-2">
          {sessions.map((sessionId) => (
            <button
              key={sessionId}
              onClick={() => loadHistory(sessionId)}
              className={`w-full text-left p-3 rounded-lg transition-colors duration-200 ${
                selectedSession === sessionId ? 'bg-indigo-50 text-indigo-700' : 'hover:bg-gray-50'
              }`}
            >
              <div className="flex items-center">
                <MessageCircle className="w-4 h-4 mr-2" />
                <span className="text-sm truncate">{String(sessionId).slice(0, 8)}...</span>
              </div>
            </button>
          ))}
          {sessions.length === 0 && (
            <p className="text-gray-500 text-center">No chat sessions yet</p>
          )}
        </div>
      </div>
      <div className="flex-1 p-4">
        <h2 className="text-xl font-semibold mb-4">Chat History</h2>
        {selectedSession ? (
          <div className="space-y-4">
            {history.length > 0 ? (
              history.map((msg, index) => {
                const content = typeof msg === 'string' ? msg : msg.content || JSON.stringify(msg);
                return (
                  <div key={index} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                    <div className={`p-3 rounded-lg max-w-md ${msg.role === 'user' ? 'bg-indigo-600 text-white' : 'bg-gray-100 text-gray-800'}`}>
                      {content}
                    </div>
                  </div>
                );
              })
            ) : (
              <p className="text-gray-500">No messages in this session</p>
            )}
          </div>
        ) : (
          <p className="text-gray-500">Select a session to view history</p>
        )}
      </div>
    </div>
  );
};

export default ChatHistory;