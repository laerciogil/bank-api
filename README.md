# Bank API

A comprehensive RESTful API for banking operations built with modern web technologies.

## Overview

This project is a study implementation of a banking API that provides core financial services through a secure and scalable RESTful interface. The API follows industry best practices for security, data validation, and error handling.

## Tech Stack

- **Backend Framework**: Python/FastAPI
- **Database**: PostgreSQL or SQLite
- **Authentication**: JWT (JSON Web Tokens)
- **API Documentation**: OpenAPI/Swagger
- **Testing**: pytest

## Current Features

### Core Banking Operations
- Account management
- Balance inquiries
- Transaction history

### API Endpoints

#### Accounts
- `GET /api/accounts` - List all accounts
- `GET /api/accounts/{id}` - Get account details
- `POST /api/accounts` - Create new account
- `PUT /api/accounts/{id}` - Update account information
- `DELETE /api/accounts/{id}` - Close account

#### Transactions
- `GET /api/transactions` - List transactions
- `GET /api/transactions/{id}` - Get transaction details
- `POST /api/transactions` - Create transaction

## Future Implementations

### Authentication & Authorization
- **User Registration & Login**
  - `POST /api/auth/register` - User registration
  - `POST /api/auth/login` - User authentication
  - `POST /api/auth/logout` - User logout
  - `POST /api/auth/refresh` - Token refresh

- **Role-Based Access Control**
  - Admin roles for bank operations
  - Customer roles for personal banking
  - Teller roles for branch operations

### Enhanced Account Management
- **Account Types**
  - Checking accounts
  - Savings accounts
  - Credit accounts
  - Investment accounts

- **Account Features**
  - Account statements
  - Account limits and restrictions
  - Joint accounts
  - Account freezing/unfreezing
  - Overdraft protection

### Banking Transactions
- **Transfers**
  - `POST /api/transfers/internal` - Internal account transfers
  - `POST /api/transfers/external` - External bank transfers
  - `POST /api/transfers/international` - International wire transfers
  - `GET /api/transfers/history` - Transfer history

- **Deposits & Withdrawals**
  - `POST /api/deposits/cash` - Cash deposits
  - `POST /api/deposits/check` - Check deposits
  - `POST /api/withdrawals/cash` - Cash withdrawals
  - `POST /api/withdrawals/atm` - ATM withdrawals

- **Payments & Bills**
  - `POST /api/payments/bills` - Bill payments
  - `POST /api/payments/recurring` - Recurring payments
  - `GET /api/payments/scheduled` - Scheduled payments
  - `POST /api/payments/cancel` - Cancel payment

### Advanced Features
- **Card Management**
  - Debit card issuance
  - Credit card management
  - Card blocking/unblocking
  - PIN management

- **Notifications**
  - SMS alerts
  - Email notifications
  - Push notifications
  - Transaction alerts

- **Reporting & Analytics**
  - Account summaries
  - Transaction reports
  - Spending analytics
  - Tax documents

## Security Features

- JWT-based authentication
- Rate limiting
- Input validation and sanitization
- HTTPS enforcement
- CORS configuration
- SQL injection prevention
- XSS protection

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:3000/api-docs`
- OpenAPI JSON: `http://localhost:3000/api-docs.json`

## Getting Started

### Prerequisites
- Python 3.14 or higher
- Database server (PostgreSQL or SQLite)
- Environment variables configuration

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd bank-api
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run database migrations:
```bash
npm run migrate
```

5. Start the development server:
```bash
npm run dev
```

### Environment Variables

```env
PORT=3000
DATABASE_URL=<your-database-url>
JWT_SECRET=<your-jwt-secret>
JWT_EXPIRES_IN=24h
```

## API Usage Examples

### Authentication
```bash
# Login
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password"}'
```

### Get Account Balance
```bash
curl -X GET http://localhost:3000/api/accounts/123/balance \
  -H "Authorization: Bearer <jwt-token>"
```

### Make a Transfer
```bash
curl -X POST http://localhost:3000/api/transfers/internal \
  -H "Authorization: Bearer <jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{"fromAccount": "123", "toAccount": "456", "amount": 100.00}'
```

## Testing

Run the test suite:
```bash
npm test
```

Run tests with coverage:
```bash
npm run test:coverage
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please contact [your-email@example.com].

---

**Note**: This is a study project for educational purposes. Do not use in production without proper security audits and compliance checks.