import UploadPanel from "./UploadPanel"
import FailedQueries from "./FailedQueries"

export default function AdminPage() {
    return (
        <div className="p-6 space-y-6">
            <h1 className="text-2xl font-bold">
                Admin Dashboard
            </h1>

            <UploadPanel />
            <FailedQueries />
        </div> 
    )
}