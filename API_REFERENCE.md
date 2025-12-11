# Library Management System - API Reference

## Base URL
```
Development: https://localhost:7xxx
Production: https://your-domain.com/api
```

## Authentication
Current MVP version does not include authentication. All endpoints are publicly accessible.

**Future versions will include:**
- JWT Bearer token authentication
- Role-based access control (Admin, Librarian, Member)

---

## Books API

### 1. Get All Books
Retrieve a list of all books in the library.

**Endpoint:** `GET /api/books`

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer | No | Page number (default: 1) |
| pageSize | integer | No | Items per page (default: 10, max: 100) |
| category | string | No | Filter by category |
| author | string | No | Filter by author |

**Response:** `200 OK`
```json
{
  "data": [
    {
      "id": 1,
      "isbn": "978-0-123456-78-9",
      "title": "The Great Book",
      "author": "John Doe",
      "publisher": "ABC Publishers",
      "publicationYear": 2023,
      "category": "Fiction",
      "totalCopies": 10,
      "availableCopies": 8,
      "price": 29.99,
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z"
    }
  ],
  "totalCount": 100,
  "page": 1,
  "pageSize": 10
}
```

---

### 2. Get Book by ID
Retrieve details of a specific book.

**Endpoint:** `GET /api/books/{id}`

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | Book ID |

**Response:** `200 OK`
```json
{
  "id": 1,
  "isbn": "978-0-123456-78-9",
  "title": "The Great Book",
  "author": "John Doe",
  "publisher": "ABC Publishers",
  "publicationYear": 2023,
  "category": "Fiction",
  "totalCopies": 10,
  "availableCopies": 8,
  "price": 29.99,
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T10:30:00Z"
}
```

**Error Response:** `404 Not Found`
```json
{
  "error": "Book not found",
  "statusCode": 404
}
```

---

### 3. Search Books
Search books by title, author, ISBN, or category.

**Endpoint:** `GET /api/books/search`

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query | string | Yes | Search term |
| searchBy | string | No | Field to search (title, author, isbn, category) |
| page | integer | No | Page number (default: 1) |
| pageSize | integer | No | Items per page (default: 10) |

**Response:** `200 OK`
```json
{
  "data": [
    {
      "id": 1,
      "isbn": "978-0-123456-78-9",
      "title": "The Great Book",
      "author": "John Doe",
      "availableCopies": 8
    }
  ],
  "totalCount": 5,
  "query": "Great"
}
```

---

### 4. Create Book
Add a new book to the library catalog.

**Endpoint:** `POST /api/books`

**Request Body:**
```json
{
  "isbn": "978-0-123456-78-9",
  "title": "The Great Book",
  "author": "John Doe",
  "publisher": "ABC Publishers",
  "publicationYear": 2023,
  "category": "Fiction",
  "totalCopies": 10,
  "availableCopies": 10,
  "price": 29.99
}
```

**Validation Rules:**
- ISBN: Required, unique, 10-17 characters
- Title: Required, max 200 characters
- Author: Required, max 200 characters
- PublicationYear: Must be between 1000 and current year
- TotalCopies: Required, minimum 1
- AvailableCopies: Cannot exceed TotalCopies
- Price: Required, minimum 0

**Response:** `201 Created`
```json
{
  "id": 1,
  "isbn": "978-0-123456-78-9",
  "title": "The Great Book",
  "author": "John Doe",
  "publisher": "ABC Publishers",
  "publicationYear": 2023,
  "category": "Fiction",
  "totalCopies": 10,
  "availableCopies": 10,
  "price": 29.99,
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T10:30:00Z"
}
```

**Error Response:** `400 Bad Request`
```json
{
  "errors": {
    "ISBN": ["ISBN already exists"],
    "Title": ["Title is required"],
    "AvailableCopies": ["Available copies cannot exceed total copies"]
  },
  "statusCode": 400
}
```

---

### 5. Update Book
Update details of an existing book.

**Endpoint:** `PUT /api/books/{id}`

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | Book ID |

**Request Body:**
```json
{
  "id": 1,
  "isbn": "978-0-123456-78-9",
  "title": "The Great Book - Updated",
  "author": "John Doe",
  "publisher": "ABC Publishers",
  "publicationYear": 2023,
  "category": "Fiction",
  "totalCopies": 15,
  "availableCopies": 13,
  "price": 34.99
}
```

**Response:** `204 No Content`

**Error Responses:**
- `400 Bad Request`: Validation errors
- `404 Not Found`: Book not found

---

### 6. Delete Book
Remove a book from the catalog.

**Endpoint:** `DELETE /api/books/{id}`

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | Book ID |

**Response:** `204 No Content`

**Error Response:** `404 Not Found`
```json
{
  "error": "Book not found",
  "statusCode": 404
}
```

**Business Rules:**
- Cannot delete a book that is currently issued
- Soft delete recommended (mark as inactive instead of hard delete)

---

## Members API

### 1. Get All Members
Retrieve a list of all library members.

