---
layout: case-study
title: "Building a Documentation System from Zero"
description: "Designing and implementing a complete documentation ecosystem for a data governance platform, starting with no existing structure or standards."
company: "Dawiso"
date: 2024-04-01
metrics:
  - value: "500+"
    label: "Articles Created"
  - value: "40%"
    label: "Ticket Deflection"
  - value: "80+"
    label: "Developer Tutorials"
link: "https://help.dawiso.com"
---

## The Challenge

When I joined Dawiso as Documentation Specialist in April 2024, my initial task was to manage and expand the existing documentation. After evaluating both the product and documentation structure, I identified a need for comprehensive restructuring rather than incremental updates.

The existing knowledge was distributed across outdated articles, Slack conversations, and JIRA tickets. This was valuable information, but difficult to access for new users or those seeking quick answers. The documentation lacked a cohesive structure that could effectively serve its diverse audience.

The platform itself presented additional complexity. As a data governance tool with extensive JSON-based configuration packages, it required clear explanation of both abstract concepts and technical implementation. Data governance spans multiple use cases and workflows, making it essential to establish a clear foundation before documenting specific features.

## Establishing the Foundation

I began by using the platform from a user's perspective, documenting my interactions: interface elements, actions, objectives, and decision points. This hands-on approach informed the structure and content priorities for the initial user documentation.

Parallel to this, I conducted interviews with subject matter experts to understand client use cases and pain points. These conversations revealed three primary user groups with distinct needs: developers implementing JSON configurations, business users managing governance workflows, and administrators maintaining platform infrastructure.

## Technical Validation: JSON Configuration Packages

JSON configuration packages represented the most significant technical challenge. With numerous configuration options and specific compatibility requirements, these packages required thorough understanding to document effectively.

The standard approach of modifying existing packages proved effective for experienced users but created obstacles for those new to the system. Identifying errors in unfamiliar code structures consumed significant time without building foundational knowledge.

I shifted to a systematic approach: understanding each property's function, testing configurations methodically, and validating behavior. This process, while initially slower, enabled me to create tutorials that guided users from first principles rather than requiring them to work backward from complex examples.

The validation process covered 100+ JSON configurations, each contributing to a comprehensive understanding of the system's architecture and capabilities.

## Information Architecture Design

With product knowledge established, I designed the documentation's information architecture using Figma and FigJam to map content relationships and hierarchies. The structure prioritized intuitive navigation and logical content grouping while minimizing fragmentation.

I applied the Diátaxis framework as a guiding principle, organizing content into tutorials, how-to guides, reference materials, and resources. This structure ensures each content type serves its intended purpose and audience need.

## Documentation Workflow Development

Prior to my arrival, no formal process existed for tracking documentation needs or status. Development tickets reached completion without documentation verification, creating gaps and making it difficult to identify what required documentation.

I designed and led implementation of an integrated documentation workflow that connected development and documentation processes. The workflow operates as follows:

1. Development tickets include final stage classification: user documentation, developer documentation, or release notes
2. When developers mark tickets as complete, I review and transition them to "Done and Documented"
3. Tickets automatically create corresponding items in the documentation JIRA, progressing through the documentation lifecycle to publication
4. All stakeholders have visibility into documentation status for each feature

This workflow established accountability, eliminated documentation gaps, and provided clear communication channels between development and documentation teams.

## Cross-Functional Collaboration

Documentation development involved close collaboration with product management, engineering, and customer support teams. Product and engineering provided technical insights and feature walkthroughs. Customer support identified recurring user issues, informing documentation priorities.

To accommodate team bandwidth constraints, I adapted communication approaches to individual preferences, whether Slack messages, brief calls, or asynchronous JIRA reviews. The most effective workflow involved independent feature exploration and draft creation, followed by focused review requests. This approach minimized the time required from stakeholders while ensuring technical accuracy.

## Impact

Post-launch monitoring revealed that approximately every second customer ticket could be resolved by providing documentation links, achieving **40% ticket deflection**. This represented a significant improvement over baseline metrics, attributed to the comprehensive restructuring and systematic approach to content creation.

The documentation enabled developers to implement JSON configurations and automation rules independently, reducing support dependencies. Internal teams adopted the documentation as a primary resource for assisting clients and partners, creating a knowledge-sharing foundation that extended beyond direct customer interactions.

## Dawiso Academy: Video Learning Content

In parallel with written documentation, leadership initiated Dawiso Academy, a video-based learning platform. I developed the syllabus and scripts, and when no other team members were available to present, took on the presentation role. This was a new challenge that required video production and presentation skills.

The project produced 10+ educational videos covering key platform features and established a sustainable production workflow for future content.

For more information, see the [Dawiso Academy Case Study](/case_studies/dawiso-academy).

## Key Insights

|Key Insight| Description|
|---|---|
|**Product understanding precedes documentation.**|Effective documentation requires comprehensive product knowledge and consideration of how content integrates within the broader information ecosystem and user workflows.|
|**Collaboration efficiency matters.**|Reducing stakeholder time investment through independent exploration and focused review requests accelerates documentation development while maintaining technical accuracy.|
|**Technical validation ensures user trust.**|Testing configurations before documentation prevents user frustration and establishes documentation credibility.|
|**Format diversity serves different learning styles.**|Combining written documentation with video content accommodates varied user preferences and learning contexts.|

## Technologies & Tools

- **Documentation Platform:** Dawiso Documentation Application
- **Source Control:** Git, GitHub
- **Content Format:** Markdown, HTML, JSON, SQL
- **Screenshots:** Figma, FigJam
- **Collaboration:** Jira, Confluence, Slack


[View Live Documentation →](https://help.dawiso.com){:target="_blank" rel="noopener noreferrer" class="btn btn-primary"}
