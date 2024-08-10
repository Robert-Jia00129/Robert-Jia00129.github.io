// src/App.tsx
import React from 'react';
import './App.css';

const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <nav>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About Me</a></li>
            <li><a href="/portfolio">Portfolio</a></li>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>
        </nav>
      </header>
      <main>
        <section className="hero">
          <h1>Welcome to My Personal Website</h1>
          <p>Hi, I'm Robert Jia, a computer science student at UMN.</p>
          <img src="images/profile.jpg" alt="Robert Jia"/>
        </section>
        <section className="featured-projects">
          <h2>Featured Projects</h2>
          {/* Add your featured projects here */}
        </section>
      </main>
      <footer>
        <p>Follow me on social media: [links]</p>
        <p>Contact: [contact information]</p>
      </footer>
    </div>
  );
}

export default App;
