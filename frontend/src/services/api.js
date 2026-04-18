import axios from "axios"

const API_BASE =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:8000"

export const sendMessage = async (sessionId, message) => {
    const res = await axios.post(`${API_BASE}/chat`, {
        session_id: sessionId,
        message: message,
    })
    return res.data
}

export const uploadDocument = async (file) => {
    const formData = new FormData()
    formData.append("file", file)
    const res = await axios.post(`${API_BASE}/admin/upload-doc`, formData, {
        headers: {
            "Content-Type": "multipart/form-data",
        },
    })
    return res.data
}

export const fetchFailedQueries = async () => {
    const res = await axios.get(`${API_BASE}/admin/failed-queries`)
    return res.data
}