# City Navigator & Delivery Planner

**Smart City Navigation, Delivery Planning & Road Network Optimization**

## 1. Project Overview

City Navigator & Delivery Planner is a Python-based application that models a city's road network and provides efficient solutions for navigation, delivery planning, and road network optimization.

The system represents city intersections and roads using graph data structures, taking one-way streets into account. It helps users find shortest routes, manage delivery orders by priority, and identify cost-effective ways to connect different areas.

The project demonstrates the practical application of Data Structures and Algorithms through an interactive, real-world-inspired system.

## 2. Project Objectives

- Model a city using directed and undirected graphs.
- Find efficient routes between locations.
- Manage and prioritize delivery orders.
- Optimize road network expansion costs.
- Implement and compare sorting and searching techniques.
- Analyze algorithm performance using time complexity and doubling ratios.
- Apply course concepts through practical implementations.

## 3. Main Features

| Feature | Description |
|---|---|
| City Map | Display intersections and existing one-way roads. |
| Route Finder | Find shortest paths between selected locations. |
| Delivery Planner | Manage and prioritize delivery orders. |
| Road Optimizer | Find minimum-cost connections for potential new roads. |
| Algorithm Lab | Compare sorting algorithms and visualize performance results. |

## 4. Data Structures & Algorithms

The project will implement the following course concepts from scratch:

| Topic | Planned Application |
|---|---|
| Stacks & Queues | Graph traversal and processing operations |
| Elementary Sorting | Bubble, Selection, and Insertion Sort |
| Mergesort | Efficient sorting of records |
| Priority Queues & Heaps | Delivery prioritization and shortest-path processing |
| Symbol Tables | Key-value mapping for application records |
| BST & Balanced Search Trees | Searching and organizing records using BST and AVL Trees |
| Hash Tables | Fast lookup of locations and orders |
| Directed Graphs | Representing existing one-way streets |
| Undirected Graphs | Representing potential road connections |
| DFS & BFS | Graph traversal |
| Connected Components | Connectivity analysis |
| Shortest Paths | Dijkstra's Algorithm |
| Minimum Spanning Trees | Prim's and Kruskal's Algorithms |
| Algorithm Analysis | Time complexity and doubling-ratio experiments |

**Optional Extension:** Linear Programming, depending on the team's progress and implementation feasibility.

## 5. Technology Stack

- **Language:** Python
- **Data Storage:** JSON
- **UI:** Streamlit
- **Visualization:** Matplotlib
- **Version Control:** Git & GitHub

All required data structures and algorithms will be implemented from scratch. Libraries may be used for UI, visualization, and general application support, but not as replacements for required implementations.

## 6. Team Members & Responsibilities

The work is divided into three main roles to enable parallel development and clear task ownership.

### Role 1 — Graph & Navigation
**Assignee: Saif Aldeen Al Sayde**

- Prepare and manage city intersections and existing-road JSON data.
- Implement Directed Graph using an Adjacency List.
- Implement Stack and Queue.
- Implement BFS and DFS.
- Implement Dijkstra's shortest-path algorithm.
- Handle graph connectivity analysis.
- Develop and test the Route Finder component.

### Role 2 — Road Network Optimization & Algorithm Analysis
**Assignee: Rania Raafat**

- Prepare candidate-road data and construction costs in JSON.
- Implement an Undirected Weighted Graph using an Adjacency List.
- Implement Priority Queue and Binary Min Heap.
- Implement Prim's and Kruskal's MST algorithms.
- Implement Bubble Sort, Selection Sort, Insertion Sort, and Mergesort.
- Conduct performance experiments using doubling ratios.
- Visualize road optimization and algorithm performance.
- Explore Linear Programming as an optional extension.

### Role 3 — Data Management & Delivery Planning
**Assignee: Ziad Mohamad**

- Prepare and manage location and delivery-order JSON data.
- Implement Hash Table and Symbol Table functionality.
- Implement Binary Search Tree and AVL Tree.
- Develop delivery-order management operations.
- Integrate data structures into the delivery workflow.
- Develop and test the Delivery Planner component.

## 7. Implementation Timeline

| Milestone | Deadline | Deliverables |
|---|---|---|
| M1 — Proposal & Project Setup | Nov 29, 2026 | Project proposal, team roles, and repository setup |
| M2 — Core Data Structures | Dec 6, 2026 | Sorting, Priority Queue, Symbol Table, and Hash Table |
| M3 — Graph Algorithms | Dec 13, 2026 | Directed & Undirected Graphs, traversal, MST, and shortest paths |
| Integration & Testing | Dec 14–18, 2026 | Component integration, main UI, testing, and documentation |
| Code Freeze | Dec 19, 2026 | Final stable version |
| Final Presentation | Dec 20, 2026 | Live demonstration and project discussion |

## 8. Development Workflow

The team will follow a Git-based workflow:

- `main`: Stable project version.
- `develop`: Main integration branch.
- `feat/*`: Individual feature branches.
- Pull Requests will be used to review and merge completed work into `develop`.
- Each member will contribute through their own GitHub account.

## 9. UI & Deployment

Each member will develop a simple UI to test and demonstrate their assigned component independently. Once the components are ready, the team will integrate them into one main application and work together on the final UI design, integration, and deployment.

## 10. Expected Outcome

A functional and interactive city navigation and delivery planning application that demonstrates the practical use of Data Structures and Algorithms in route finding, delivery management, and road network optimization.