**Endpoint:** `GET /api/members`

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer | No | Page number (default: 1) |
| pageSize | integer | No | Items per page (default: 10) |
| isActive | boolean | No | Filter by active status |

**Response:** `200 OK`
```json
{
  "data": [
    {
      "id": 1,
      "memberId": "LIB2024001",
      "firstName": "Jane",
      "lastName": "Smith",
      "email": "jane.smith@email.com",
      "phone": "+1-555-0100",
      "address": "123 Main St, City, State",
      "membershipDate": "2024-01-01T00:00:00Z",
      "expiryDate": "2025-01-01T00:00:00Z",
      "isActive": true,
      "createdAt": "2024-01-01T10:00:00Z",
      "updatedAt": "2024-01-01T10:00:00Z"
    }
  ],
  "totalCount": 50,
  "page": 1,
  "pageSize": 10
}
```

---

### 2. Get Member by ID
Retrieve details of a specific member.

**Endpoint:** `GET /api/members/{id}`

**Response:** `200 OK`
```json
{
  "id": 1,
  "memberId": "LIB2024001",
  "firstName": "Jane",
  "lastName": "Smith",
  "email": "jane.smith@email.com",
  "phone": "+1-555-0100",
  "address": "123 Main St, City, State",
  "membershipDate": "2024-01-01T00:00:00Z",
  "expiryDate": "2025-01-01T00:00:00Z",
  "isActive": true,
  "borrowedBooks": 2,
  "overdueBooks": 0,
  "outstandingFines": 0.00
}
```

---

### 3. Search Members
Search members by name, email, or member ID.

**Endpoint:** `GET /api/members/search`

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query | string | Yes | Search term |

**Response:** `200 OK`
```json
{
  "data": [
    {
      "id": 1,
      "memberId": "LIB2024001",
      "firstName": "Jane",
      "lastName": "Smith",
      "email": "jane.smith@email.com",
      "isActive": true
    }
  ],
  "totalCount": 3
}
```

---

### 4. Register Member
Register a new library member.

**Endpoint:** `POST /api/members`

**Request Body:**
```json
{
  "firstName": "Jane",
  "lastName": "Smith",
  "email": "jane.smith@email.com",
  "phone": "+1-555-0100",
  "address": "123 Main St, City, State"
}
```

**Validation Rules:**
- FirstName: Required, max 100 characters
- LastName: Required, max 100 characters
- Email: Required, valid email format, unique
- Phone: Optional, valid phone format
- Address: Optional, max 500 characters

**Response:** `201 Created`
```json
{
  "id": 1,
  "memberId": "LIB2024001",
  "firstName": "Jane",
  "lastName": "Smith",
  "email": "jane.smith@email.com",
  "phone": "+1-555-0100",
  "address": "123 Main St, City, State",
  "membershipDate": "2024-01-15T10:30:00Z",
  "expiryDate": "2025-01-15T10:30:00Z",
  "isActive": true
}
```

---

### 5. Update Member
Update member information.

**Endpoint:** `PUT /api/members/{id}`

**Request Body:**
```json
{
  "id": 1,
  "firstName": "Jane",
  "lastName": "Smith-Updated",
  "email": "jane.smith@email.com",
  "phone": "+1-555-0101",
  "address": "456 New St, City, State",
  "isActive": true
}
```

**Response:** `204 No Content`

---

### 6. Deactivate Member
Deactivate a member (soft delete).

**Endpoint:** `DELETE /api/members/{id}`

**Response:** `204 No Content`

**Business Rules:**
- Cannot deactivate if member has unreturned books
- Cannot deactivate if member has unpaid fines

---

## Transactions API

### 1. Get All Transactions
Retrieve all borrowing transactions.

**Endpoint:** `GET /api/transactions`

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer | No | Page number |
| pageSize | integer | No | Items per page |
| status | string | No | Filter by status (Issued, Returned, Overdue, Lost) |
| memberId | integer | No | Filter by member ID |
| bookId | integer | No | Filter by book ID |

**Response:** `200 OK`
```json
{
  "data": [
    {
      "id": 1,
      "bookId": 5,
      "memberId": 2,
      "bookTitle": "The Great Book",
      "memberName": "Jane Smith",
      "issueDate": "2024-01-01T10:00:00Z",
      "dueDate": "2024-01-15T10:00:00Z",
      "returnDate": null,
      "status": "Issued",
      "fineAmount": 0.00,
      "finePaid": false,
      "notes": ""
    }
  ],
  "totalCount": 25
}
```

---

### 2. Issue Book
Issue a book to a member.

**Endpoint:** `POST /api/transactions/issue`

**Request Body:**
```json
{
  "bookId": 5,
  "memberId": 2,
  "notes": "First-time borrower"
}
```

**Business Rules Validated:**
- Member must be active
- Member must not exceed borrowing limit (5 books)
- Member must not have overdue books
- Book must be available (availableCopies > 0)
- Auto-calculate due date (14 days from issue date)

