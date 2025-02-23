import React, { useState } from "react";
import styles from "./TransferVault.module.css";
import SearchForm from "./SearchForm";
import BackgroundImage from "./BackgroundImage";
import Title from "./Title";
import Subtitle from "./Subtitle";

function TransferVault() {
  const [searchQuery, setSearchQuery] = useState("");

  const handleSearch = (query) => {
    setSearchQuery(query);
  };

  return (
    <main className={styles.container}>
      <div className={styles.content}>
        <BackgroundImage />
        <Title />
        <Subtitle />
        <SearchForm onSearch={handleSearch} />
      </div>
    </main>
  );
}

export default TransferVault;
