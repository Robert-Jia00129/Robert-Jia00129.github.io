import React from 'react';
import './Footer.css';

const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <p>&copy; 2024 Robert Jia. All rights reserved.</p>
      <div className="footer-links">
        <a href="https://www.linkedin.com/in/robertjia/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        <a href="https://github.com/robertjia" target="_blank" rel="noopener noreferrer">GitHub</a>
      </div>
    </footer>
  );
}

export default Footer;
