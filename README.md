# miftaah-drone

Monorepo for drone simulation, perception, and RL.

Structure:
- infra/: terraform, k8s
- sim/: Gazebo, AirSim, datasets
- backend/: FastAPI + websocket
- perception/: YOLO and tracking
- rl/: DRL agents and env wrappers
- models/: saved small model artifacts
