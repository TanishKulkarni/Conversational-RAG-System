import { useState, useEffect } from 'react';
import axios from 'axios';
import { Upload as UploadIcon, FileText, Trash2 } from 'lucide-react';

const API_BASE = 'http://localhost:8000';

const Upload = () => {
  const [documents, setDocuments] = useState([]);
  const [uploading, setUploading] = useState(false);

  useEffect(() => {
    fetchDocuments();
  }, []);

  const fetchDocuments = async () => {
    try {
      const response = await axios.get(`${API_BASE}/admin/documents`);
      setDocuments(response.data);
    } catch (error) {
      console.error('Error fetching documents:', error);
    }
  };

  const handleUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    setUploading(true);
    try {
      await axios.post(`${API_BASE}/admin/upload-doc`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      fetchDocuments(); // Refresh list
      event.target.value = ''; // Reset input
    } catch (error) {
      console.error('Error uploading document:', error);
      alert('Upload failed');
    } finally {
      setUploading(false);
    }
  };

  const deleteDocument = async (fileName) => {
    if (!confirm(`Delete ${fileName}?`)) return;

    try {
      await axios.delete(`${API_BASE}/admin/documents/${fileName}`);
      fetchDocuments();
    } catch (error) {
      console.error('Error deleting document:', error);
      alert('Delete failed');
    }
  };

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  return (
    <div className="h-full p-6">
      <h1 className="text-2xl font-semibold mb-6">Document Management</h1>

      <div className="mb-6">
        <label className="block">
          <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center hover:border-indigo-400 transition-colors duration-200 cursor-pointer">
            <UploadIcon className="w-12 h-12 mx-auto text-gray-400 mb-4" />
            <p className="text-gray-600 mb-2">Click to upload a document</p>
            <p className="text-sm text-gray-500">PDF, TXT, or other text files</p>
            <input
              type="file"
              onChange={handleUpload}
              disabled={uploading}
              className="hidden"
              accept=".pdf,.txt,.doc,.docx"
            />
          </div>
        </label>
        {uploading && <p className="text-center mt-2 text-indigo-600">Uploading...</p>}
      </div>

      <div>
        <h2 className="text-xl font-semibold mb-4">Uploaded Documents</h2>
        {documents.length === 0 ? (
          <p className="text-gray-500">No documents uploaded yet</p>
        ) : (
          <div className="space-y-3">
            {documents.map((doc) => (
              <div key={doc.name} className="flex items-center justify-between p-4 bg-white rounded-lg shadow-sm border border-gray-200">
                <div className="flex items-center">
                  <FileText className="w-5 h-5 text-gray-400 mr-3" />
                  <div>
                    <p className="font-medium text-gray-900">{doc.name}</p>
                    <p className="text-sm text-gray-500">
                      {formatFileSize(doc.size)} • Uploaded {new Date(doc.uploaded_at).toLocaleDateString()}
                    </p>
                  </div>
                </div>
                <button
                  onClick={() => deleteDocument(doc.name)}
                  className="text-red-500 hover:text-red-700 p-2"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Upload;