**Response:** `201 Created`
```json
{
  "id": 1,
  "bookId": 5,
  "memberId": 2,
  "bookTitle": "The Great Book",
  "memberName": "Jane Smith",
  "issueDate": "2024-01-01T10:00:00Z",
  "dueDate": "2024-01-15T10:00:00Z",
  "status": "Issued",
  "message": "Book issued successfully"
}
```

**Error Responses:**
```json
{
  "error": "Member has exceeded borrowing limit",
  "statusCode": 400
}
```

```json
{
  "error": "Book is not available",
  "statusCode": 400
}
```

```json
{
  "error": "Member has overdue books",
  "statusCode": 400
}
```

---

### 3. Return Book
Return a borrowed book.

**Endpoint:** `POST /api/transactions/return`

**Request Body:**
```json
{
  "transactionId": 1
}
```

**Business Logic:**
- Calculate fine if overdue
- Update book availability (+1)
- Update transaction status
- Record return date

**Response:** `200 OK`
```json
{
  "id": 1,
  "bookId": 5,
  "memberId": 2,
  "issueDate": "2024-01-01T10:00:00Z",
  "dueDate": "2024-01-15T10:00:00Z",
  "returnDate": "2024-01-20T10:00:00Z",
  "status": "Returned",
  "fineAmount": 5.00,
  "finePaid": false,
  "message": "Book returned successfully. Fine: $5.00"
}
```

**Fine Calculation:**
- Days overdue = ReturnDate - DueDate
- Fine = Days overdue × $1.00 per day (configurable)
- Maximum fine = $50.00 per book (configurable)

---

### 4. Get Member Transaction History
Retrieve borrowing history for a specific member.

**Endpoint:** `GET /api/transactions/member/{memberId}`

**Response:** `200 OK`
```json
{
  "memberId": 2,
  "memberName": "Jane Smith",
  "totalBorrowed": 15,
  "currentlyBorrowed": 2,
  "totalOverdue": 0,
  "transactions": [
    {
      "id": 1,
      "bookTitle": "The Great Book",
      "issueDate": "2024-01-01T10:00:00Z",
      "dueDate": "2024-01-15T10:00:00Z",
      "returnDate": "2024-01-10T10:00:00Z",
      "status": "Returned",
      "fineAmount": 0.00
    }
  ]
}
```

---

### 5. Get Overdue Transactions
Retrieve all overdue book transactions.

**Endpoint:** `GET /api/transactions/overdue`

**Response:** `200 OK`
```json
{
  "data": [
    {
      "id": 5,
      "bookTitle": "Learning C#",
      "memberName": "John Doe",
      "memberId": "LIB2024005",
      "issueDate": "2023-12-01T10:00:00Z",
      "dueDate": "2023-12-15T10:00:00Z",
      "daysOverdue": 31,
      "fineAmount": 31.00,
      "memberEmail": "john.doe@email.com",
      "memberPhone": "+1-555-0200"
    }
  ],
  "totalCount": 8,
  "totalFines": 248.00
}
```

---

## Error Response Format

All API errors follow this consistent format:

```json
{
  "error": "Error message describing what went wrong",
  "statusCode": 400,
  "details": {
    "field1": ["Validation error for field1"],
    "field2": ["Validation error for field2"]
  },
  "timestamp": "2024-01-15T10:30:00Z",
  "path": "/api/books/123"
}
```

### HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | Success - Request completed successfully |
| 201 | Created - Resource created successfully |
| 204 | No Content - Request successful, no content to return |
| 400 | Bad Request - Invalid input or validation error |
| 404 | Not Found - Resource not found |
| 409 | Conflict - Resource already exists (e.g., duplicate ISBN) |
| 500 | Internal Server Error - Server error |

---

## Rate Limiting

**Current MVP:** No rate limiting

**Future Implementation:**
- 100 requests per minute per IP
- 1000 requests per hour per authenticated user

---

## Versioning

**Current Version:** v1

**Future versions** will be accessible via:
- URL: `/api/v2/books`
- Header: `API-Version: 2.0`

---

## Testing the API

### Using Swagger UI
1. Run the application
2. Navigate to `https://localhost:7xxx/swagger`
3. Try out endpoints interactively

### Using cURL

**Get all books:**
```bash
curl -X GET "https://localhost:7xxx/api/books" -H "accept: application/json"
```

**Create a book:**
```bash
curl -X POST "https://localhost:7xxx/api/books" \
  -H "Content-Type: application/json" \
  -d '{
    "isbn": "978-0-123456-78-9",
    "title": "The Great Book",
    "author": "John Doe",
    "publisher": "ABC Publishers",
    "publicationYear": 2023,
    "category": "Fiction",
    "totalCopies": 10,
    "availableCopies": 10,
    "price": 29.99
  }'
```

### Using Postman
Import the Postman collection provided in QUICK_START_GUIDE.md

---

## Support

For API issues or questions:
1. Check this documentation
2. Review Swagger UI documentation
3. Check application logs
4. Create an issue in the repository

---

**Last Updated:** 2024-01-15  
**API Version:** 1.0  
**Maintained By:** Library Management Team
