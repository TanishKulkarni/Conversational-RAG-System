export default function SourceViewer({ sources }) {
    if (!sources || sources.length === 0) return null

    return (
        <div className="mt-2 text-sm text-gray-600">
            <b>Sources:</b>
            <ul>
                {sources.map((s, i) => (
                    <li key={i}>
                        {s.document_name} - {s.section_title}
                    </li>
                ))}
            </ul>
        </div>
    )
}