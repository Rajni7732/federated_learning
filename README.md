# federated_learning
# 🧠 Federated Learning Simulator using Streamlit

A fully interactive **Federated Learning** dashboard built using **Streamlit**, where multiple clients train local models and collaborate via a central server. The project demonstrates end-to-end communication, model training, aggregation, and evaluation across distributed systems, simulating how modern FL systems work in real-world privacy-preserving scenarios.

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-orange?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Table of Contents

- [Overview](#rocket-overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Setup & Installation](#setup--installation)
- [How to Run](#how-to-run)
- [Folder Structure](#folder-structure)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## 🚀 Overview

This project demonstrates a **Federated Learning (FL)** environment where:
- Clients train local models using private data
- Models are sent to a **central server**
- The server aggregates models (e.g., via stacking or averaging)
- Updated global model is redistributed to all clients

This simulates edge-device learning in sensitive domains like healthcare or mobile AI, where raw data never leaves the device.

---

## ✅ Key Features

- 📡 **Client-server socket communication**
- 🖥️ **Streamlit UI** for real-time interaction
- 🔒 **Data privacy preserved** through local training
- 🧩 **Custom model aggregation** (Stacking, Averaging, etc.)
- 📊 **Loop-based federated simulation**
- 📦 **Modular structure** with reusable logic in `serverNew.py` and `clientNew.py`

---

## 🧱 Architecture

```text
     +---------------------+                     +---------------------+
     |      Client 1       |                     |      Client N       |
     |  Trains local model |                     |  Trains local model |
     |  Sends to Server    |----> Server <----   |  Sends to Server    |
     |  Receives global    |                     |  Receives global    |
     +---------------------+                     +---------------------+

                      Server performs model aggregation
