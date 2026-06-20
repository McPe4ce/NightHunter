# NightHunter

A beginner Python dungeon crawler game built in four parts, from architecture diagrams to a playable client.

NightHunter is to dungeon games what HBnB is to AirBnb — a small, complete, learnable replica of a real system. It teaches Python from the ground up: classes, APIs, databases, and user interfaces, one concept at a time.

All architecture diagrams, class diagrams, sequence diagrams, API specs, and technical documentation were personally authored as part of this project and can be found in [`docs-NightHunter`](../docs-NightHunter/).

---

## The Game

A player registers an account and creates a hero — Warrior, Mage, Rogue, or Cleric. They enter a dungeon, navigate its rooms, and fight monsters to earn gold. The world persists: close the game and come back later, and your hero is exactly where you left them.

---

## Project Structure

| Part | Focus | What You Build |
|------|-------|----------------|
| [Part 0](part0/) | Python Basics | Playable game in a single script — learn the language before the architecture |
| Part 1 | Design | Architecture diagrams, class diagrams, sequence diagrams, technical document |
| Part 2 | Core Python | Entity classes, game logic, Flask API with in-memory storage |
| Part 3 | Backend | JWT authentication, password hashing, SQLite persistence via SQLAlchemy |
| Part 4 | Interface | Terminal or web client that connects to the Part 3 API |

---

## API Reference

The full API is defined in the docs [`openapi.yaml`](../docs-NightHunter/openapi.yaml). Key endpoints:

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/auth/register` | Create a player account |
| `POST` | `/auth/login` | Log in and receive a JWT token |
| `POST` | `/characters` | Create a hero |
| `GET` | `/characters/<id>` | Get hero details |
| `POST` | `/dungeons` | Create a dungeon (admin only) |
| `POST` | `/characters/<id>/enter-dungeon` | Enter a dungeon |
| `POST` | `/characters/<id>/move` | Move to an adjacent room |
| `POST` | `/characters/<id>/attack` | Attack a monster |

---

## Getting Started

```bash
git clone <this-repo>
cd NightHunter
```

Start with Part 0 — no dependencies needed, just Python 3.

When you reach Part 2, set up your virtual environment first:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
# Visit http://localhost:5000 for the Swagger UI
```

---

## Git Workflow

Read [`git_workflow.md`](../docs-NightHunter/git_workflow.md) before your first commit. Each task has a "Git Checkpoint" section — follow it. By the end of the project you will have a complete, commit-by-commit history of how you built NightHunter from scratch.
