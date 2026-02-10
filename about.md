---
layout: page
title: About
---

<div class="about-intro">
  <h1>About Me</h1>
  <p class="about-lead">I'm a technical writer specializing in building complete documentation ecosystems for B2B SaaS companies. I've created 1,200+ articles across two documentation systems built from scratch, achieving 30-40% support ticket reduction through strategic information architecture and developer-facing content.</p>

  <div class="about-meta-inline">
    <span class="meta-item">
      <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
        <circle cx="12" cy="10" r="3"></circle>
      </svg>
      Prague, Czechia
    </span>

    <span class="meta-separator">|</span>
    <span class="meta-item">
      <strong>Languages:</strong> Czech, Vietnamese, English (C2), Japanese (N4), French (B2)
    </span>
  </div>

  <div class="about-intro-cta">
    <a href="{{ '/contact' | relative_url }}" class="btn btn-primary">Contact Me</a>
  </div>
</div>


<nav class="about-nav" id="aboutNav">
  <a href="#experience" class="about-nav-link">Experience</a>
  <a href="#expertise" class="about-nav-link">Expertise</a>
  <a href="#education" class="about-nav-link">Education</a>
</nav>

<h2 id="experience">Professional Experience</h2>

### Documentation Specialist at Dawiso
*April 2024 – Present*

I own and scale end-to-end documentation for a data governance platform with 500+ articles and 40% ticket deflection:

- Designed complete information architecture from zero for the data governance platform
- Created 80+ references and tutorials for JSON package configuration and automation rules
- Delivered documentation for 15+ releases, including comprehensive LTS release notes
- Established documentation standards, style guides, and docs-as-code workflows
- Co-created Dawiso Academy with 10+ educational videos
- Validated 100+ JSON configurations to ensure technical accuracy

### Knowledge Base Manager at Dataddo
*April 2022 – April 2024 | Freelance maintenance: April 2024 – Present*

Built user and developer documentation of 700+ articles with 30% ticket deflection for a SaaS ETL tool:

- Re-built the knowledge base information architecture from the ground up
- Documented 400+ data source connectors with consistent structure
- Created comprehensive integration guides and technical tutorials
- Served as primary documentation partner for Engineering and Product teams
- Advised on documentation scope, structure, and best practices

<h2 id="expertise">Expertise</h2>

<div class="expertise-grid">
  <div class="expertise-card">
    <div class="expertise-icon">
      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
        <polyline points="14 2 14 8 20 8"></polyline>
        <line x1="16" y1="13" x2="8" y2="13"></line>
        <line x1="16" y1="17" x2="8" y2="17"></line>
        <polyline points="10 9 9 9 8 9"></polyline>
      </svg>
    </div>
    <h3>Documentation & Writing</h3>
  
    <div class="skill-level">Developer & API documentation</div>
    <div class="skill-level">Technical tutorials & integration guides</div>
    <div class="skill-level">Information architecture & content modeling</div>
    <div class="skill-level">Documentation strategy, standards & governance</div>
    <div class="skill-level">Release notes & product communication</div>
    
  </div>

  <div class="expertise-card">
    <div class="expertise-icon">
      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="16 18 22 12 16 6"></polyline>
        <polyline points="8 6 2 12 8 18"></polyline>
      </svg>
    </div>
    <h3>Technical Skills</h3>
    <div class="skill-level">
      <strong>Advanced:</strong> Markdown, Docs-as-Code workflows
    </div>
    <div class="skill-level">
      <strong>Intermediate:</strong> Git & version control, HTML & CSS, JSON, Information Architecture
    </div>
    <div class="skill-level">
      <strong>Working knowledge:</strong> JavaScript, SQL, XML, REST APIs, CI/CD pipelines
    </div>
  </div>

  <div class="expertise-card">
    <div class="expertise-icon">
      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
        <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
      </svg>
    </div>
    <h3>Tools & Platforms</h3>
    <div class="tool-category">
      <strong>Documentation:</strong> Document360, Confluence, Notion, SharePoint
    </div>
    <div class="tool-category">
      <strong>Development:</strong> GitHub, GitLab, VS Code, Cursor, Claude Code, Postman
    </div>
    <div class="tool-category">
      <strong>Project Management:</strong> Asana, Jira
    </div>
    <div class="tool-category">
      <strong>Cloud & Data:</strong> Azure Data Studio, Google BigQuery, SQL Server
    </div>
    <div class="tool-category">
      <strong>Design & Media:</strong> Camtasia, Canva, Figma
    </div>
  </div>
</div>

<h2 id="education">Education</h2>

**Master's Degree** — Prague University of Economics and Business
*International Politics and Diplomacy, European Economic Integration*
*September 2018 – January 2022*

**Exchange Semester** — L'Université du Québec à Montréal, Canada
*International Business*
*September 2020 – December 2020*

<script>
document.addEventListener('DOMContentLoaded', function() {
    const nav = document.getElementById('aboutNav');
    const navLinks = nav.querySelectorAll('.about-nav-link');
    const navOffsetTop = nav.offsetTop;

    // Sticky nav on scroll
    window.addEventListener('scroll', function() {
        if (window.pageYOffset >= navOffsetTop) {
            nav.classList.add('sticky');
        } else {
            nav.classList.remove('sticky');
        }
    });

    // Highlight active section
    const sections = Array.from(navLinks).map(link => {
        const id = link.getAttribute('href').substring(1);
        return document.getElementById(id);
    });

    window.addEventListener('scroll', function() {
        let current = '';
        sections.forEach(section => {
            if (section) {
                const sectionTop = section.offsetTop;
                if (window.pageYOffset >= sectionTop - 150) {
                    current = section.getAttribute('id');
                }
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').substring(1) === current) {
                link.classList.add('active');
            }
        });
    });
});
</script>
