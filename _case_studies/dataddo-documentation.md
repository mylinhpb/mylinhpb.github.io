---
layout: case-study
title: "Scaling Documentation for 400+ Data Connectors"
description: "Rebuilding information architecture and establishing content patterns to document hundreds of data sources for a SaaS ETL platform."
company: "Dataddo"
date: 2022-04-01
metrics:
  - value: "700+"
    label: "Articles Created"
  - value: "30%"
    label: "Ticket Reduction"
  - value: "400+"
    label: "Connectors Documented"
link: "https://docs.dataddo.com"
---

## The Challenge

When I joined Dataddo as Knowledge Base Manager in April 2022, the documentation required significant restructuring. Content gaps and outdated information had accumulated as the platform evolved, and the existing information architecture made navigation difficult for both users and internal teams.

The fragmentation manifested in specific ways. For example, sync frequency information appeared across multiple locations (FAQ, source creation guides, and troubleshooting articles) with inconsistent or contradictory details. Similar patterns affected other topics, where information was distributed across disconnected articles without clear linking or hierarchy.

The navigation structure reflected organic growth rather than intentional design. The FAQ had become a repository for various topics, many of which warranted dedicated articles. Content organization lacked clear categorization principles, making information retrieval challenging even for internal Solutions teams familiar with the platform.

As my first technical writing role, this project required learning documentation principles while implementing solutions. The structural issues were evident, and the need for systematic reorganization was clear.

## Information Architecture Approach

Research into information architecture principles and frameworks, particularly Diátaxis, provided the foundation for restructuring. Effective documentation IA requires:

| Requirement | Description |
| ---|---|
| **Task-based organization** | Organization based on tasks and concepts helps the documentation be more intuitive. | 
| **Shallow, predictable navigation**| Navigation must allow users to find information within minimal clicks. | 
| **Clear content type separation** | Each piece of content must have a main purpose, e.g., references need to be different from resources. | 

These principles guided the complete knowledge base restructuring.

## Scaling Connector Documentation

Dataddo's SaaS ETL platform includes 400+ data source connectors, requiring systematic prioritization and standardization.

Prioritization followed usage statistics. This meant documenting high-traffic connectors first, then focusing on connectors with strategic customer acquisition potential.

Initial connector documentation led to the development of templates. Once standardized templates and reusable snippets were established, documentation time decreased from several hours to 5 minutes for straightforward connectors. Complex connectors with custom authorization or unique configuration requirements continued to require comprehensive testing and detailed documentation.

## Cross-Functional Partnership

The documentation role expanded beyond content creation to strategic partnership across teams. Developers and product managers consulted on feature documentation and content development. Solutions teams used the documentation as their primary information resource. Release notes became the organization's single source of truth for feature tracking and product updates.

One significant collaboration involved aligning with Marketing on content strategy. Marketing sought benefit-focused, engaging language similar to marketing materials. Technical documentation, however, serves users seeking rapid problem resolution rather than product evaluation.

Resolution came through content type clarification. Marketing's objectives aligned with technical blog posts and educational tutorials, in other words, content that combines technical information with persuasive elements. Documentation maintains its distinct purpose: enabling efficient problem-solving. Clarifying these distinct content purposes and audiences resolved the strategic misalignment.

## Impact

Ticket monitoring revealed that approximately one in three customer tickets could be resolved through documentation links, achieving a **30% ticket deflection rate**.

The consistent documentation structure enabled developers to independently configure data pipelines and troubleshoot issues. Standardized connector documentation provided predictable information architecture regardless of connector selection.

Monitoring searches without results created a feedback loop for identifying documentation gaps. This data-driven approach enabled continuous coverage improvement and prevented recurring support issues.

## Key Insights
| Key Insight | Description |
|---|---|
| **Information architecture determines usability.** | Content quality becomes irrelevant when users cannot locate information. Structural redesign represented the highest-impact intervention.|
| **Templates enable systematic scaling.** | Standardized documentation patterns made consistent, efficient documentation of hundreds of connectors achievable.|
| **Content types serve distinct purposes.** | Understanding the fundamental differences between documentation (problem-solving) and marketing content (persuasion) preserves the effectiveness of both.|
| **Data-driven iteration improves coverage.** | Monitoring search failures and ticket resolution patterns provides actionable insights for continuous documentation improvement.|

## Technologies & Tools

- **Documentation Platform:** Custom knowledge base
- **Source Control:** Git, GitLab
- **Content Format:** Markdown, HTML
- **API Testing:** Postman
- **Collaboration:** Jira, Confluence
- **Cloud Platforms:** Google Cloud, BigQuery, various data sources


[View Live Documentation →](https://docs.dataddo.com){:target="_blank" rel="noopener noreferrer" class="btn btn-primary"}
