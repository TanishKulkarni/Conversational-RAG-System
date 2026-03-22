import { motion } from "framer-motion"

export default function MessageBubble({ role, text }) {
    const isUser = role === "user"

    return (
        <motion.div
           initial={{ opacity: 0, y: 10 }}
           animate={{ opacity: 1, y: 0 }}
           className={`max-w-lg p-3 rounded-xl mb-2 ${
             isUser
                ? "bg-blue-500 text-white ml-auto"
                : "bg-gray-200 text-black"
           }`}
        >
            {text}
        </motion.div>
    )
}