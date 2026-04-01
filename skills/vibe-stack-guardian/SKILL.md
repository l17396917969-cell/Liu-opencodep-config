---
name: vibe-stack-guardian
description: Use when initializing a new project, introducing new dependencies, or making architecture decisions that require Vibe Coding compliance verification
---

# Vibe Stack Guardian

## Overview

Guardian skill that enforces Vibe Coding technical standards during project initialization, dependency selection, and architecture design. Prevents technology stack drift by validating all decisions against the Three Iron Rules and Seven Principles.

## When to Use

- **Project Initialization**: When user says "帮我搭建...", "create a new project", "init a backend/frontend"
- **Dependency Introduction**: When user wants to add a new library/framework not in the whitelist
- **Architecture Design**: When planning system structure, database schema, or API design
- **Technology Migration**: When considering switching from one stack to another

**When NOT to use**: Routine coding tasks within an already-compliant project, bug fixes, or minor feature additions using established stack.

## Core Rules

### The Three Iron Rules

| Rule | Requirement | Validation Check |
|------|-------------|------------------|
| **Container First** | All services via Docker Compose | `docker-compose.yml` present? No local service installs? |
| **Schema Driven** | ORM + Pydantic everywhere | SQLModel/Prisma used? All IO has Pydantic models? |
| **Explicit Observability** | Structured logging + clear errors | Loguru configured? Errors traceable to AI fix? |

### Tech Stack Whitelist

#### Infrastructure Layer
| Component | Mandatory Choice | Forbidden Alternatives |
|-----------|-----------------|----------------------|
| Orchestration | Docker Compose | Local Python/Node, systemd |
| Python Package Manager | uv | pip, poetry, conda |
| JS Package Manager | pnpm | npm, yarn |
| Environment | python-dotenv | Hardcoded configs, os.environ direct |

#### Data Layer
| Component | Mandatory Choice | Forbidden Alternatives |
|-----------|-----------------|----------------------|
| Database | PostgreSQL (Docker) | SQLite, MySQL, MongoDB |
| ORM (Python) | SQLModel | Raw SQL, SQLAlchemy without Pydantic |
| ORM (TS/Node) | Prisma | TypeORM, Sequelize |
| Vector Store | pgvector | Chroma, Milvus, Pinecone |
| DB Admin | Adminer/PGAdmin in compose | Local pgAdmin, CLI only |

#### Backend Layer
| Component | Mandatory Choice | Forbidden Alternatives |
|-----------|-----------------|----------------------|
| Web Framework | FastAPI | Flask, Django, Express |
| Validation | Pydantic V2 | Cerberus, Marshmallow, manual |
| Async Tasks | ARQ (Redis) | Celery, RQ, custom threads |

#### Frontend Layer
| Component | Mandatory Choice | Forbidden Alternatives |
|-----------|-----------------|----------------------|
| Internal Tools | Streamlit | Gradio, Dash, custom React |
| C-End Apps | Next.js + shadcn/ui | Vue, Angular, raw React |
| Docs | Redoc (FastAPI) | Manual markdown, Swagger UI |

#### AI Layer
| Component | Mandatory Choice | Forbidden Alternatives |
|-----------|-----------------|----------------------|
| Model Gateway | LiteLLM | Direct OpenAI calls, custom clients |
| Structured Output | Instructor | Raw LLM calls, regex parsing |

#### QA Layer
| Component | Mandatory Choice | Forbidden Alternatives |
|-----------|-----------------|----------------------|
| Logging | Loguru | Standard logging, print |
| Testing | Pytest | unittest, no tests |
| Linting | Ruff | flake8, black, pylint |

## The Seven Principles (Extension Policy)

Before introducing ANY new library, verify ALL principles:

1. **Atomic Rule**: General lib + AI logic > Niche framework
   - ✅ Pandas for data + AI logic
   - 🛑 Specialized "business rule engine"

2. **AI Proficiency**: AI can write code instantly without docs
   - ✅ FastAPI, SQLModel
   - 🛑 Obscure library with poor examples

3. **Code-First**: No GUI editors required
   - ✅ Prisma schema files
   - 🛑 Unity Editor, Unreal Blueprint

4. **No-Binary**: Pure native or Dockerized
   - ✅ pip installable, has Dockerfile
   - 🛑 Requires complex C++ compilation

5. **Declarative**: Configuration over code
   - ✅ YAML configs, Pydantic models
   - 🛑 Imperative scripts, complex inheritance

6. **Type-Safety**: Full type hints / TypeScript
   - ✅ Pydantic, Prisma
   - 🛑 Dynamic languages without types

7. **Not Dead**: GitHub stars > 5000, recent commits
   - ✅ FastAPI (70k+ stars)
   - 🛑 Last commit 2 years ago

## Decision Tree

```
Need new library/framework?
        |
        v
Is it in whitelist? ---> YES --> Use it
        |
        NO
        |
        v
Pass 7 Principles? ---> NO --> STOP, use AI logic instead
        |
       YES
        |
        v
Is it atomic/general? --> NO --> STOP, build with Python
        |
       YES
        |
        v
Is it AI-proficient? --> NO --> STOP, find alternative
        |
       YES
        |
        v
  APPROVED for use
```

## Validation Checklist

### For Project Initialization

- [ ] `docker-compose.yml` will be generated
- [ ] `.env.example` will be provided with python-dotenv
- [ ] Backend uses FastAPI + SQLModel (Python) or Next.js (JS)
- [ ] Database uses PostgreSQL via Docker
- [ ] Loguru configured for structured logging
- [ ] Pytest setup for testing

### For New Dependency

- [ ] Passes 7 Principles check
- [ ] GitHub stars > 5000 OR AI knows it well
- [ ] Not a niche framework when general lib works
- [ ] Has Docker support if binary involved
- [ ] Supports type hints / TypeScript

### For Architecture Decision

- [ ] Container First: All components dockerized
- [ ] Schema Driven: All data has model definitions
- [ ] Observability: Errors traceable, logs structured
- [ ] No local service dependencies

## Common Mistakes

**Mistake**: "I'll use Flask because it's simpler"
- **Fix**: Flask lacks Pydantic integration. Use FastAPI for Schema Driven requirement.

**Mistake**: "SQLite is fine for this small project"
- **Fix**: Use PostgreSQL in Docker. Migration path later is painful.

**Mistake**: "I'll add Redis directly to the host"
- **Fix**: Redis must be in docker-compose.yml. No local service installs.

**Mistake**: "This specialized library handles exactly my use case"
- **Fix**: Check Atomic Rule. Can you build it with Pandas + AI logic instead?

**Mistake**: "I'll parse the LLM output with regex"
- **Fix**: Use Instructor for structured output. No regex parsing.

## Action Protocol

When triggered, execute:

1. **Analyze Request**: Identify if this involves tech stack selection
2. **Run Checklist**: Apply appropriate validation checklist
3. **Report Violations**: List any non-compliance found
4. **Propose Fix**: Suggest compliant alternatives
5. **Confirm**: Get user approval before proceeding

**If user insists on non-compliant choice**: Document the deviation and its risks, but respect user decision.
