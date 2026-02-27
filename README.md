# Sboboz Bot - Reinforcement Learning Agent

Un agente di Reinforcement Learning per il gioco Sboboz basato su PPO e self-play.

## 🎯 Obiettivi

- Creare un bot che impari a giocare tramite self-play
- Architettura modulare e accademicamente corretta
- Separazione totale tra game engine e UI
- Integrabile in Flutter via API

## 🏗️ Architettura

```
sboboz/
├── game/           # Game Engine puro (nessuna UI)
├── env/            # Gymnasium Environment
├── agents/         # Random Agent + PPO Agent
└── training/       # Training e Self-play
```

## 📋 Fasi di Sviluppo

### ✅ Fase 1: Game Engine

- [] GameState puro
- [] get_legal_actions()
- [] apply_action()
- [] Simulazione random completa

### ✅ Fase 2: Gymnasium Environment

- [] SbobozEnv
- [] Observation space (vettoriale numerico)
- [] Action space (con action masking)
- [] reset() e step()

### 🔄 Fase 3: Training Base

- [ ] Addestrare PPO vs Random Agent
- [ ] Valutare winrate

### 🔄 Fase 4: Self-Play

- [ ] Salvare versioni modello
- [ ] Opponent sampling da pool
- [ ] Training iterativo

### 🔄 Fase 5: Miglioramenti

- [ ] State encoding avanzato
- [ ] Scelta multi-card
- [ ] Reward shaping

## 🚀 Quick Start

```bash
# Creare ambiente virtuale
python -m venv .venv
.venv\Scripts\activate

# Installare dipendenze
pip install -r requirements.txt

# Testare game engine
python -m pytest tests/

# Simulazione random vs random
python -m sboboz.game.game_state

# Training PPO
python -m sboboz.training.train --episodes 10000

# Self-play
python -m sboboz.training.self_play --iterations 10
```

## 📦 Dipendenze

- gymnasium
- stable-baselines3[extra]
- numpy
- torch

## 🎮 Integrazione Flutter

Il modello addestrato può essere esposto via API REST/gRPC per l'integrazione con l'app Flutter.

## 📊 Monitoraggio

I log di training e i modelli salvati sono in:

- `experiments/` - Log e metriche
- `models/` - Checkpoint modelli

## 🧪 Testing

```bash
pytest tests/ -v
```
