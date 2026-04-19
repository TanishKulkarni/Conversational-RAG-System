import { useState } from 'react';
import Sidebar from '../components/Sidebar';
import Chat from './Chat';
import ChatHistory from './ChatHistory';
import Upload from './Upload';
import Admin from './Admin';

const Dashboard = () => {
  const [currentPage, setCurrentPage] = useState('chat');

  const renderPage = () => {
    switch (currentPage) {
      case 'chat':
        return <Chat />;
      case 'chat-history':
        return <ChatHistory />;
      case 'upload':
        return <Upload />;
      case 'admin':
        return <Admin />;
      default:
        return <Chat />;
    }
  };

  return (
    <div className="flex h-screen bg-gray-50">
      <Sidebar currentPage={currentPage} setCurrentPage={setCurrentPage} />
      <main className="flex-1 overflow-hidden">
        {renderPage()}
      </main>
    </div>
  );
};

export default Dashboard;