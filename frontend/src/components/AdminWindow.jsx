import { useState, useEffect } from "react"
import axios from "axios"

export default function AdminWindow() {
  const [failedQueries, setFailedQueries] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchFailedQueries()
  }, [])

  const fetchFailedQueries = async () => {
    try {
      setLoading(true)
      const response = await axios.get("http://127.0.0.1:8000/admin/failed-queries")
      setFailedQueries(response.data)
      setError(null)
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to fetch failed queries")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="flex flex-col h-full">
      <div className="p-4 border-b">
        <h1 className="text-xl font-bold">Admin Dashboard</h1>
        <p className="text-gray-600">Failed Queries Log</p>
      </div>

      <div className="flex-1 overflow-y-auto p-4">
        {loading && <p>Loading failed queries...</p>}

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            {error}
          </div>
        )}

        {!loading && !error && failedQueries.length === 0 && (
          <p className="text-gray-500">No failed queries found.</p>
        )}

        {!loading && !error && failedQueries.length > 0 && (
          <div className="space-y-4">
            {failedQueries.map((item, index) => (
              <div key={index} className="bg-gray-50 p-4 rounded border">
                <div className="font-mono text-sm">
                  <strong>Query:</strong> {item.question || item.query || "N/A"}
                </div>
                <div className="text-sm text-gray-600 mt-1">
                  <strong>Timestamp:</strong> {item.timestamp || "N/A"}
                </div>
                <div className="text-sm text-red-600 mt-1">
                  <strong>Error:</strong> {item.error || "N/A"}
                </div>
              </div>
            ))}
          </div>
        )}

        <div className="mt-4">
          <button
            onClick={fetchFailedQueries}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Refresh
          </button>
        </div>
      </div>
    </div>
  )
}