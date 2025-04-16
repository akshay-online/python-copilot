# ✅ Requirements: *Smart Task Tracker API*

## 🔐 User Management

1. **User Registration & Login**
   - As a new user, I want to **register using social login** (Google, GitHub, Microsoft) so I don’t need to remember another password.
   - As a returning user, I want to **log in using the same social account** I registered with.
   - As a user, I should also have the option to **register/login using email and password** if I don’t want to use social login.
   - As a user, I want to **reset my password** using a secure email link if I forget it.
   - As a user, I want my **profile to be editable**, including display name, profile picture, and contact preferences.

2. **Roles & Access**
   - As an admin, I want to **create and manage users and assign roles** (Admin, Project Manager, Developer).
   - As a system, I must restrict access to protected routes based on the user’s role.

---

## 📋 Project & Task Management

1. **Project CRUD**
   - As an admin, I want to **create, update, and delete projects**.
   - As a project manager, I want to **assign users to projects**.
   - As a user, I want to **see all projects I'm a part of**.

2. **Task CRUD**
   - As a user, I want to **create tasks under a project**, so I can track work items.
   - As a user, I want to **edit, update status, delete, or mark tasks as complete**.
   - As a user, I want to **assign tasks to team members**.
   - As a user, I want to **set deadlines and priority levels (Low, Medium, High)**.
   - As a user, I want to **attach reference files** (PDFs, Docs, etc.) to tasks.

---

## 🔔 Notification & Alerts

- As a user, I want to receive:
  - **Email reminders** before a task's due date.
  - **Notifications when tasks are assigned to me or updated**.
  - **Weekly summary emails** of tasks status (optional via settings).

---

## 📊 Reporting

- As a user, I want to:
  - View **task completion status per project**.
  - Export reports in **PDF or Excel** formats.

---

## 🧪 Other Features

- As a user, I want to:
  - **Filter tasks** by status, due date, priority, and assigned user.
  - **Search tasks** using keywords.
  - View a **calendar view** of task due dates (optional stretch goal).

---

# 📐 Non-Functional Requirements

### 🏗️ Architecture
- The system should follow **clean architecture principles**, supporting both monolithic and microservice options.

### ⚡ Performance
- Most API responses should complete in **< 200ms** under normal load.

### 🔒 Security
- All endpoints must be protected via **JWT-based authentication**.
- User input should be validated on both client and server.
- OAuth2 for social logins using providers like Google, GitHub, and Microsoft.

### ☁️ Scalability & Availability
- System must be deployable to the cloud (e.g., Azure, AWS) and handle at least **100 concurrent users** with **99.9% uptime**.

### 🛠️ Maintainability
- The code should be **modular, testable**, and follow **SOLID** principles.
- Should include **unit and integration tests** for critical paths.

### 📈 Monitoring & Logging
- The application should expose **health check endpoints**.
- Logs should be **centralized and searchable** via ELK or Azure Monitor.
- Include support for metrics (e.g., Prometheus + Grafana or Azure Application Insights).