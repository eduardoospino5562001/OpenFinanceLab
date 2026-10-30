# OpenFinanceLab — Development Setup

## 1. Overview

This document describes how to configure a local development environment for OpenFinanceLab. The initial development environment consists of:

- Git for source control.
- Python for backend development and data processing.
- Node.js and npm for frontend development.
- React and TypeScript for the frontend.
- FastAPI for the backend API.
- SQLite or PostgreSQL for data storage.

Development is performed locally, with source code and project changes managed through GitHub. The instructions below assume Windows with PowerShell. Linux and macOS users can use equivalent commands where indicated.

## 2. Prerequisites

Install the following software before beginning development.

### 2.1 Git

Git is used for version control and collaboration. Download and install:

https://git-scm.com/downloads

Verify the installation:

```bash
git --version
```

Configure your Git identity if you have not already done so:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Use the email address associated with your GitHub account when possible.

### 2.2 GitHub Account

You will need a GitHub account with access to the OpenFinanceLab repository: https://github.com/hansen-ai-service/OpenFinanceLab

### 2.3 Python

Install a current stable Python 3 release supported by the project's dependencies. Download:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

On some systems, the command may instead be:

```bash
python3 --version
```

### 2.4 Node.js and npm

Node.js is required for frontend development. Download the current supported LTS release:

https://nodejs.org/

Verify the installation:

```bash
node --version
npm --version
```

### 2.5 Code Editor

Visual Studio Code is recommended. Download:

https://code.visualstudio.com/

Useful extensions include:

- Python
- Pylance
- ESLint
- Prettier
- GitLens
- Docker

Other editors may be used if they support the required development tools.

## 3. Clone the Repository

Open a terminal and navigate to the directory where you want to store the project.

Clone the repository:

```bash
git clone https://github.com/hansen-ai-service/OpenFinanceLab.git
```

Navigate into the project directory:

```bash
cd OpenFinanceLab
```

Open the project in Visual Studio Code:

```bash
code .
```

Before beginning work, make sure your local repository is up to date:

```bash
git checkout main
git pull origin main
```

## 4. Backend Setup

The backend uses Python and FastAPI.

### 4.1 Create a Virtual Environment

From the repository root, navigate to the backend directory (or make the directory if it is not already created):

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

If PowerShell prevents activation because of its execution policy, consult the Python virtual-environment documentation or use Command Prompt activation instead.

When activated, the environment name should appear in your terminal prompt.

### 4.2 Install Dependencies

Once the backend dependency file (`requirements.txt`) is available:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Backend dependencies are expected to include the following categories:

- FastAPI for API development.
- Uvicorn for running the application.
- SQLAlchemy or an equivalent database-access library.
- Pydantic for data validation.
- Pandas and NumPy for data processing and analysis.
- Pytest for automated testing.

The actual dependency list should be maintained in `backend/requirements.txt`.

### 4.3 Configure Environment Variables

Create a local environment file based on the project's example configuration:

```bash
copy .env.example .env
```

On Linux/macOS:

```bash
cp .env.example .env
```

The environment file may contain settings such as:

```dotenv
APP_ENV=development
DATABASE_URL=sqlite:///./openfinance.db
```

Additional variables may be introduced as application functionality develops.

Do not commit `.env` files or credentials (like keys, passwords, secrets, etc.) to GitHub. Only commit the example configuration file, without actual secrets.

### 4.4 Run the Backend

Once the FastAPI application has been implemented, start the development server from the backend directory:

```bash
uvicorn app.main:app --reload
```

The default local address is:

http://127.0.0.1:8000

FastAPI provides interactive API documentation at:

http://127.0.0.1:8000/docs

The application should automatically reload when backend source files change. The exact application module path may change as the backend structure is established.

## 5. Frontend Setup

The frontend uses React and TypeScript.

### 5.1 Install Dependencies

Open a separate terminal and navigate to the frontend directory (or make it if it has not already been created):

```bash
cd frontend
```

Once the frontend `package.json` and lockfile have been committed, install the dependencies:

```bash
npm ci
```

If a lockfile has not yet been created, use:

```bash
npm install
```

The frontend is expected to use:

- React for the user interface.
- TypeScript for application development.
- Vite for development and build tooling.
- ESLint for code-quality checks.

### 5.2 Run the Frontend

