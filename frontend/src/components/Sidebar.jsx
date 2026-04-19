import { MessageCircle, History, Upload, BarChart3 } from 'lucide-react';

const Sidebar = ({ currentPage, setCurrentPage }) => {
  const menuItems = [
    { id: 'chat', label: 'Chat', icon: MessageCircle },
    { id: 'chat-history', label: 'Chat History', icon: History },
    { id: 'upload', label: 'Upload Documents', icon: Upload },
    { id: 'admin', label: 'Admin', icon: BarChart3 },
  ];

  return (
    <div className="w-64 bg-white shadow-lg border-r border-gray-200">
      <div className="p-6">
        <h2 className="text-xl font-semibold text-gray-800">Academic Assistant</h2>
      </div>
      <nav className="mt-6">
        {menuItems.map((item) => {
          const Icon = item.icon;
          return (
            <button
              key={item.id}
              onClick={() => setCurrentPage(item.id)}
              className={`w-full flex items-center px-6 py-3 text-left transition-colors duration-200 ${
                currentPage === item.id
                  ? 'bg-indigo-50 text-indigo-700 border-r-2 border-indigo-700'
                  : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
              }`}
            >
              <Icon className="w-5 h-5 mr-3" />
              {item.label}
            </button>
          );
        })}
      </nav>
    </div>
  );
};

export default Sidebar;