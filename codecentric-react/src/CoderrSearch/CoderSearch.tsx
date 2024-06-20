import React, { useState } from "react";
import { findFirstCoderByLanguageInRepos } from "./CoderUtils";

export const CoderSearch = () => {
  const [language, setLanguage] = useState("");
  const [coder, setCoder] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const foundCoder = await findFirstCoderByLanguageInRepos(language);
    setCoder(foundCoder);
    console.log("Coder", foundCoder);
  };

  return (
    <div>
      <h1>Find Coder by Language</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
        />
        <button type="submit">Search</button>
      </form>
      {coder && <p>Coder found: {coder}</p>}
      {coder === null && <p>No coder found with the specified language.</p>}
    </div>
  );
};
