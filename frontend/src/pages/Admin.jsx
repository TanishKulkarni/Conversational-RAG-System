import { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { AlertTriangle, TrendingUp } from 'lucide-react';

const API_BASE = 'http://localhost:8000';

const Admin = () => {
  const [failedQueries, setFailedQueries] = useState([]);
  const [analytics, setAnalytics] = useState([]);

  useEffect(() => {
    fetchFailedQueries();
    // Mock analytics data
    setAnalytics([
      { name: 'Mon', queries: 12 },
      { name: 'Tue', queries: 19 },
      { name: 'Wed', queries: 15 },
      { name: 'Thu', queries: 25 },
      { name: 'Fri', queries: 22 },
      { name: 'Sat', queries: 8 },
      { name: 'Sun', queries: 5 },
    ]);
  }, []);

  const fetchFailedQueries = async () => {
    try {
      const response = await axios.get(`${API_BASE}/admin/failed-queries`);
      setFailedQueries(response.data);
    } catch (error) {
      console.error('Error fetching failed queries:', error);
    }
  };

  return (
    <div className="h-full p-6 overflow-y-auto">
      <h1 className="text-2xl font-semibold mb-6">Admin Dashboard</h1>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h2 className="text-lg font-semibold mb-4 flex items-center">
            <TrendingUp className="w-5 h-5 mr-2 text-indigo-600" />
            Query Analytics
          </h2>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={analytics}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="queries" fill="#4f46e5" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h2 className="text-lg font-semibold mb-4 flex items-center">
            <AlertTriangle className="w-5 h-5 mr-2 text-red-600" />
            Failed Queries
          </h2>
          <div className="space-y-2 max-h-64 overflow-y-auto">
            {failedQueries.length === 0 ? (
              <p className="text-gray-500">No failed queries</p>
            ) : (
              failedQueries.map((query, index) => {
              const questionText = typeof query === 'string'
                ? query
                : query.question || query.query || JSON.stringify(query);
              return (
                <div key={index} className="p-3 bg-red-50 rounded border border-red-200">
                  <p className="text-sm text-red-800">{questionText}</p>
                  <p className="text-xs text-red-600 mt-1">
                    {query.timestamp ? new Date(query.timestamp).toLocaleString() : 'Recent'}
                  </p>
                </div>
              );
            })
            )}
          </div>
        </div>
      </div>

      <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <h2 className="text-lg font-semibold mb-4">Frequently Asked Queries</h2>
        <p className="text-gray-500">Feature coming soon - will show most common queries</p>
      </div>
    </div>
  );
};

export default Admin;