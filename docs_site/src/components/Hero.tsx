import React from 'react';
import styles from './Hero.module.css';

interface HeroProps {
  title: React.ReactNode;
  subtitle: string;
  children: React.ReactNode;
}

export default function Hero({ title, subtitle, children }: HeroProps) {
  return (
    <header className={styles.heroBanner}>
      <div className={styles.container}>
        <h1 className={styles.heroTitle}>{title}</h1>
        <p className={styles.heroSubtitle}>{subtitle}</p>
        <div className={styles.buttons}>{children}</div>
      </div>
    </header>
  );
}