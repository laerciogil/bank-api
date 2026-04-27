# Bank API

A RESTful API for basic banking operations built with FastAPI and SQLAlchemy.

## Overview

This project is a fictitious banking API for learning purposes that provides core financial services through a secure RESTful interface. The API implements basic account management, transaction processing, and JWT-based authentication.

## Tech Stack

- **Backend Framework**: FastAPI 0.136.0+
- **Database**: SQLite (development) / PostgreSQL (production)
- **ORM**: SQLAlchemy with databases library for async support
- **Authentication**: JWT (JSON Web Tokens) using PyJWT
- **Data Validation**: Pydantic v2
- **Package Management**: UV
- **Testing**: pytest with httpx for async testing
- **Code Quality**: ruff for linting and formatting, mypy for type checking

## Current Features

### Authentication
- JWT-based authentication with user login
- Protected endpoints requiring authentication
- Simple user ID-based login system

### Account Management
- Create new accounts with user ID and initial balance
- List accounts with pagination (limit/skip)
- View account transaction history

### Transaction Processing
- Create transactions of three types:
  - **Deposit**: Add funds to an account
  - **Withdraw**: Remove funds from an account
  - **Transfer**: Move funds between accounts
- View transaction history for accounts
- Transaction validation and error handling

## API Endpoints

### Authentication
- `POST /auth/login` - Authenticate user and receive JWT token

### Accounts
- `GET /accounts` - List all accounts (requires authentication)
  - Query parameters: `limit` (required), `skip` (optional, default: 0)
- `POST /accounts` - Create new account (requires authentication)
- `GET /accounts/{account_id}/transactions` - Get account transactions (requires authentication)
  - Query parameters: `limit` (required), `skip` (optional, default: 0)

### Transactions
- `POST /transactions` - Create new transaction (requires authentication)
  - Supported types: `deposit`, `withdraw`, `transfer`

### Root
- `GET /` - Welcome message and API info

## Database Schema

### Accounts Table
- `id` (Integer, Primary Key)
- `user_id` (Integer, Not Null)
- `balance` (Numeric(10,2), Not Null)
- `created_at` (Timestamp with timezone)

### Transactions Table
- `id` (Integer, Primary Key)
- `account_id` (Integer, Foreign Key to accounts.id)
- `type` (Enum: deposit, withdraw, transfer)
- `amount` (Numeric(10,2), Not Null)
- `created_at` (Timestamp with timezone)

## Getting Started

### Prerequisites
- Python 3.14+
- UV package manager
- SQLite (for development) or PostgreSQL (for production)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd bank-api
```

2. Set up development environment:
```bash
make dev-setup
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Running the Application

Start the development server:
```bash
make run
# Or
uv run bank-api
```

The API will be available at `http://localhost:8000`

### Environment Variables

```env
DATABASE_URL=sqlite:///./bank.db  # or postgresql://user:pass@localhost/dbname
ENVIRONMENT=DEV  # or PROD
```

## API Usage Examples

### Authentication
```bash
# Login
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1}'
```

### Create Account
```bash
curl -X POST http://localhost:8000/accounts \
  -H "Authorization: Bearer <jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "balance": 1000.00}'
```

### Create Transaction
```bash
# Deposit
curl -X POST http://localhost:8000/transactions \
  -H "Authorization: Bearer <jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{"account_id": 1, "type": "deposit", "amount": 500.00}'

# Withdraw
curl -X POST http://localhost:8000/transactions \
  -H "Authorization: Bearer <jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{"account_id": 1, "type": "withdraw", "amount": 200.00}'
```

### List Accounts
```bash
curl -X GET "http://localhost:8000/accounts?limit=10&skip=0" \
  -H "Authorization: Bearer <jwt-token>"
```

## Development

### Code Quality

Run code quality checks:
```bash
make code-style-check    # Linting with ruff
make code-style-format   # Format code with ruff
make code-static-check   # Type checking with mypy
```

### Testing

Run the test suite:
```bash
make quality-check    # Run tests with coverage
```

### Available Make Commands

- `make dev-setup` - Set up development environment
- `make run` - Run the application
- `make clean` - Clean cache and temp files
- `make clean-all` - Clean all files including virtual environment
- `make code-style-check` - Run linting
- `make code-style-format` - Format code
- `make code-static-check` - Run type checking
- `make quality-check` - Run tests with coverage
- `make help` - Show all available commands

## Project Structure

```
src/bank_api/
├── __init__.py
├── main.py              # FastAPI application entry point
├── config.py            # Configuration settings
├── database.py          # Database connection and metadata
├── security.py          # JWT authentication utilities
├── exceptions.py        # Custom exception classes
├── controllers/         # API route handlers
│   ├── auth.py         # Authentication endpoints
│   ├── account.py      # Account management endpoints
│   ├── transaction.py  # Transaction endpoints
│   └── root.py         # Root endpoint
├── models/              # Database models
│   ├── account.py      # Account table definition
│   └── transaction.py  # Transaction table definition
├── schemas/             # Pydantic schemas for request/response
│   ├── auth.py         # Authentication schemas
│   ├── account.py      # Account schemas
│   └── transaction.py  # Transaction schemas
├── views/               # Response models
├── service/             # Business logic layer
└── tests/               # Test files
```

## Error Handling

The API implements custom error handling for:
- **404 Not Found**: Account not found errors
- **409 Conflict**: Business logic errors (e.g., insufficient funds)

## Security Features

- JWT-based authentication for protected endpoints
- Input validation using Pydantic models
- CORS middleware configured for development
- SQL injection prevention through SQLAlchemy ORM

## License

This project is licensed under the MIT License.

---

**Note**: This is a fictitious banking API created for educational purposes. Do not use in production without proper security audits and compliance checks.