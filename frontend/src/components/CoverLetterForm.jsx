import React, { useState } from "react";
import axios from "axios";

export default function CoverLetterForm() {
  const [formData, setFormData] = useState({
    name: "",
    role: "",
    company: "",
    experience: "",
    skills: "",
    tone: "corporate",
  });

  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult("");

    try {
    // That matches the backend route from your logs (POST /generate-cover-letter).
      const res = await axios.post("http://127.0.0.1:8000/generate-cover-letter", formData);
      setResult(res.data.cover_letter);
    } catch (error) {
      setResult("Error generating cover letter.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container" style={{ maxWidth: 700, margin: "auto", padding: 20 }}>
      <h2>Cover Letter Generator</h2>
      <form onSubmit={handleSubmit}>
        {["name", "role", "company", "experience", "skills"].map((field) => (
          <div key={field} style={{ marginBottom: 10 }}>
            <label style={{ display: "block", fontWeight: "bold" }}>{field.replace("_", " ")}</label>
            <textarea
              name={field}
              value={formData[field]}
              onChange={handleChange}
              rows={field === "experience" || field === "skills" ? 3 : 1}
              style={{ width: "100%" }}
            />
          </div>
        ))}

        <div style={{ marginBottom: 10 }}>
          <label style={{ display: "block", fontWeight: "bold" }}>Tone</label>
          <select name="tone" value={formData.tone} onChange={handleChange}>
            <option value="corporate">Corporate</option>
            <option value="creative">Creative</option>
            <option value="dynamic">Dynamic</option>
            <option value="education">Education</option>
            <option value="professional">Professional</option>
            <option value="school">School</option>
            <option value="technical">Technical</option>
          </select>
        </div>

        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Generate Cover Letter"}
        </button>
      </form>

      {result && (
        <div style={{ marginTop: 30 }}>
          <h3>Generated Cover Letter:</h3>
          <pre style={{ background: "#f4f4f4", padding: 20, whiteSpace: "pre-wrap" }}>{result}</pre>
        </div>
      )}
    </div>
  );
}
