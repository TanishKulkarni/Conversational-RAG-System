import { useEffect, useState } from "react"
import axios from "axios"

export default function FailedQueries() {

  const [queries, setQueries] = useState([])

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/admin/failed-queries")
      .then(res => setQueries(res.data))
  }, [])

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="font-bold mb-2">
        Unanswered Questions
      </h2>

      <ul>
        {queries.map((q, i) => (
          <li key={i} className="border-b py-1">
            {q.question} — {q.timestamp}
          </li>
        ))}
      </ul>
    </div>
  )
}