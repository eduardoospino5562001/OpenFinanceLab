# Team Roles and Responsibilities

## Purpose and Flexibility

The roles below are proposed starting points for organizing the team's work. They are not fixed assignments, exclusive areas of ownership, or permanent titles. They may be adjusted as the project develops, as participants' interests and strengths become clearer, and as team needs and priorities change.

A proposed role is intended to provide a general area of ongoing responsibility and help the team coordinate its work. It should not prevent anyone from contributing outside that area, collaborating with others, or taking on different tasks.

**A role describes ongoing responsibility; a GitHub issue describes a specific deliverable.** The issues listed for each participant are recommendations for where they might initially contribute, not a complete definition of their role or a restriction on what they may work on.

For example, Sophie's responsibility for frontend/backend integration doesn't mean every integration-related issue must automatically be assigned to her. Some tasks may be better handled by Rushiil or another participant.

## Proposed Roles

| Participant | Proposed role | Primary focus | Recommended GitHub issues |
|---|---|---|---|
| **Sophie Harman** | Full-Stack Engineering and Application Integration | Building and integrating application components across the frontend and backend; supporting database design, dashboard implementation, testing, and development/deployment foundations. | OF-008 — Compare technical approaches; OF-038 — Design database schema *(collaborator)*; OF-044 — Transaction-summary endpoint; OF-050 — Dashboard shell; OF-051 — Display summary metrics; OF-053 — Loading and error states; OF-060 — Automated test execution; OF-068 — Local setup documentation. |
| **Zach Martim** | AI Engineering and Agent Development | Designing and implementing AI-assisted capabilities, including agent/tool interactions, model-provider integration, handling unsupported questions, and evaluating answer quality. | OF-067 — Document a design decision; OF-075 — Identify useful AI questions; OF-076 — Define approved tool functions; OF-078 — Compare no-cost model options; OF-079 — Model-provider interface; OF-080 — Implement one analytical tool call; OF-084 — Handle unsupported questions; OF-085 — Evaluate answer correctness. |
| **Ivan Eskic** | Data Engineering and Data Quality | Developing data-ingestion and transformation processes; generating and parsing data; detecting and handling data-quality problems; and storing validated financial records. | OF-009 — Define transaction schema *(collaborator)*; OF-011 — Generate synthetic revenue records; OF-012 — Generate synthetic expense records *(collaborator)*; OF-014 — Generate duplicate records; OF-018 — CSV parsing; OF-021 — Detect duplicates; OF-025 — Cleaning pipeline; OF-026 — Track ingestion counts; OF-029 — Test ingestion pipeline; OF-040 — Store validated transactions. |
| **Astha K C** | Financial Analytics and Reporting | Defining financial reporting requirements and calculations; validating financial metrics; shaping dashboard and report content; and ensuring that outputs are consistent and useful. | OF-005 — Define financial reporting questions; OF-007 — Define initial data fields *(collaborator)*; OF-016 — Generate inconsistent categories *(collaborator)*; OF-017 — Document synthetic-data assumptions; OF-030 — Define monthly revenue calculation; OF-032 — Define monthly expense calculation; OF-034 — Define net cash-flow calculation; OF-049 — Sketch dashboard layout; OF-056 — Verify dashboard calculations; OF-071 — Define report contents; OF-074 — Test report consistency. |
| **Rushiil Nakka** | Backend/API Engineering and AI Integration | Designing and implementing backend interfaces, API validation and error handling, integration between services, and the backend capabilities needed to support AI tools. | OF-043 — Define API response format; OF-045 — Monthly-metrics endpoint; OF-046 — API input validation; OF-047 — Standardize API errors; OF-061 — Continuous integration *(collaborator)*; OF-077 — Define AI evaluation dataset *(collaborator)*; OF-081 — Validate AI tool inputs; OF-082 — Return calculated results to assistant; OF-086 — Test model and tool failures. |

## Areas of Collaboration

Some work naturally crosses the proposed role boundaries. Participants should coordinate rather than treat the table as a set of separate silos. Examples include:

- **Database and data structures:** Sophie, Ivan, and Astha may work together on schema design, data fields, and how financial information is represented.
- **Data requirements and quality:** Ivan and Astha may coordinate on the structure, assumptions, validation, and interpretation of financial data.
- **Backend and frontend integration:** Sophie and Rushiil may coordinate API contracts and the integration of application components.
- **AI integration:** Zach and Rushiil may coordinate the AI-facing design, tool interfaces, backend integration, and failure handling.
- **Testing and reliability:** Everyone is expected to test their work and help identify problems that affect the larger application.

These examples are not an exhaustive assignment of collaboration. The appropriate participants will depend on the specific issue and the state of the project.

## Shared Expectations

Regardless of proposed role, each participant is expected to:

- Take responsibility for understanding and progressing the GitHub issues they undertake.
- Communicate progress, questions, blockers, and changes that may affect other work.
- Coordinate with teammates when tasks have dependencies or overlapping responsibilities.
- Follow the repository's contribution workflow, including branches, pull requests, and code review.
- Aim for code and documentation that are understandable, maintainable, and appropriately tested.
- Document important technical decisions and relevant assumptions.
- Be willing to review teammates' work and contribute outside their proposed area when useful.

The proposed roles and issue recommendations should be revisited as the team's composition, interests, capabilities, and project priorities evolve.
