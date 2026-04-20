---
on:
  issue_comment:
    types: [created]
permissions:
      contents: read
engine: copilot
network: defaults
---

# issue-create-history

This workflow reads newly created GitHub issues and transforms them into structured User Stories using AI.

The AI must:
1. Read the issue title and body as input.
2. Analyze the content and determine the intent (bug, feature request, or improvement).
3. Rewrite the content into a formal User Story using the exact structure below:

-------------
Story
Como Ingeniero DevSecOps contribuidor de la SPL,
quiero que...
para que...
---------
Acceptance Criteria
DADO...
CUANDO...
ENTONCES...

4. Ensure the output is clear, specific, and actionable.
5. If the issue lacks information, the AI should make reasonable assumptions but keep them realistic and aligned with DevSecOps practices.
6. Do not include explanations, only return the formatted User Story.

7. When generating the Acceptance Criteria, the AI must follow the Given/When/Then (DADO/CUANDO/ENTONCES) format with precise technical behavior:

- DADO (Given): Define the initial context, system state, or preconditions required before execution.
  It must describe where or under what conditions the scenario starts (e.g., a file exists, a pipeline runs, a script is executed).

- CUANDO (When): Describe the exact action or event being performed.
  It must be a clear, executable action (e.g., running a script, triggering a pipeline, processing a file).

- ENTONCES (Then): Describe the expected observable outcome.
  It must be measurable, verifiable, and testable (e.g., exit code, log output, validation message, artifact generation).

Rules:
- Each Acceptance Criteria must be testable and unambiguous.
- Avoid generic phrases like "should work correctly" or "should validate properly".
- Prefer technical outputs such as:
  - exit codes (0, 1)
  - console outputs (e.g., ::error:: messages)
  - file changes
  - pipeline/job status
- If applicable, include file paths, command examples, or execution context.

8. Prioritize Acceptance Criteria that can be validated in CI/CD pipelines.

Output behavior:
- Create a new GitHub issue with the generated User Story.
- The new issue title must start with: "HU - "
- Include a reference to the original issue number in the body.

Constraints:
- Always follow the exact structure provided.
- Do not change the language (must be Spanish).
- Do not add extra sections outside the defined format.

# --------------------------------------------------------------------------------
# Traducción al español (comentario)
#
# Este workflow lee los issues recién creados en GitHub y los transforma en
# Historias de Usuario estructuradas utilizando IA.
#
# La IA debe:
# 1. Leer el título y el cuerpo del issue como entrada.
# 2. Analizar el contenido y determinar la intención (bug, solicitud de funcionalidad o mejora).
# 3. Reescribir el contenido en una Historia de Usuario formal usando exactamente la siguiente estructura:
#
# -------------
# Story
# Como Ingeniero DevSecOps contribuidor de la SPL,
# quiero que...
# para que...
# ---------
# Acceptance Criteria
# DADO...
# CUANDO...
# ENTONCES...
#
# 4. Asegurar que la salida sea clara, específica y accionable.
# 5. Si el issue carece de información, la IA debe hacer suposiciones razonables,
#    pero manteniéndolas realistas y alineadas con prácticas DevSecOps.
# 6. No incluir explicaciones, solo retornar la Historia de Usuario formateada.
#
# 7. Al generar los Acceptance Criteria, la IA debe seguir el formato
#    DADO/CUANDO/ENTONCES con comportamiento técnico preciso:
#
# - DADO: Define el contexto inicial, estado del sistema o precondiciones.
#   Debe indicar bajo qué condiciones inicia el escenario (ej: existe un archivo, corre un pipeline).
#
# - CUANDO: Describe la acción exacta que se ejecuta.
#   Debe ser clara y ejecutable (ej: correr un script, ejecutar un comando, procesar un archivo).
#
# - ENTONCES: Describe el resultado esperado observable.
#   Debe ser medible y verificable (ej: código de salida, logs, errores, artefactos).
#
# Reglas:
# - Cada criterio debe ser testeable y sin ambigüedad.
# - Evitar frases genéricas como "debe funcionar correctamente".
# - Preferir salidas técnicas como:
#   - códigos de salida (0, 1)
#   - logs (::error::)
#   - cambios en archivos
#   - estado de jobs o pipelines
#
# 8. Priorizar Acceptance Criteria que puedan validarse en pipelines CI/CD.
#
# Comportamiento de salida:
# - Crear un nuevo issue en GitHub con la Historia de Usuario generada.
# - El título debe iniciar con: "HU - "
# - Incluir referencia al issue original.
#
# Restricciones:
# - Seguir exactamente la estructura.
# - Mantener idioma en español.
# - No agregar secciones adicionales.

<!--
## TODO: Customize this workflow

The workflow has been generated based on your selections. Consider adding:

- [ ] More specific instructions for the AI
- [ ] Error handling requirements
- [ ] Output format specifications
- [ ] Integration with other workflows
- [ ] Testing and validation steps

## Configuration Summary

- **Trigger**: Issue comment created
- **AI Engine**: copilot
- **Network Access**: defaults

## Next Steps

1. Review and customize the workflow content above
2. Remove TODO sections when ready
3. Run `gh aw compile` to generate the GitHub Actions workflow
4. Test the workflow with a manual trigger or appropriate event
-->
