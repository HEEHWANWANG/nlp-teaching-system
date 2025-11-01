#!/bin/bash

# NLP Knowledge agents
for agent in nlp-theory nlp-papers nlp-trends linguistics nlp-knowledge-coordinator; do
cat > .claude/agents/pods/nlp-knowledge/${agent}-agent.md << EOF
---
name: ${agent}-agent
description: ${agent} specialist
tools: Read, Write, web_search
model: sonnet
---

# ${agent} Agent

NLP 지식 제공 전문가
EOF
done

# LaTeX agents  
for agent in latex-writer math-formula biblio diagram latex-doc-coordinator; do
cat > .claude/agents/pods/latex-doc/${agent}-agent.md << EOF
---
name: ${agent}-agent
description: ${agent} specialist
tools: Read, Write, Bash
model: sonnet
---

# ${agent} Agent

LaTeX 문서 작성 및 수식 처리
EOF
done

# Tools agents
for agent in github-manager data-engineer experiment-tracker web-researcher tools-coordinator; do
cat > .claude/agents/pods/tools/${agent}-agent.md << EOF
---
name: ${agent}-agent
description: ${agent} specialist
tools: Read, Write, Bash
model: sonnet
---

# ${agent} Agent

도구 및 인프라 관리
EOF
done

# Teaching agents
for agent in concept-explainer homework-helper career-advisor teaching-coordinator; do
cat > .claude/agents/pods/teaching/${agent}-agent.md << EOF
---
name: ${agent}-agent
description: ${agent} specialist
tools: Read, Write
model: sonnet
---

# ${agent} Agent

학생 교육 지원
EOF
done
