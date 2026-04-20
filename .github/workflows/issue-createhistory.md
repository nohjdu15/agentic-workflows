---
on:
  issues:
    types: [opened, reopened]

permissions:
  contents: read
  issues: read
  pull-requests: read

tools:
  github:
    toolsets: [default, projects]

engine: copilot

network: defaults

safe-outputs: 
  update-project:
    project: https://github.com/users/<HU_OWNER>/projects/<HU_PROJECT_NUMBER>
    max: 1
    github-token: ${{ secrets.GH_AW_PROJECT_GITHUB_TOKEN }}
  update-issue:
    max: 1
  add-comment: {}
---

# issue-createhistory

when a new issue is opened or reopened, you will transform it into a structured bilingual user story using AI, update the original issue, and add it to a GitHub Project dashboard

## what to do

1. read the issue title and description
2. consume the GitHub API using github tools (projects toolset) and detect the GitHub Project associated with the triggering issue
3. if one or more projects are linked, pick the first project URL and use that exact URL in update_project
4. if no project is linked to the triggering issue, do not guess a project URL
5. analyze the content and determine the intent (bug, feature request, or improvement)
6. generate a structured user story in both spanish and english using the exact format below:

-------------
Story (Spanish)
Como Ingeniero DevSecOps contribuidor de la SPL,
quiero que...
para que...

Story (English)
As a DevSecOps Engineer contributor of the SPL,
I want...
so that...
---------
Acceptance Criteria (Spanish)
DADO que...
CUANDO...
ENTONCES...

Acceptance Criteria (English)
GIVEN...
WHEN...
THEN...

7. ensure the output is clear, specific, actionable, and technically precise
8. if the issue lacks information, make reasonable assumptions aligned with devsecops and ci/cd practices
9. generate acceptance criteria using testable and measurable conditions:
   - use technical outputs such as exit codes, logs (::error::), file paths, or pipeline/job status
   - avoid vague phrases like "should work correctly"
10. prioritize acceptance criteria that can be validated in ci/cd pipelines
11. do not include explanations or additional text outside the defined structure

## output behavior

- do not create a new issue
- update the triggering issue with the generated user story in the issue body
- use the project URL discovered from the triggering issue through GitHub API
- if no project is discovered, skip update_project and post a comment indicating "Issue sin proyecto asociado"
- set project fields when possible (for example: Status = Backlog, Priority = Medium)
- add a comment in the triggering issue with confirmation and the project URL

## constraints

- always include both spanish and english versions
- always follow the exact structure provided
- do not add extra sections or modify the format
- the content must be technically oriented to devsecops, ci/cd, and automation contexts

<!--
## TODO: Customize this workflow

The workflow has been generated based on your selections. Consider adding:

- [ ] More specific instructions for the AI
- [ ] Error handling requirements
- [ ] Output format specifications
- [ ] Integration with other workflows
- [ ] Testing and validation steps

## Configuration Summary

- **Trigger**: Issue opened or reopened
- **AI Engine**: copilot
- **Network Access**: defaults

## Next Steps

1. Review and customize the workflow content above
2. Remove TODO sections when ready
3. Run `gh aw compile` to generate the GitHub Actions workflow
4. Test the workflow with a manual trigger or appropriate event
-->
