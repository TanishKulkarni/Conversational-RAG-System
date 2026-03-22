import axios from "axios"

export default function UploadPanel() {
    const handleUpload = async (e) => {
        const file = e.target.files[0]

        const formData = new FormData()
        formData.append("file", file)

        await axios.post(
            "http://127.0.0.1:8000/admin/upload-doc",
            formData
        )

        alert("Document uploaded successfully")
    }

    return (
        <div className="bg-white p-4 rounded shadow">
            <h2 className="font-bold mb-2">
                Upload New Policy
            </h2>

            <input type="file" onChange={handleUpload} />   
        </div>
    )
}