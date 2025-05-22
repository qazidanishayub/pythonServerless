## 💻 Frontend Setup (Vercel)

1. Deploy `/frontend` as a Next.js app to Vercel.
2. In your `index.tsx` or wherever you fetch the post:
   ```ts
   fetch("https://your-render-api-url.onrender.com/generate", { ... })
   ```
3. Add environment variable `GEMINI_API_KEY` to Vercel (optional if you proxy request)

---

## 📄 Tech Stack

- FastAPI
- Google GenerativeAI (`gemini-1.5-pro-001`)
- Next.js (React 18+)
- Tailwind (optional for UI)
- Render (backend)
- Vercel (frontend)

---

## 📬 Contact

Built by Qazi Danish  
For technical support or questions, message on [LinkedIn](https://www.linkedin.com).
