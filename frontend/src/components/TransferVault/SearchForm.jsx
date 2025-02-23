import React, { useState } from "react";
import styles from "./TransferVault.module.css";

function SearchForm({ onSearch }) {
  const [inputValue, setInputValue] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(inputValue);
  };

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  return (
    <form className={styles.inputContainer} onSubmit={handleSubmit}>
      <label htmlFor="playerInput" className={styles["visually-hidden"]}>
        Enter player name
      </label>
      <input
        type="text"
        id="playerInput"
        className={styles.inputField}
        aria-label="Enter player name"
        value={inputValue}
        onChange={handleInputChange}
      />
      <button className={styles.searchButton} type="submit">
        SEARCH
      </button>
    </form>
  );
}

export default SearchForm;
