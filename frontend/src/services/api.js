import axios from "axios"

const API_BASE = "http://127.0.0.1:8000"

export const sendMessage = async (sessionId, message) => {
    const res = await axios.post(`${API_BASE}/chat`, {
        session_id: sessionId,
        message: message,
    })
    return res.data
}