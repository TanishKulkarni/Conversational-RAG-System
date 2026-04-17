import { useState, useEffect } from "react"
import { fetchFailedQueries as fetchFailedQueriesApi, uploadDocument } from "../services/api"

export default function AdminWindow() {
  const [failedQueries, setFailedQueries] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [uploading, setUploading] = useState(false)
  const [uploadMessage, setUploadMessage] = useState("")

  useEffect(() => {
    loadFailedQueries()
  }, [])

  const loadFailedQueries = async () => {
    try {
      setLoading(true)
      const data = await fetchFailedQueriesApi()
      setFailedQueries(data)
      setError(null)
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to fetch failed queries")
    } finally {
      setLoading(false)
    }
  }

  const handleUpload = async (e) => {
    const file = e.target.files?.[0]
    if (!file) return

    try {
      setUploading(true)
      setUploadMessage("")
      const result = await uploadDocument(file)
      setUploadMessage(`Uploaded: ${result.filename}`)
    } catch (err) {
      setUploadMessage(err.response?.data?.detail || "Upload failed")
    } finally {
      setUploading(false)
      e.target.value = ""
    }
  }

  return (
    <div className="flex flex-col h-full">
      <div className="p-4 border-b">
        <h1 className="text-xl font-bold">Admin Dashboard</h1>
        <p className="text-gray-600">Upload policies and review failed queries</p>
      </div>

      <div className="flex-1 overflow-y-auto p-4">
        <div className="bg-white p-4 rounded border mb-4">
          <h2 className="font-semibold mb-2">Upload New Policy</h2>
          <input
            type="file"
            onChange={handleUpload}
            disabled={uploading}
            className="block w-full text-sm"
          />
          {uploading && <p className="text-sm text-gray-500 mt-2">Uploading and indexing document...</p>}
          {uploadMessage && <p className="text-sm mt-2">{uploadMessage}</p>}
        </div>

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
            onClick={loadFailedQueries}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Refresh
          </button>
        </div>
      </div>
    </div>
  )
}