Start the development server:

```bash
npm run dev
```

Vite will display the local address, typically:

http://localhost:5173

Open that address in your browser to access the application.

### 5.3 Build the Frontend

To generate a production build:

```bash
npm run build
```

The resulting files will normally be placed in the `dist/` directory.

## 6. Database Setup

The initial development environment may use SQLite to simplify local development. SQLite does not require a separate database server installation. The application should be configured through the `DATABASE_URL` environment variable so that the database can be changed without modifying application logic.

For example:

```dotenv
DATABASE_URL=sqlite:///./openfinance.db
```

If PostgreSQL is adopted, developers will need to install or access a PostgreSQL instance and configure the appropriate connection string. Database schema changes should be managed through database migrations rather than manual modifications to individual development databases. Database initialization and migration commands will be documented here once the database implementation is established.

## 7. Running the Application

During development, the frontend and backend should generally run in separate terminal windows.

**Terminal 1 — Backend**

```bash
cd backend
# Activate the virtual environment
uvicorn app.main:app --reload
```

**Terminal 2 — Frontend**

```bash
cd frontend
npm run dev
```

The frontend communicates with the backend through its HTTP API. The backend API address and any frontend proxy configuration should be maintained in the application's development configuration.

## 8. Running Tests

Automated tests are an important part of the development process.

### 8.1 Backend Tests

Activate the backend virtual environment and install the development dependencies.

Run the backend test suite:

```bash
pytest
```

To run tests with additional output:

```bash
pytest -v
```

To run an individual test file:

```bash
pytest tests/test_example.py -v
```

Backend tests should cover, among other things:

- Financial calculations.
- Data validation.
- Data transformations.
- Database operations.
- API endpoints.
- Error handling.

### 8.2 Frontend Tests

From the frontend directory, execute:

```bash
npm test
```

The actual test command will depend on the frontend testing framework selected for the project. Frontend tests should cover important components, user interactions, and application behavior.

### 8.3 Testing Expectations

Developers should test their changes before submitting pull requests. Changes should not introduce regressions in existing functionality. New functionality should include appropriate tests, particularly when implementing financial calculations, data transformations, or validation rules.

## 9. Git and Development Workflow

All development work should be tracked through GitHub.

Before beginning a task:

```bash
git checkout main
git pull origin main
```

Create a new branch for the task:

```bash
git checkout -b feature/ISSUE-NUMBER-description
```

(Replace `ISSUE-NUMBER` with the relevant GitHub issue number.)

After making changes, inspect them:

```bash
git status
git diff
```

Stage and commit the changes:

```bash
git add .
git commit -m "Describe the changes"
```

Push the branch:

```bash
git push -u origin feature/ISSUE-NUMBER-description
```

Create a pull request on GitHub and reference the corresponding issue. Pull requests should explain what changed, why it changed, and how the changes were tested. Do not push directly to the `main` branch.

## 10. Development Guidelines

All contributors should follow these general practices:

- Keep changes focused on the assigned task.
- Write readable, maintainable code.
- Use descriptive names for variables, functions, classes, and files.
- Avoid unnecessary duplication.
- Handle errors explicitly.
- Write tests for new functionality.
- Document non-obvious implementation decisions.
- Keep dependencies and configuration files current.  If the database configuration is changed, a dependency is added, or changes are made to how the application starts, the relevant documentation should be updated as part of the same task.
- Never commit credentials, passwords, API keys, or sensitive financial information.
- Communicate potential conflicts or dependencies with other contributors.

## 11. Troubleshooting

**Python dependencies cannot be found**

Verify that the virtual environment is activated and that dependencies have been installed.

**The frontend cannot communicate with the backend**

Verify that the backend is running, the API address is correct, and the frontend's proxy or CORS configuration is properly configured.

**Git reports merge conflicts**

Update your local branch, review the conflicting changes, and resolve them carefully before pushing.

**Database connection errors**

Verify the database configuration, connection string, and database availability.

**A dependency installation fails**

Check the installed Python or Node.js version against the project's requirements and verify that the dependency files are current.

## 12. Keeping This Document Current

These instructions should be updated as the application architecture and development tooling evolve. Changes to dependencies, environment variables, database configuration, startup commands, and testing procedures should be reflected here so that all contributors can maintain consistent development environments.
