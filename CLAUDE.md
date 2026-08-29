## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).


## District / location culture synthesis

When doing per-district or per-location cultural synthesis work, **start at
`Worldspace/Locations-and-Levels/Concordia-City/Districts/Phase_Instructions/00_RUNBOOK.md`.** It is the
operational procedure — eight ordered steps, eleven QA gates, the Review Panel, and the standing honesty
problems — and it points to every detail file. Do not reconstruct the method from the phase files or from the
index's historical notes; the runbook exists so that is unnecessary.

Two things in it are easy to skip and should not be:
- **`Cross_District_Differentiation_Table.md`** — check the relevant row *before* writing a category, and add
  the district's column in the same commit that completes it. It is the only mechanical guard against thirteen
  districts quietly converging.
- **Paste raw QA scan output rather than summarizing it.** Self-audit error in this project has run in one
  direction — toward flattering the pass — on every occasion it has been measured.
